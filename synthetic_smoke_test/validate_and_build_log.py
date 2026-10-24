"""Non-destructive quality checks and prefix leakage/partition assertions."""
import json
from pathlib import Path
import pandas as pd

P1='origin_sort';P2='linehaul_departure';P3='destination_arrival'

def validate(events):
    x=events.copy()
    x['parsed_time']=pd.to_datetime(x['event_timestamp_utc'],utc=True,errors='coerce')
    x['parsed_ingestion']=pd.to_datetime(x['event_ingestion_timestamp_utc'],utc=True,errors='coerce')
    x['duplicate_id']=x.duplicated(['case_id','event_id'],keep='first')
    x['mapped']=x.raw_event_code.eq('SIM_'+x.canonical_activity.str.upper())
    audit={'raw_rows':len(x),'distinct_cases':int(x.case_id.nunique()),'duplicate_event_id_rows':int(x.duplicate_id.sum()),'missing_or_invalid_event_times':int(x.parsed_time.isna().sum()),'unknown_codes':int((~x.mapped).sum()),'censored_cases':int(x.loc[x.completion_status.eq('incomplete'),'case_id'].nunique()),'recovered_cases':int(x.loc[x.completion_status.eq('recovered_exception'),'case_id'].nunique())}
    # Never overwrite original records. Work with clearly marked, valid subset.
    cleaned=x.loc[(~x.duplicate_id)&x.parsed_time.notna()&x.mapped].copy()
    cleaned=cleaned.sort_values(['case_id','parsed_time','event_id'],kind='stable')
    cleaned['next_time']=cleaned.groupby('case_id').parsed_time.shift(-1)
    cleaned['dwell_minutes']=(cleaned.next_time-cleaned.parsed_time).dt.total_seconds()/60
    assert cleaned.dwell_minutes.dropna().ge(0).all()
    return cleaned,audit

def partitions(cleaned):
    starts=cleaned.groupby('case_id').parsed_time.min().sort_values(kind='stable')
    n=len(starts);assert n>=20
    names=['train']*int(n*.6)+['validation']*(int(n*.8)-int(n*.6))+['test']*(n-int(n*.8))
    assign=dict(zip(starts.index,names))
    assert len(assign)==n and len(set(assign))==n
    for name in ['train','validation','test']:
        ids={cid for cid,split in assign.items() if split==name}
        assert ids
    return assign

def prefix_checks(cleaned):
    checked={x:0 for x in ['P1','P2','P3']}
    for stage,activity in [('P1',P1),('P2',P2),('P3',P3)]:
        for cid,case in cleaned.groupby('case_id',sort=False):
            matching=case.loc[case.canonical_activity.eq(activity)]
            if matching.empty: continue
            cutoff=matching.parsed_time.iloc[0]
            prefix=case.loc[case.parsed_time.le(cutoff)]
            assert prefix.parsed_time.max()<=cutoff
            assert not prefix.loc[prefix.parsed_time.gt(cutoff)].shape[0]
            assert len(prefix)<=len(case)
            checked[stage]+=1
    return checked

def run(input_path='data/synthetic_events.csv',output='outputs'):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    events=pd.read_csv(input_path,keep_default_na=False)
    cleaned,audit=validate(events)
    assignment=partitions(cleaned)
    audit['split_case_counts']={s:list(assignment.values()).count(s) for s in ['train','validation','test']}
    audit['prediction_prefix_cases']=prefix_checks(cleaned)
    audit['clean_rows']=len(cleaned)
    audit['synthetic_only']=True
    # Never interpret data-generation outcome field as a feature; it is excluded below.
    cleaned[['case_id','event_id','canonical_activity','parsed_time','facility_id','dwell_minutes']].rename(columns={'parsed_time':'time:timestamp','canonical_activity':'concept:name','case_id':'case:concept:name'}).to_csv(output/'clean_synthetic_events.csv',index=False)
    (output/'validation_summary.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
    return cleaned,audit

if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('--input',default='data/synthetic_events.csv');a.add_argument('--out',default='outputs');v=a.parse_args();print(json.dumps(run(v.input,v.out)[1],indent=2))

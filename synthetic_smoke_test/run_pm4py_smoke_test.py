"""Real PM4Py discovery on solely synthetic generated data."""
import argparse
import json
from collections import Counter
from pathlib import Path
import pandas as pd
from validate_and_build_log import run

def main(input_path='data/synthetic_events.csv',out='outputs'):
    try:
        import pm4py
    except ImportError as exc:
        raise SystemExit('PM4Py is not installed. Run: python -m pip install -r requirements.txt') from exc
    dest=Path(out);dest.mkdir(parents=True,exist_ok=True)
    cleaned,audit=run(input_path,out)
    log=cleaned.rename(columns={'case_id':'case:concept:name','canonical_activity':'concept:name','parsed_time':'time:timestamp'})
    log=log[['case:concept:name','concept:name','time:timestamp']].copy()
    log=pm4py.format_dataframe(log,case_id='case:concept:name',activity_key='concept:name',timestamp_key='time:timestamp')
    dfg,start,end=pm4py.discover_dfg(log)
    tree=pm4py.discover_process_tree_inductive(log)
    net,initial,final=pm4py.convert_to_petri_net(tree)
    pm4py.write_pnml(net,initial,final,str(dest/'synthetic_inductive_model.pnml'))
    edge_rows=[{'source':str(a),'target':str(b),'frequency':int(n)} for (a,b),n in sorted(dfg.items())]
    pd.DataFrame(edge_rows,columns=['source','target','frequency']).to_csv(dest/'synthetic_dfg.csv',index=False)
    variants=Counter(tuple(g['concept:name']) for _,g in log.sort_values(['case:concept:name','time:timestamp'],kind='stable').groupby('case:concept:name',sort=False))
    ranked=[{'variant':' > '.join(k),'cases':int(v)} for k,v in variants.most_common()]
    pd.DataFrame(ranked,columns=['variant','cases']).to_csv(dest/'synthetic_variants.csv',index=False)
    rework=int(sum((g.canonical_activity=='origin_sort').sum()>1 for _,g in cleaned.groupby('case_id')))
    positive=cleaned.dwell_minutes.dropna()
    summary={'synthetic_only':True,'pm4py_version':getattr(pm4py,'__version__','unknown'),'case_count':audit['distinct_cases'],'valid_event_rows':len(cleaned),'dfg_edges':len(dfg),'variants':len(variants),'synthetic_rework_cases':rework,'median_inter_event_dwell_minutes':float(positive.median()),'audit':audit,'top_variants':ranked[:5]}
    (dest/'smoke_test_results.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    lines=['# Strictly synthetic PM4Py smoke-test results','','**NOT FEDEX DATA OR EMPIRICAL FEDEX FINDINGS.**','','Generated using artificial logistics-inspired transitions and invented codes/locations.','',f"PM4Py version: `{summary['pm4py_version']}`",f"Cases: **{summary['case_count']}**; valid mapped event rows: **{summary['valid_event_rows']}**.",f"DFG edges: **{summary['dfg_edges']}**; full-trace variants: **{summary['variants']}**.",f"Cases containing repeated origin sorting: **{rework}**.",f"Median adjacent-event dwell (minutes): **{summary['median_inter_event_dwell_minutes']:.2f}**.",'','## Synthetic quality checks','']
    lines += [f'- {k}: {v}' for k,v in audit.items()]
    lines += ['','## Five most frequent synthetic variants','']
    lines += [f"- {x['cases']} cases: {x['variant']}" for x in ranked[:5]]
    lines += ['','## Files','', '- `synthetic_dfg.csv`: observed artificial directly-follows edges', '- `synthetic_inductive_model.pnml`: PM4Py-discovered synthetic model', '- `synthetic_variants.csv`: artificial trace variants', '- `smoke_test_results.json`: machine-readable summary', '', 'No empirical FedEx operational effects, data quality, process compliance, or model accuracy are claimed.','']
    (dest/'smoke_test_results.md').write_text('\n'.join(lines),encoding='utf-8')
    print('\n'.join(lines[:10]))

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--input',default='data/synthetic_events.csv');a.add_argument('--out',default='outputs');v=a.parse_args();main(v.input,v.out)

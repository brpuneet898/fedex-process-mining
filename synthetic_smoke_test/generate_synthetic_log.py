"""Deterministic FICTIONAL event-log generator; never uses operational data."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

BASE = pd.Timestamp('2026-01-01T00:00:00Z')
NORMAL = ['origin_arrival','origin_sort','load','linehaul_departure','destination_arrival','destination_sort','onward_handoff']
LOC = {'origin_arrival':'HUB_A','origin_sort':'HUB_A','load':'HUB_A','linehaul_departure':'CORRIDOR_X','destination_arrival':'HUB_B','destination_sort':'HUB_B','onward_handoff':'HUB_B','exception_recorded':'HUB_A','recovery_recorded':'HUB_A','terminal_failure':'HUB_A'}

def generate(seed=42, cases=200):
    if cases < 20: raise ValueError('Use >=20 cases to cover all injected test scenarios')
    rng = np.random.default_rng(seed)
    records, truth = [], []
    for k in range(cases):
        cid=f'SIM_CASE_{k:05d}'
        scenario=['normal','rework','recovered_exception','terminal_failure','censored','duplicate','missing_timestamp','late_ingestion','revised_deadline','unmapped_code'][k%10]
        offset = pd.Timedelta(hours=k*12)
        current=BASE+offset
        deadline=current+pd.Timedelta(hours=20)
        path=list(NORMAL)
        if scenario=='rework': path.insert(2,'origin_sort')
        if scenario=='recovered_exception': path[2:2]=['exception_recorded','recovery_recorded']
        if scenario=='terminal_failure': path=path[:3]+['terminal_failure']
        if scenario=='censored': path=path[:4]
        ingested=[]
        for j,activity in enumerate(path):
            if j: current += pd.Timedelta(minutes=int(rng.integers(30, 90)))
            event_id=f'{cid}_EV_{j:02d}'
            code='SIM_'+activity.upper()
            if scenario=='unmapped_code' and j==1: code='SIM_UNKNOWN_CODE'
            t=current.isoformat()
            if scenario=='missing_timestamp' and j==1: t=''
            ingress=current+pd.Timedelta(minutes=5 if scenario!='late_ingestion' else (180 if j==1 else 5))
            status=('failed' if scenario=='terminal_failure' else 'incomplete' if scenario=='censored' else 'recovered_exception' if scenario=='recovered_exception' else 'successful')
            row=dict(case_id=cid,event_id=event_id,raw_event_code=code,canonical_activity=activity,event_timestamp_utc=t,event_timezone_raw='UTC',event_ingestion_timestamp_utc=ingress.isoformat(),facility_id=LOC[activity],corridor_id='CORRIDOR_X',exception_flag=activity=='exception_recorded',recovery_flag=activity=='recovery_recorded',case_start_flag=j==0,terminal_event_flag=activity in ['onward_handoff','terminal_failure'],completion_status=status,service_deadline_utc=(deadline+pd.Timedelta(hours=2) if scenario=='revised_deadline' else deadline).isoformat(),extraction_timestamp_utc=(BASE+pd.Timedelta(days=180)).isoformat())
            records.append(row)
            ingested.append(event_id)
            if scenario=='duplicate' and j==1: records.append(dict(row))
        truth.append(dict(case_id=cid,scenario=scenario,generated_outcome=status,expected_events=len(path),injected_duplicate_records=int(scenario=='duplicate'),injected_missing_timestamps=int(scenario=='missing_timestamp'),injected_unknown_codes=int(scenario=='unmapped_code'),injected_rework=int(scenario=='rework'),injected_exception=int(scenario=='recovered_exception'),seed=seed))
    events=pd.DataFrame(records)
    return events,pd.DataFrame(truth)

def write(seed=42,cases=200,out='data'):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    e,t=generate(seed,cases)
    e.to_csv(out/'synthetic_events.csv',index=False)
    t.to_csv(out/'synthetic_ground_truth.csv',index=False)
    digest=hashlib.sha256((out/'synthetic_events.csv').read_bytes()).hexdigest()
    manifest={'synthetic_only':True,'seed':seed,'cases':cases,'rows':len(e),'event_sha256':digest,'scenario_counts':{str(k):int(v) for k,v in t.scenario.value_counts().items()},'warning':'Fictional labels, timings, codes and locations; NOT FedEx operational information.'}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    return manifest

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--seed',type=int,default=42);a.add_argument('--cases',type=int,default=200);a.add_argument('--out',default='data');v=a.parse_args()
    print(json.dumps(write(v.seed,v.cases,v.out),indent=2))

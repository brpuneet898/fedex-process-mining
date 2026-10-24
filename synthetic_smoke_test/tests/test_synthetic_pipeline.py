import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pandas as pd
from generate_synthetic_log import generate, write
from validate_and_build_log import validate, partitions, prefix_checks

def test_repeatability():
    a,t=generate(42,200);b,u=generate(42,200)
    pd.testing.assert_frame_equal(a,b)
    pd.testing.assert_frame_equal(t,u)

def test_fixed_seed_differs():
    assert not generate(42,200)[0].equals(generate(43,200)[0])

def test_scenarios_present():
    _,truth=generate(42,200)
    assert truth.scenario.nunique()==10
    assert truth.scenario.value_counts().eq(20).all()

def test_injected_anomalies_and_cleaning():
    events,truth=generate(42,200)
    clean,audit=validate(events)
    assert audit['duplicate_event_id_rows']==20
    assert audit['missing_or_invalid_event_times']==20
    assert audit['unknown_codes']==20
    assert audit['censored_cases']==20
    assert audit['recovered_cases']==20
    assert len(clean)==len(events)-60

def test_rehandling_retained():
    cleaned,_=validate(generate(42,200)[0])
    repeated=sum((g.canonical_activity=='origin_sort').sum()>1 for _,g in cleaned.groupby('case_id'))
    assert repeated==20

def test_partition_disjoint_and_chronological():
    cleaned,_=validate(generate(42,200)[0]); splits=partitions(cleaned)
    assert set(splits.values())=={'train','validation','test'}
    starts=cleaned.groupby('case_id').parsed_time.min().sort_values()
    sequence=[splits[cid] for cid in starts.index]
    assert sequence==sorted(sequence,key={'train':0,'validation':1,'test':2}.get)

def test_prefix_cutoffs():
    cleaned,_=validate(generate(42,200)[0]); results=prefix_checks(cleaned)
    assert results['P1']==160  # missing or unmapped synthetic P1 scans
    assert results['P2']>0
    assert results['P3']>0

def test_incomplete_not_labelled_success():
    events,_=generate(42,200)
    censored=events[events.completion_status=='incomplete']
    assert not censored.terminal_event_flag.any()
    assert censored.case_id.nunique()==20

def test_recovery_not_failure():
    events,truth=generate(42,200)
    ids=set(truth.loc[truth.scenario=='recovered_exception','case_id'])
    recovered=events[events.case_id.isin(ids)]
    assert recovered.completion_status.eq('recovered_exception').all()
    assert recovered.recovery_flag.sum()==20

def test_file_manifest(tmp_path):
    m=write(42,200,tmp_path)
    assert m['synthetic_only'] and m['cases']==200
    assert (tmp_path/'synthetic_events.csv').exists()
    assert (tmp_path/'synthetic_ground_truth.csv').exists()

def test_pm4py_inductive_and_dfg_if_installed(tmp_path):
    import pytest
    pytest.importorskip('pm4py')
    from run_pm4py_smoke_test import main
    dat=tmp_path/'data';write(42,200,dat)
    main(dat/'synthetic_events.csv',tmp_path/'outputs')
    assert (tmp_path/'outputs'/'synthetic_inductive_model.pnml').is_file()
    assert (tmp_path/'outputs'/'smoke_test_results.md').is_file()
    assert pd.read_csv(tmp_path/'outputs'/'synthetic_dfg.csv').shape[0]>0

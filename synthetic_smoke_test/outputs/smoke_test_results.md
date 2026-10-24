# Strictly synthetic PM4Py smoke-test results

**NOT FEDEX DATA OR EMPIRICAL FEDEX FINDINGS.**

Generated using artificial logistics-inspired transitions and invented codes/locations.

PM4Py version: `2.7.23.11`
Cases: **200**; valid mapped event rows: **1300**.
DFG edges: **12**; full-trace variants: **6**.
Cases containing repeated origin sorting: **20**.
Median adjacent-event dwell (minutes): **61.00**.

## Synthetic quality checks

- raw_rows: 1360
- distinct_cases: 200
- duplicate_event_id_rows: 20
- missing_or_invalid_event_times: 20
- unknown_codes: 20
- censored_cases: 20
- recovered_cases: 20
- split_case_counts: {'train': 120, 'validation': 40, 'test': 40}
- prediction_prefix_cases: {'P1': 160, 'P2': 180, 'P3': 160}
- clean_rows: 1300
- synthetic_only: True

## Five most frequent synthetic variants

- 80 cases: origin_arrival > origin_sort > load > linehaul_departure > destination_arrival > destination_sort > onward_handoff
- 40 cases: origin_arrival > load > linehaul_departure > destination_arrival > destination_sort > onward_handoff
- 20 cases: origin_arrival > origin_sort > origin_sort > load > linehaul_departure > destination_arrival > destination_sort > onward_handoff
- 20 cases: origin_arrival > origin_sort > exception_recorded > recovery_recorded > load > linehaul_departure > destination_arrival > destination_sort > onward_handoff
- 20 cases: origin_arrival > origin_sort > load > terminal_failure

## Files

- `synthetic_dfg.csv`: observed artificial directly-follows edges
- `synthetic_inductive_model.pnml`: PM4Py-discovered synthetic model
- `synthetic_variants.csv`: artificial trace variants
- `smoke_test_results.json`: machine-readable summary

No empirical FedEx operational effects, data quality, process compliance, or model accuracy are claimed.

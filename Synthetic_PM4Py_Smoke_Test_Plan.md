# FedEx Process Mining Extension — Strictly Synthetic PM4Py Smoke-Test Plan

## 1. Purpose and restrictions
Demonstrate that the planned Python/PM4Py software pipeline can ingest a **fully artificial** shipment-event table, derive a Directly-Follows Graph (DFG), run Inductive Miner, summarize trace variants, and calculate simple dwell/rehandling measures. The exercise is **not** a FedEx process reconstruction, an audit of FedEx quality or an SOP-conformance finding. No protected route, scan, SOP, case or operational field values may be used. Public repository use requires prior internal clearance even though the example is synthetic.

## 2. Artificial toy workflow
Use neutral fictitious facility labels `HUB_A`, `CORRIDOR_X`, `HUB_B` (not real codes) and invented events:
`origin_arrival → origin_sort → load → linehaul_departure → destination_arrival → destination_sort → onward_handoff`.
Simulated disruptions may include extra `origin_sort` (actual rehandling), an `exception_recorded → recovery_recorded` loop, longer delay before departure, missed synthetic movement/reassignment, diversion, return and a terminal failure. Generated outcome proportions, dwell times and dates are **assumed parameters chosen for software testing**, never empirical FedEx estimates.

## 3. Artificial schema and data generation
Generate a deterministic set of fictional cases with a fixed random seed; e.g., 100–300 illustrative cases, clearly parameterized rather than a claimed expected shipment volume. Use keys `case_id`, `raw_event_code` (invented `SIM_*` codes), `canonical_activity`, `event_timestamp_utc`, `event_timezone_raw`, `facility_id`, `corridor_id`, `event_id`, `exception_flag`, `recovery_flag`, `case_start_flag`, `terminal_event_flag`, `completion_status`, `service_deadline_utc`, `extraction_timestamp_utc`. Add versioned toy plans and piece IDs only to verify optional handling; do not fill all conditional fields with made-up values in the real schema. Keep separate **generator ground truth** (injected failure, duplicate, exception, missingness and simulated event) from observed synthetic event logs.

Test scenarios (toggle independently): clean normal paths; repeated true sorting with distinct IDs; exact duplicated event IDs; missing timestamp/timezone; out-of-order ingestion vs valid occurrence time; missing terminal scan/right-censored case; late event entry; exception with recovery before deadline; unrecovered terminal exception; amended synthetic deadline; and concept drift between synthetic periods.

## 4. Intended execution steps
1. **Generate:** `python generate_synthetic_log.py --seed 42 --cases 200 --out data/synthetic_events.csv` (illustrative future command, not evidence of an existing script).
2. **Validate/canonicalize:** preserve original synthetic code and timestamps; normalize event times to UTC; flag unrecognized codes and missingness; record duplicate decisions with event IDs. Never eliminate genuine handling repetitions.
3. **Build event log:** sort by `case_id`, occurrence timestamp and documented deterministic tie-break; convert to PM4Py DataFrame/event log with case ID, activity and timestamp keys.
4. **Discover:** construct DFG with counts/performance and Inductive Miner Petri net or process tree; export visualizations only if dependencies/renderer are available.
5. **Summarize:** rank full-case variants; describe synthetic event/case counts and durations, adjacent-event dwell distributions and count of rehandling loops; separately report incomplete traces.
6. **Check reference distinction:** the toy workflow is a **synthetic generator specification**. Optional conformity to that toy workflow tests code only; never label it FedEx normative compliance.
7. **Partition test:** create non-overlapping chronological train/validation/test *shipment sets*; assert no case spans partitions; create event prefixes at invented P1/P2/P3 points and assert no future event/updated outcome/deadline leaks into early prefixes.

## 5. Smoke-test acceptance assertions
| Check | Expected test behavior (synthetic only) |
|---|---|
| Trace identity | Every case's permitted event IDs grouped consistently; no case crosses temporal partitions |
| Date handling | Converted UTC timestamps match injected truth, with explicit flags for invalid/ambiguous times |
| Mapping | Every known invented `SIM_*` code maps deterministically; unknown code remains unmapped |
| Genuine rehandling | Distinct-ID repeated sorts survive and appear in trace variants/rework counts |
| Accidental duplicate | Exact duplicate-ID copy is flagged without silently discarding audit evidence |
| Incomplete cases | Censored cases stay unlabelled for supervised outcomes |
| Exception/recovery | Injected recovered case distinguishes recovery from terminal failure |
| Discovery | Nonempty DFG and Inductive Miner output for valid synthetic traces; common injected normal path observed |
| Dwell | No negative dwell after valid event occurrence ordering; deliberately flawed scans are reported |
| Leakage | Pre-P1/P2/P3 features cannot access subsequently observed events/outcome status |
| Reproducibility | Fixed seed yields stable generation and summary counts |

## 6. Proposed code organization if approved for implementation
```
synthetic_smoke_test/
  README.md                    # Labels all content synthetic
  requirements.txt             # Version-pinned Python, pandas, pm4py
  generate_synthetic_log.py
  validate_and_build_log.py
  run_pm4py_smoke_test.py
  tests/test_synthetic_pipeline.py
  data/                       # Only demonstrably synthetic records
  outputs/                    # Only demonstrably synthetic artifacts
```
The above is a **proposed file tree**, not a claim that the scripts or figures are included in this checkpoint package.

# FedEx Process Mining Extension — Data-Quality Audit Plan & Month-2 Feasibility Protocol

## 1. Authority and prerequisites
The audit runs **only** after documented authorization, approved secure environment and owner-confirmed definitions. The protocol operationalizes the **signed-off Research Proposal §4.2** (also Technical Annexe §22), not new feasibility cutoffs. Final denominators and corrections require approval before inspection of outcomes. Logs, confidential mappings, SOPs and outputs must remain inside the approved environment. Synthetic examples are software checks only.

## 2. Unit, intake and lineage
- **Case:** one pseudonymous individual shipment by default; multi-piece treatment pending owner decision. No single shipment's events may be split across temporal partitions.
- **Event:** one actual recorded operational occurrence, with source event ID when available; distinguish event occurrence time from ingestion time.
- **Process boundary:** first valid origin-hub acceptance/arrival into the specified corridor through destination-hub processing completion and outward handoff/departure, or an authorized terminal interruption.
- **Audit manifest:** extract date/as-of date; owner/authorization reference; source system/version; time coverage; mapping version; data classification; record counts before/after every filtering step; secure storage location (internally only).
- Keep a reproducible lineage table (`input_count`, `excluded_count`, `reason`, `output_count`) per step. Do not auto-delete repeated scans merely because activity and time repeat.

## 3. Locked feasibility measures: definitions, denominators, reporting
These are **proposed Go requirements** in the signed-off proposal; written authorization and permissible reporting are independent gates. Calculations show numerator **n** / denominator **N**, observed percentage and uncertainty/limitations where applicable. Predefine the definition of 'usable event', 'required event', 'candidate supervised case' and 'mature case' with the data owner; publish denominator sensitivity.

| Criterion | Proposed Go requirement | Planned operational measurement | Handling if unresolved |
|---|---|---|---|
| Consistent case ID | **≥99% of usable events** | n = usable events linked to a valid, stable, internally consistent pseudonymous case; N = all usable events per approved definition; report orphan/conflicting IDs separately | Flag as pending; do not silently remove bad-ID events from denominator |
| Usable activity/event | **≥95%** | n = in-scope events with a valid approved raw-code→canonical activity; N = events eligible for mapping; log unknown and ambiguous codes | Report unmapped frequency and source-system breakdown |
| Required timestamp validity | **≥95% of required events** | n = required events with parseable, nonambiguous occurrence time and verified time-zone conversion; N = all required events; separately report missing, DST ambiguity and ingestion-only dates | Keep invalid as NULL; no fabricated event time |
| Chronological consistency | **Major errors correctable or reproducibly excludable** | Count cases/events with negative dwell, impossible ordering, future time, local/UTC conflict, same-time ambiguities; document cause and reproducible fix/exclusion | Qualitative gate; no ad hoc pass percentage |
| Service/process commitment | **≥90% of candidate supervised cases** | n = candidate supervised cases with valid applicable terminal deadline/commitment; N = all candidate cases according to predefined inclusion rules | Do not label outcome on missing deadline; report case-level coverage |
| Reliable terminal outcome | **≥90% of mature cases** | n = mature cases with trustworthy observed terminal outcome via approved rule/authoritative feed; N = mature in-scope cases as of extract; report immature/right-censored separately | Never infer failure from a missing terminal scan |
| Observation duration | **≥6 consecutive months preferred** | Actual first/last occurrence date, consecutive coverage and missing periods by source | Adequacy target, **not universal hard cutoff** |
| Pilot coverage | **Origin hub + corridor + destination hub** | Observed facility/segment presence, coverage by service and period; gaps/missing scans | Require selected in-scope pilot coverage |
| Failure prevalence | **Preferred ≥500 overall, ≥100 temporal test** | Count operational failures by authoritative definition, stage and planned temporal windows; show prevalence and test-window precision limits | Adequacy preference, not a hard cutoff |
| Exceptions | **Sufficient recovered and unrecovered cases** | Counts/rates by exception type, recovery status and observation window | Record scarcity and inference limits |
| Reference process | **SOP, route rules, milestone rules OR agreed behavioural reference** | Owner-approved source, version, effective period; distinguish normative vs behavioural | No normative compliance claim with derived model alone |
| Data permission | **Written authorization for approved analysis** | Written authorization reference and secure environment approval | Block real-data analysis until confirmed |
| Reporting/publication | **Internal/external rules clarified** | Written permitted-audience/output and external-publication conditions | Do not disseminate protected results |

## 4. Specific audit tests and outputs
1. **Inventory & coverage:** raw event count, usable event count, distinct case count, events/case quantiles, periods, source systems, facility/corridor and service coverage; repeated and orphan events.
2. **IDs & case construction:** NULL IDs, changes/aliases, many-to-one/multi-piece ambiguity, same-event cross-case conflicts, case start completeness and uniqueness, premature terminal markers.
3. **Activity mapping:** raw-code distribution, matched/unmatched/ambiguous codes, unmapped by facility/service/version, versioned mapping approvals.
4. **Clock integrity:** parse failures, missing timezones, DST ambiguous/nonexistent local time, future/implausible dates, event-vs-ingestion lag, UTC conversion verification, tied/out-of-order scans.
5. **Duplicates versus genuine repeats:** exact repeat of immutable `event_id`/payload vs repeated real handling with distinct events; record **rule, affected rows, review evidence and uncertainty**; avoid collapsing rework.
6. **Sequence & duration:** impossible start/end ordering, negative or implausible dwell, looping, transitions across unexpected facilities, case durations, very short/long traces. Use data-owner-approved rules, not invented operational cutoffs.
7. **Commitment & outcomes:** deadline availability/version, outcome-source reliability, recovered exceptions distinct from missed-deadline failures, cancellations/returns/diversions separated, contradictory statuses and late corrections.
8. **Censoring:** right-censor active/incomplete cases at extraction cutoff; measure mature vs immature cases, unresolved outcome fraction and temporal edge effects.
9. **Exceptions:** counts, types, terminal vs nonterminal, recovered vs unrecovered, recovery time only when semantically valid.
10. **Partition readiness:** candidate time-ordered train/validation/untouched test periods; assign **entire shipment** to one partition, holdout last period, count mature positives per window; prohibit future-event/predictor leakage at P1/P2/P3.
11. **Measurement limits:** unrecorded physical actions, scan delays, incomplete source-system capture, ambiguity in normative reference and service commitments.

## 5. Proposed processing sequence
`authorized raw intake → immutable raw inventory → source/timezone verification → versioned code mapping → approved ID/case linkage → start/end detection → duplicate/rehandling adjudication → temporal QA → maturity/outcome reconciliation → metric computation → restricted results/report`. Every rule gets a version, owner decision, affected count and reversibility note.

## 6. Results template (populate ONLY with approved real data)
| Metric | n/N | Actual % / count | Threshold or preference | Evidence/version | Result |
|---|---|---|---|---|---|
| Case-ID consistency | Not measured | Not measured | ≥99% | Pending | Not assessed |
| Activity-code usability | Not measured | Not measured | ≥95% | Pending | Not assessed |
| Timestamp validity | Not measured | Not measured | ≥95% | Pending | Not assessed |
| Service-commitment coverage | Not measured | Not measured | ≥90% | Pending | Not assessed |
| Reliable mature-case outcomes | Not measured | Not measured | ≥90% | Pending | Not assessed |
| Chronological consistency | Not measured | Not measured | Reproducibly correctable/excludable | Pending | Not assessed |
| Duration, volume and failure cases | Not measured | Not measured | Preferred adequacy checks | Pending | Not assessed |
| Coverage, exception, reference, permissions | Not measured | Not measured | Review each condition | Pending | Not assessed |

## 7. Month-2 recommendation framework (not a current decision)
- **Go:** approved access/governance; measured core quality thresholds satisfied; corridor coverage and process definitions sufficient; chronology addressable; enough evidence for defensible analyses and meaningful temporal validation.
- **Conditional Go:** defined, remedyable gaps (e.g., restricted service strata, mapping clarification, limited failures) with owner, deadline, restricted scope, planned re-audit and explicit uncertainty; never override missing written analysis permission.
- **No-Go:** analysis not authorized; critical IDs/times/outcomes not recoverable; fundamental coverage absent; or irreparable limitations prevent the central questions being answered.
- Record decision-maker, meeting/date, exact measured basis, caveats, remediation tasks, permitted next steps. Do **not** issue a Month-2 classification until evidence exists.

If service failure is too rare for meaningful modelling, any broader disruption target must be **prospectively agreed before model development**, not redefined after testing. Conformance to FedEx policy requires approved normative SOP/route/milestone rules. Without these, describe any model as an observed behavioural comparator.

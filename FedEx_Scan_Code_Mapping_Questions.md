# FedEx Process Mining Extension — Scan-Code Mapping & Operational Semantics Questions

## A. Source inventories and code dictionary
1. Which source system(s) generate shipment scans, status transitions, planned milestones and terminal outcomes? What are their event IDs and update/version semantics?
2. Is there an authorized **scan-code dictionary** containing raw code, description, source system, expected activity, facility context, applicable event time, effective dates and inactive/renamed-code history?
3. Which codes signify genuine physical handling, automated status propagation, scheduled intent, corrections, administrative changes or synthesized statuses?
4. Are codes facility-, service-, country- or software-version-dependent? Who approves mappings and resolves ambiguous codes?
5. Can a code be counted as a **usable canonical activity** only after validation against its source system and operational meaning? Which codes must remain unmapped?

## B. Pilot boundaries and case identity
6. Which **one origin hub → line-haul movement/corridor → destination hub** is feasible and approved for the pilot? What operational scope restrictions apply?
7. Which code(s) confirm the **first valid acceptance/arrival at the origin hub for this corridor**? How are preceding or out-of-boundary events handled?
8. Which code(s) confirm **completed destination processing followed by successful onward handoff/departure**? Does an arrival scan ever count as terminal success? (Proposed rule: no.)
9. Is a stable de-identified ID available **across all relevant scan systems**, including diversions, returns, reassignment and replacement IDs?
10. For a **multi-piece shipment**, are scans piece-level, shipment-level or mixed? Does the authorized project trace represent one shipment or several pieces? What linked pseudonymous hierarchy and aggregation rule avoids duplicate case inflation?
11. Can shipment identifiers be reused, merged or split? Which linkage table, pseudonymization method and permitted steward handles these cases?

## C. Time, ordering, duplication and provenance
12. Does each timestamp record **physical occurrence**, scan entry, server receipt or a later backfill? Which field is authoritative for process ordering?
13. What is the timezone format (IANA zone, fixed offset, facility-local time, UTC)? How should daylight-saving ambiguities and cross-border movements be resolved?
14. How are tied timestamps, offline uploads, delayed scans, clock skew, corrections and retracted events documented?
15. Is a native immutable **event ID** available? What is the safe rule for detecting accidental system duplicate ingestion?
16. Which repeated code sequences represent **real repeated handling/re-sorting/rework** and must be retained? Can duplicate source IDs or transaction metadata distinguish them from accidents?
17. Are there expected event-order constraints and documented exceptions (e.g., departure after arrival) suitable for audit checks?

## D. Milestones, outcomes, exceptions and recovery
18. Which planned and actual milestones are available? How are their names, versions, planned times and subsequent revisions represented?
19. What is the authorized **pilot-process service deadline** at each prediction stage (P1 origin processing; P2 line-haul departure; P3 destination entry)? Are extensions/waivers recorded with effective times?
20. What codes mean a **nonterminal exception**, terminal exception, missed connection, cancellation, diversion, return, reassignment and resumption/recovery?
21. Which **terminal outcome** feed is authoritative and when does it become reliable? How should conflicting statuses/late outcomes be reconciled?
22. When a shipment incurs an exception but meets its terminal deadline, may it be classified as **recovered exception** as defined by the proposal? Which event(s) verify recovery?
23. Are returns and diversions always failures? (Proposed answer: **no**; interpretation depends on commitment and final outcome.) Can statuses distinguish commercial return from operational inability to complete?
24. What is the **case maturity rule** for assessing an outcome at extraction date, and how long can late scans/outcomes arrive? Are incomplete cases flagged as right-censored?
25. Can we obtain an approved normative **SOP, milestone rule or expected event/route sequence** with a version and effective period? If not, should behavioural reference analysis be described only as an observed comparison, never SOP compliance?

## E. Access, reporting and downstream research
26. Which requested columns are actually held, with which completeness, granularity and temporal history? Are route/facility and movement fields classified as confidential?
27. May approved analysts inspect source scans and mapping metadata only within an institutional/private environment? What are the allowed tools, logging, retention and export restrictions?
28. What internal aggregated results may be circulated? Which external figures, models, maps, code mappings or findings require separate publication authorization?
29. Are sample volumes and positive outcome prevalence likely to permit separate development and future temporal holdouts? Can failure and recovery cases be characterized without exposing identities?
30. What operational action and alert-review capacity might eventually be evaluated, and who is authorized to approve it? (For later stages; not a checkpoint commitment.)

## Requested output from authorized domain review
A versioned, access-controlled **raw-code → canonical-activity mapping** with ambiguous-code notes; a start/terminal rule sheet; exception/recovery and service-deadline definitions; a multi-piece case-unit decision; timezone/duplication policy; a normative-reference status; and the responsible approving owner. All remain **pending** until supplied through the Centre.

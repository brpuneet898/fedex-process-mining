# FedEx Process Mining Extension — Data-Readiness & Authorization Matrix
**Version:** 0.1 | **Status:** Prepared for internal professor/Centre review; no FedEx operational data examined | **Checkpoint:** requested 16 October 2026 (if feasible; submission timing to be confirmed)

## Purpose and scope
This is a *pre-access readiness assessment*, not evidence of an authorized data transfer or a Month-2 Go decision. The proposed pilot is **one selected origin hub → one principal line-haul corridor/movement → one selected destination hub**. Specific locations, route IDs, periods, field names and ownership are **not yet confirmed**. The individual pseudonymous shipment is the proposed case unit, subject to confirmation of multi-piece treatment. Keep this FedEx extension separate from the independent Transportation Science research track.

## Decision/authorization matrix
Legend: **Direction approved** = professor reports project direction approved; **Pending verification** = no documentary confirmation available to this checkpoint; **Not authorized** = cannot proceed with that activity on current evidence. No entry here should be treated as an attestation from FedEx or the Centre.

| Gate | Current state/evidence | Needed confirmation or record | Responsible route | Constraint / next step |
|---|---|---|---|---|
| Research direction | **Direction approved**, per professor's email; preparatory work only | Record kickoff direction and internal sign-off | Professor / Centre | Prepare plans only |
| Formal extension period / order | **Pending verification** | Executed order/extension, effective start/end, administrative scope | Centre via professor | Do not infer project Month 1 from calendar date |
| Budget activation | **Pending verification** | Funding approval and activation terms, if applicable | Centre via professor | No spending or resource commitments assumed |
| Pilot corridor | **Pending selection** | Approved origin hub, one connecting corridor, destination hub; authorized descriptive identifiers | FedEx data owner through Centre | Do not place sensitive facility/route details in public repo |
| Data owner and liaison | **Pending verification** | Named accountable data steward and contact protocol | Centre / FedEx-designated owner | No independent request or commitment to FedEx |
| Data-access authorization | **Not authorized on present evidence** | Written purpose-specific approval listing approved recipients/activities | FedEx / Centre | No collection, download, transfer, or analysis of operational logs |
| Confidentiality / agreement | **Pending verification** | NDA/DUA, commercial sensitivity classification, data minimization, retention/deletion terms | Centre / FedEx legal/governance | Pseudonymization is insufficient for publication permission |
| Approved compute and storage | **Pending verification** | Institutional/private secure environment, access control, logging, backup, transfer mechanism | Centre IT / data owner | Public GitHub is not an approved operational-data store |
| Identity and access restrictions | **Pending verification** | Least-privilege roles, allowed users, restrictions on contractors/cloud/AI services | Data owner / Centre IT | Keep protected records out of unapproved tools |
| Reporting to professor/Centre | **Pending permitted-output rules** | Internal distribution, aggregation, suppression/redaction restrictions | Centre / FedEx | This document contains preparatory specifications only |
| Publication / external dissemination | **Pending separate permission** | Explicit written external reporting/publication approval | FedEx / Centre | Do not publish logs, mappings, SOPs, facility details or findings |
| Approved SOP/reference | **Pending availability and authorization** | Versioned SOP, expected scan route/milestone rules, or agreed behavioural reference | FedEx operations via Centre | No claim of normative conformance without authorized reference |
| Process boundary / outcomes | **Proposed only** | Authoritative start/terminal markers, deadline semantics, recovered/returned/diverted/cancelled treatment | FedEx domain owner via Centre | Freeze only after review |
| Observation coverage | **Unknown** | Available extract period, actual event/case counts, service/facility coverage | Data owner via Centre | Six months and ~50,000 are preferences, not established facts |

## Data-request checklist — for Centre coordination, not a data request to FedEx
- [ ] Written approval for **one origin hub, one associated line-haul corridor and one destination hub**, including what route/facility descriptors may be shared.
- [ ] Requested **time coverage**: availability of consecutive historical months, extraction/as-of time and updates/late-arriving events; six consecutive months *preferred*.
- [ ] Permission for **event-level fields**: stable pseudonymous shipment/case key, event/scan ID (if any), raw code, event occurrence time and timezone, location/facility, corridor/movement link, exception/recovery markers, raw ordering/source provenance.
- [ ] Permission for **shipment/conditional fields**: planned/actual milestones and times, applicable service/process deadline, terminal status and authoritative outcome indicator, service class and route information where allowed; distinguish actually available from requested.
- [ ] Versioned **scan-code glossary** and operational interpretation including start, terminal, exception, recovery, repeat/duplicate behaviour and timestamp source semantics.
- [ ] **Responsible data owner/steward**, approved secure storage/compute location, approved transfer procedure, user list and role-based access limits.
- [ ] Data classification, minimization, retention/deletion rules, audit-logging and breach/escalation contacts.
- [ ] Written **internal reporting** rules and separately documented **external publication** rules, including aggregates and figures.
- [ ] Clarify handling of multi-piece consignments, split events, diversions/returns, cancelled line-haul movements, missing/late scans, deadline revisions and right-censoring.
- [ ] Confirm whether the sample may include sufficient normal, failed, recovered and incomplete cases for stage-wise and temporal validation without presuming any counts.

## Decision requested from professor/Centre
Confirm the outstanding authorization owner, secure collaboration environment, permissible data-request scope and whether these preparatory documents may be shared beyond the internal project team. **Current gate status: PREPARATORY WORK ONLY; operational-data access not established.**

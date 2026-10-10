Goal - Assess data feasibility, finalize the proposed shipment event-log schema, and establish an initial process-discovery and conformance-analysis baseline.

Proposed Activities - 
- Finalize one origin hub → line-haul corridor → destination hub. Confirm data availability, access permissions, shipment-level tracking, and operational process boundaries.
- Prepare a standardized shipment event-log schema, with one record per operational event and one de-identified shipment ID per case. Define canonical activity names and map available FedEx scan codes.
- Examine the available sample for missing values, duplicate scans, inconsistent timestamps, incomplete shipment histories, and outcome reliability. Assess progress toward the preferred dataset of 50,000+ shipments spanning at least six consecutive months.
- Using Python and PM4Py, construct an initial Directly-Follows Graph (DFG), discover a process model using Inductive Miner, and identify common shipment variants, dwell-time bottlenecks, and repeated handling. Conduct preliminary conformance checking against an approved reference process, if available.
- Consolidate feasibility findings, event-code mappings, data-quality results, and initial process-discovery outputs. Freeze the agreed schema and provisional analytical definitions, while documenting unresolved issues for the Month-2 feasibility gate.

Minimum Required Event-Log Fields - shipment_id (De-identified unique shipment identifier), activity / event_code (Operational scan or activity), timestamp (Event occurrence time), facitlity_id (Hub or operational location), planned_milestone / planned_time (Expected process stage and timing), actual_milestone (Recorded actual process stage), service_deadline (Committed completion deadline), exception_code (Exception or disruption classification), movement_route_id (Associated line-haul movement, where available), and outcome (Success, recovered, failure, diversion, return, cancellation or incomplete).

Expected Deliverables - 
- Dataset coverage, completeness, quality issues, and initial assessment against feasibility thresholds. - Data Feasibility Report
- Standardized fields, event dictionary, operational boundaries, and documented mapping rules. - Shipment Event-Log Schema v1.0
- Initial DFG, Inductive Miner model, frequent process variants, bottleneck statistics, and preliminary conformance findings where a suitable reference exists. - Process-Mining Baseline v0.1
- Outstanding data gaps, required FedEx clarifications, and tasks for completing the formal feasibility gate. - Month-2 Action Plan

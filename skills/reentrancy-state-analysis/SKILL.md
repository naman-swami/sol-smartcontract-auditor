---
name: reentrancy-state-analysis
description: "Detecting cross-contract and read-only reentrancy vectors where external calls precede state modifications."
version: "0.1.0"
---

# reentrancy-state-analysis

## Objective
Detecting cross-contract and read-only reentrancy vectors where external calls precede state modifications.

## Implementation Procedure
1. Parse incoming parameters and check domain preconditions.
2. Apply validated transformation pipelines and mathematical heuristics.
3. Formulate structured output objects containing confidence metrics and audit traces.

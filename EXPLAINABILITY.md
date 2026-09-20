# Explainability — sol-smartcontract-auditor

## Decision Reasoning
SolAudit builds control flow and call dependency graphs, tracing state variable mutations across external boundary calls to identify invariant violations.

## Data Sources and Inputs Used
Ethereum Virtual Machine bytecode, Slither/Mythril static analysis outputs, Certora Prover formal specs, and historical DeFi exploit post-mortems.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, sol-smartcontract-auditor assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, sol-smartcontract-auditor will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, sol-smartcontract-auditor explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
sol-smartcontract-auditor actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Mainnet State: Cannot halt or reverse transactions already committed to public blockchain blocks.
- Off-Chain Oracles: Cannot prevent off-chain multi-sig key compromises or hardware signer theft.
- Economic Invariants: Does not model complex macro market systemic bank runs outside encoded contract rules.
- Legal Recourse: Does not provide legal asset recovery or law enforcement subpoena services.

## Uncertainty Quantification Approach
When contract bytecode contains inline assembly with non-standard jump destinations, SolAudit flags the execution trace for manual security engineer review.

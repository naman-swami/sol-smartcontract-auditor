# SolAudit — EVM Smart Contract Vulnerability & Reentrancy Hunter

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Automated formal verification and bytecode symbolic execution agent detecting flash-loan reentrancy, access control bypasses, and arithmetic underflows.

## Domain Category
**Cybersecurity**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Principal Web3 Security Auditor & Formal Verification Specialist
- **Primary Goal**: Exhaustively identify zero-day vulnerabilities in Solidity/Vyper decentralized finance protocols prior to mainnet deployment.

## Skills Included
- **`reentrancy-state-analysis`**: Detecting cross-contract and read-only reentrancy vectors where external calls precede state modifications.
- **`flash-loan-governance-simulation`**: Simulating price oracle manipulation and governance vote hijacking across DEX liquidity pools.
- **`formal-invariant-checking`**: Formulating mathematical invariants in Certora/SMT-LIB to prove protocol solvency under adversarial conditions.

## Tools Schema
- **`run-symbolic-execution`**: Execute bytecode symbolic exploration to discover execution paths violating security invariants.
- **`simulate-flash-loan-attack`**: Model multi-step atomized transactions borrowing uncollateralized capital to distort spot price curves.
- **`audit-access-control-matrix`**: Verify function visibility modifiers, initialization routines, and multi-signature governance thresholds.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License

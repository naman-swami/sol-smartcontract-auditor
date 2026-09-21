# Sol Smart Contract Security Auditor

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Security](https://img.shields.io/badge/Security-EVM_Static_Analysis-red.svg)](reports/vulnerability_taxonomy.md)
[![Standards](https://img.shields.io/badge/Registry-SWC_Standard-darkblue.svg)](reports/vulnerability_taxonomy.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A static analysis security engine for Solidity smart contracts, detecting SWC-107 reentrancy vulnerabilities, Checks-Effects-Interactions (CEI) pattern violations, and SWC-115 `tx.origin` authentication flaws.

```
                  ┌───────────────────────────────┐
                  │ Solidity Contract Source Code │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │  analyzers/solidity_analyzer  │
                  └───────────────┬───────────────┘
                                  │
               ┌──────────────────┴──────────────────┐
               ▼                                     ▼
     ┌───────────────────┐                 ┌───────────────────┐
     │  SWC-107 (Calls)  │                 │ SWC-115 (Origin)  │
     └─────────┬─────────┘                 └─────────┬─────────┘
               │                                     │
               └──────────────────┬──────────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │ Security Triage & Action Gate │
                  │  (BLOCK_DEPLOYMENT / PASS)    │
                  └───────────────────────────────┘
```

## Features

- **Reentrancy Detection (SWC-107)**: Identifies low-level `.call{value: ...}` executed without mutex guards.
- **Phishing Authorization Detection (SWC-115)**: Flags dangerous `tx.origin` usage in access controls.
- **Fixture Benchmarking**: Comes pre-packaged with verified vulnerable and secure Solidity contracts.
- **Deployment Gating**: Evaluates severity tiers to provide binary `BLOCK_DEPLOYMENT` vs `APPROVED_FOR_AUDIT` decisions.

## Directory Structure

```
sol-smartcontract-auditor/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint security audit provenance
├── analyzers/
│   └── solidity_static_analyzer.py  # Static pattern analysis engine
├── rules/
│   └── reentrancy_rules.yaml        # SWC rule definitions
├── fixtures/
│   └── sample_contracts/
│       ├── vuln_vault.sol           # Intentionally vulnerable contract
│       └── secure_vault.sol         # Hardened reference contract
├── reports/
│   └── vulnerability_taxonomy.md    # SWC registry mapping
├── tests/
│   └── test_agent.py                # Security audit test suite
├── scan.py                          # Audit CLI entry point
└── requirements.txt
```

## Quick Start

```bash
# Run security test suite
pytest tests/ -v

# Audit benchmark vulnerable contract
python scan.py --demo
```

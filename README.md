# Sol Smart Contract Security Auditor

> **Automated Solidity Static Analysis & Formal Verification Engine**  
> Detecting SWC-107 Reentrancy, Checks-Effects-Interactions (CEI) Violations, and Privilege Escalation Vectors.

---

### Vulnerability Detection Taxonomy

```
Solidity Source AST
       │
       ▼
┌───────────────────────────────────────────────┐
│       sol_smartcontract_auditor Engine        │
│  (slither.config.json & rules/reentrancy_rules)│
└──────┬────────────────┬───────────────┬───────┘
       │                │               │
       ▼                ▼               ▼
 [SWC-107 Check]   [SWC-115 Check] [SWC-104 Check]
  Reentrancy Call   tx.origin Auth  Unchecked Call
  External State    Phishing Risk   Silent Revert
```

| SWC ID | Vulnerability Class | Detection Pattern | Target Impact |
| :--- | :--- | :--- | :--- |
| **SWC-107** | Reentrancy | External `.call{value: ...}("")` invoked prior to internal storage state decrement | Critical (Drain of funds) |
| **SWC-115** | Authorization through `tx.origin` | Use of `tx.origin == owner` rather than `msg.sender` | High (Phishing / Proxy bypass) |
| **SWC-104** | Unchecked Call Return Value | Low-level address calls without boolean success verification | Medium (State desynchronization) |

---

### Static Analysis Sample Output

Auditing vulnerable test fixture `fixtures/sample_contracts/vuln_vault.sol`:

```solidity
// Vulnerability in vuln_vault.sol (Lines 14-17)
(bool sent, ) = msg.sender.call{value: bal}(""); // External call BEFORE state mutation!
require(sent, "Failed to send Ether");
balances[msg.sender] = 0;                        // State mutation happens too late!
```

**Auditor Detection Finding:**
```console
[HIGH RISK DETECTED] SWC-107: State variable 'balances[msg.sender]' updated after external call.
Recommendation: Enforce Checks-Effects-Interactions pattern or utilize OpenZeppelin ReentrancyGuard.
```

---

### Security Tooling & Audit CLI

```bash
# Scan default benchmark test contracts
python scan.py --demo

# Run rule validation unit tests
pytest tests/ -v
```

Rules are declaratively defined in `rules/reentrancy_rules.yaml`. Compiler settings, Slither AST passes, and gas optimizations are managed in [slither.config.json](slither.config.json).

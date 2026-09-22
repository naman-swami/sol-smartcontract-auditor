# Smart Contract Security Audit Standards & Formal Verification

## 1. Audit Methodology & Standards
This security suite implements automated static analysis, control-flow graph (CFG) inspection, and abstract syntax tree (AST) traversal in accordance with:
- **ConsenSys Smart Contract Best Practices**
- **Smart Contract Weakness Classification (SWC Registry)**
- **Ethereum Improvement Proposals (EIPs)**: ERC-20, ERC-721, ERC-1155, and ERC-4626 Tokenized Vaults.

---

## 2. Vulnerability Detection Taxonomy

### A. Reentrancy & Checks-Effects-Interactions (SWC-107)
Reentrancy occurs when an external contract call transfers execution control back to the calling contract before state variables are decremented.
- **Pattern Monitored**: External calls via low-level `.call{value: ...}("")`, `.send()`, or `.transfer()` occurring prior to internal balance updates.
- **Remediation Standard**:
  1. Enforce the **Checks-Effects-Interactions (CEI)** pattern: update internal state variables before executing external calls.
  2. Implement OpenZeppelin's non-reentrant state locks (`ReentrancyGuard` or transient storage `tstore`/`tload` under EIP-1153).

### B. Insecure Authorization via `tx.origin` (SWC-115)
- **Vulnerability**: Using `require(tx.origin == owner)` for access control enables phishing attacks via malicious intermediary contracts.
- **Remediation Standard**: Strictly authenticate using `msg.sender` or cryptographic signature verification (`ECDSA.recover`).

### C. Unchecked Call Return Values (SWC-104)
- **Vulnerability**: Low-level Solidity calls (`address.call(...)`) do not revert on failure but return a boolean flag. Ignoring this return value causes silent failure.
- **Remediation Standard**: Always verify `require(success, "Call failed")` or utilize OpenZeppelin `Address.sendValue()`.

### D. Flash Loan Governance & Price Oracle Manipulation
- **Vulnerability**: Relying on spot reserves from automated market makers (Uniswap v2 `getReserves`) allows flash-loan-funded spot price manipulation.
- **Remediation Standard**: Utilize Chainlink decentralized oracle feeds with staleness checks or cumulative Time-Weighted Average Prices (TWAP) with minimum observation windows $\ge 30$ minutes.

---

## 3. Slither Static Analysis Integration
The configuration file [slither.config.json](slither.config.json) specifies detector targets, compiler optimization flags, and severity filters:
```json
{
  "detectors_to_run": "reentrancy-eth,reentrancy-no-eth,tx-origin,unchecked-lowlevel,uninitialized-state",
  "solc_args": "--optimize --optimize-runs 200",
  "filter_paths": "node_modules|tests",
  "legacy_ast": false
}
```

---

## 4. Verification Workflow
All smart contracts must achieve zero critical or high-severity findings prior to testnet deployment:
```bash
# Scan test contracts for CEI and reentrancy violations
python scan.py --demo

# Run rule validation suite
pytest tests/ -v
```

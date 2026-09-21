"""
Solidity Static Analysis Engine
Scans smart contract source code for SWC vulnerability patterns and CEI violations.
"""
import re
from typing import List, Dict, Any

class SoliditySecurityAnalyzer:
    def __init__(self, rules: List[Dict[str, Any]] = None):
        self.rules = rules or []

    def audit_contract_text(self, source_code: str) -> Dict[str, Any]:
        lines = source_code.splitlines()
        findings = []
        has_reentrancy_guard = "nonReentrant" in source_code or "ReentrancyGuard" in source_code

        for idx, line in enumerate(lines, 1):
            clean_line = line.strip()
            if clean_line.startswith("//") or clean_line.startswith("/*"):
                continue

            # SWC-107: Reentrancy check
            if ".call{value:" in line:
                if not has_reentrancy_guard:
                    findings.append({
                        "rule_id": "SWC-107",
                        "line": idx,
                        "severity": "CRITICAL",
                        "title": "Unprotected External Call (Reentrancy Risk)",
                        "snippet": clean_line,
                        "recommendation": "Use ReentrancyGuard and ensure balances are decremented before external call."
                    })

            # SWC-115: tx.origin authorization
            if "tx.origin" in line and ("require(" in line or "if (" in line):
                findings.append({
                    "rule_id": "SWC-115",
                    "line": idx,
                    "severity": "HIGH",
                    "title": "Phishing-vulnerable Authorization via tx.origin",
                    "snippet": clean_line,
                    "recommendation": "Use msg.sender instead of tx.origin for caller verification."
                })

            # SWC-120: Weak Randomness
            if "block.timestamp" in line and ("%" in line or "random" in clean_line.lower()):
                findings.append({
                    "rule_id": "SWC-120",
                    "line": idx,
                    "severity": "MEDIUM",
                    "title": "Weak Pseudo-Randomness from Block Timestamp",
                    "snippet": clean_line,
                    "recommendation": "Utilize Chainlink VRF for cryptographic randomness."
                })

        critical_count = sum(1 for f in findings if f["severity"] == "CRITICAL")
        high_count = sum(1 for f in findings if f["severity"] == "HIGH")

        risk_tier = "CRITICAL" if critical_count > 0 else "HIGH" if high_count > 0 else "CLEAN"
        deployment_gate = "BLOCK_DEPLOYMENT" if findings else "APPROVED_FOR_AUDIT"

        return {
            "total_issues": len(findings),
            "critical_count": critical_count,
            "high_count": high_count,
            "risk_tier": risk_tier,
            "deployment_gate": deployment_gate,
            "findings": findings
        }

    def audit_file(self, filepath: str) -> Dict[str, Any]:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()
        res = self.audit_contract_text(code)
        res["filepath"] = filepath
        return res

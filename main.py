import argparse
import json
import os
from analyzers.solidity_static_analyzer import SoliditySecurityAnalyzer

def main():
    parser = argparse.ArgumentParser(description="Solidity Smart Contract Security Auditor")
    parser.add_argument("--demo", action="store_true", help="Audit sample contracts")
    parser.add_argument("--contract", type=str, help="Path to .sol file to audit")
    args = parser.parse_args()

    analyzer = SoliditySecurityAnalyzer()
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures", "sample_contracts")

    if args.demo:
        print("=== SOL SMART CONTRACT SECURITY AUDIT REPORT ===\n")
        for contract in ["vuln_vault.sol", "secure_vault.sol"]:
            path = os.path.join(fixtures_dir, contract)
            if os.path.exists(path):
                res = analyzer.audit_file(path)
                print(f"File: {contract}")
                print(f"Risk Tier: {res['risk_tier']} | Deployment Gate: {res['deployment_gate']}")
                print(f"Critical Issues: {res['critical_count']} | High Issues: {res['high_count']}")
                for f in res["findings"]:
                    print(f"  [Line {f['line']}] {f['rule_id']} ({f['severity']}): {f['title']}")
                    print(f"    Snippet: {f['snippet']}")
                    print(f"    Fix: {f['recommendation']}")
                print("-" * 50)
    elif args.contract:
        res = analyzer.audit_file(args.contract)
        print(json.dumps(res, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

import json
import argparse
from src.contract_audit_engine import SmartContractAuditorEngine

def main():
    parser = argparse.ArgumentParser(description="SolAudit Smart Contract Security CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated Solidity vulnerability audit")
    args = parser.parse_args()

    engine = SmartContractAuditorEngine()
    sample_contract = """
contract VulnerableBank {
    mapping(address => uint256) public balances;
    function withdraw() public {
        uint256 amount = balances[msg.sender];
        (bool success, ) = msg.sender.call{value: amount}("");
        balances[msg.sender] = 0;
    }
}
"""
    report = engine.audit_solidity_code(sample_contract)
    print("="*60)
    print(" SOLAUDIT EVM SMART CONTRACT SECURITY AUDIT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()

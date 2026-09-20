import pytest
from src.contract_audit_engine import SmartContractAuditorEngine

def test_reentrancy_detection():
    engine = SmartContractAuditorEngine()
    code = """
function withdraw(uint amount) external {
    (bool ok, ) = msg.sender.call{value: amount}("");
    balances[msg.sender] -= amount;
}
"""
    res = engine.audit_solidity_code(code)
    assert res["security_tier"] == "CRITICAL"
    assert any(f["type"] == "REENTRANCY_RISK" for f in res["findings"])

def test_safe_contract():
    engine = SmartContractAuditorEngine()
    code = """
function safeWithdraw(uint amount) external nonReentrant {
    balances[msg.sender] -= amount;
    (bool ok, ) = msg.sender.call{value: amount}("");
}
"""
    res = engine.audit_solidity_code(code)
    assert res["security_tier"] == "CLEAN"

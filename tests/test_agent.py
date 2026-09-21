import os
import pytest
from analyzers.solidity_static_analyzer import SoliditySecurityAnalyzer

@pytest.fixture
def analyzer():
    return SoliditySecurityAnalyzer()

def test_vulnerable_contract_detection(analyzer):
    fixtures_dir = os.path.join(os.path.dirname(__file__), "..", "fixtures", "sample_contracts")
    vuln_path = os.path.join(fixtures_dir, "vuln_vault.sol")
    res = analyzer.audit_file(vuln_path)
    
    assert res["risk_tier"] == "CRITICAL"
    assert res["deployment_gate"] == "BLOCK_DEPLOYMENT"
    assert res["critical_count"] >= 1
    
    rule_ids = [f["rule_id"] for f in res["findings"]]
    assert "SWC-107" in rule_ids
    assert "SWC-115" in rule_ids

def test_secure_contract_approval(analyzer):
    fixtures_dir = os.path.join(os.path.dirname(__file__), "..", "fixtures", "sample_contracts")
    sec_path = os.path.join(fixtures_dir, "secure_vault.sol")
    res = analyzer.audit_file(sec_path)
    
    assert res["risk_tier"] == "CLEAN"
    assert res["deployment_gate"] == "APPROVED_FOR_AUDIT"
    assert res["total_issues"] == 0

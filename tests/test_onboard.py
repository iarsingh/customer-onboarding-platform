from fastapi.testclient import TestClient

from onboard.main import app

client = TestClient(app)


def test_missing_audit_blocks_and_a_full_set_is_still_not_live():
    blocked = client.post("/onboarding", json={"customer": "Northwind", "gates": {"sso": True, "backup": True, "network_policy": True}}).json()
    assert blocked["status"] == "blocked"
    assert blocked["missing"] == ["audit"]
    assert blocked["live"] is False
    ready = client.post("/onboarding", json={"customer": "Northwind", "gates": {"sso": True, "backup": True, "network_policy": True, "audit": True}}).json()
    assert ready["status"] == "ready_for_human"
    assert ready["live"] is False

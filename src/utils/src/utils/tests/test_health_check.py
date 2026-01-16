Python
from src.utils.health_check import get_health_status


def test_health_check_returns_status():
    result = get_health_status()
    assert isinstance(result, dict)
    assert "status" in result
    assert result["status"] == "OK"


def test_health_check_has_uptime():
    result = get_health_status()
    assert "uptime_seconds" in result
    assert float(result["uptime_seconds"]) >= 0.0
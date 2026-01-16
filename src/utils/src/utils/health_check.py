Python
"""
Health check utility for OpenMind OM1.

Provides runtime health status for agents, including uptime, core modules,
and basic diagnostics. Can be used in simulation or live robot deployments.
"""

import time
from typing import Dict

# Track process start time
_START_TIME = time.time()


def get_health_status() -> Dict[str, str]:
    """
    Returns basic runtime health information for OM1.

    Returns:
        Dict[str, str]: Health status data including:
            - status: "OK" if running
            - uptime_seconds: seconds since process start
            - runtime: "OM1"
            - mode: "development"
    """
     uptime = time.time() - _START_TIME

    return {
        "status": "OK",
        "uptime_seconds": f"{uptime:.2f}",
        "runtime": "OM1",
        "mode": "development",
    }

if name == "main":
    # Quick test for developers
    status = get_health_status()
    print("[OM1 HEALTH CHECK]")
    for key, value in status.items():
        print(f"{key}: {value}")

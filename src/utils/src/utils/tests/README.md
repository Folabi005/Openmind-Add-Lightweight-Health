Markdown
## Health Check Utility

OM1 includes a lightweight health check utility for validating runtime status
during development, simulation, or robot deployment.

### Example

`python
from src.utils.health_check import get_health_status

status = get_health_status()
print(status)
Example Output
Copy code
Json
{
  "status": "OK",
  "uptime_seconds": "12.34",
  "runtime": "OM1",
  "mode": "development"
}
This utility can be extended to include module availability, sensor status, or node-level diagnostics.
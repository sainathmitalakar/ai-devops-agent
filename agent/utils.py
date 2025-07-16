def get_logs(query: str) -> str:
    return "2025-07-16 ERROR: Pod crashloop detected in namespace 'prod'."

def analyze_health(_: str) -> str:
    return "All services are healthy except `auth-service`, which is in Degraded state."
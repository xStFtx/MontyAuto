from prometheus_client import start_http_server, Counter, Gauge
import time

REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')
ERRORS = Counter('http_errors_total', 'Total HTTP Errors')
LATENCY = Gauge('http_request_latency_seconds', 'HTTP Request Latency')

class Monitor:
    def __init__(self):
        start_http_server(8001)
    
    @staticmethod
    def track_latency(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            LATENCY.set(time.time() - start_time)
            return result
        return wrapper 
import requests


class APIClient:
    def __init__(self, timeout=10):
        self.timeout = timeout

    def post(self, url, payload):
        try:
            return requests.post(url, json=payload, timeout=self.timeout).json()
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}

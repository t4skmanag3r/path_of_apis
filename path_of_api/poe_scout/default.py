from dataclasses import dataclass

import requests


@dataclass
class LiveResponse:
    status: str
    service: str

@dataclass
class ReadyResponse:
    status: str
    service: str
    checks: dict

class Default:
    def __init__(self, base_url: str, sub_url: str = "/health", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout
                 
    def check_live(self) -> LiveResponse:
        endpoint = "/live"
        try:
            resp = requests.get(self.base_url + self.sub_url + endpoint, timeout=self.timeout)
            return LiveResponse(**resp.json())
        except requests.exceptions.RequestException as e:
            raise e
        
    
    def check_ready(self) -> ReadyResponse:
        endpoint = "/ready"
        try:
            resp = requests.get(self.base_url + self.sub_url + endpoint, timeout=self.timeout)
            return ReadyResponse(**resp.json())
        except requests.exceptions.RequestException as e:
            raise e
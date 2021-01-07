import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def test_intent_route(self):
        self.client.get("/api/intent/sentence=hello world")
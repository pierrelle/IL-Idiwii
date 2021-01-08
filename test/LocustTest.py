import time
import logging

from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def test_intent_route(self):
        response = self.client.get("/api/intent?sentence=test")
        logging.info(f"Response status code: {response.status_code}")
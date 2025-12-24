from locust import HttpUser, task, between

class WeatherUser(HttpUser):
    # Wait between 1 and 3 seconds between searches (realistic behavior)
    wait_time = between(1, 3)

    @task
    def get_weather(self):
        self.client.get("/weather/Jaipur")
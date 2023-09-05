import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(URL)
        return response.content

    def load_json(self):
        people_list = []
        peoples = json.loads(self.get_response_body())
        for people in peoples:
            people_list.append(people)

        return people_list

        
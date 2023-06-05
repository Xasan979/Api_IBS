import requests
import json

from urls import API_URL


class MainPageApi:
    def __init__(self, request):
        self.request = request

    def open(self):
        self.request.get(API_URL)

    def get_request(self, get_url):
        response_api = requests.get(f'{API_URL}{get_url}')
        json_response = json.dumps(response_api.json(), indent=4)
        print(response_api, json_response)
        return response_api, json_response

    def post_request(self, post_url, data_json):
        response_api = requests.post(f"{API_URL}{post_url}", json=data_json)
        json_response = json.dumps(response_api.json(), indent=4)
        print(response_api, json_response)
        return response_api, json_response

    def put_request(self, put_url, data_json):
        response_api = requests.put(f"{API_URL}{put_url}", json=data_json)
        json_response = json.dumps(response_api.json(), indent=4)
        print(response_api, json_response)
        return response_api, json_response

    def patch_request(self, patch_url, data_json):
        response_api = requests.patch(f"{API_URL}{patch_url}", json=data_json)
        json_response = json.dumps(response_api.json(), indent=4)
        print(response_api, json_response)
        return response_api, json_response

    def delete_request(self, delete_url):
        response_api = requests.delete(f'{API_URL}{delete_url}')
        print(response_api)
        return response_api

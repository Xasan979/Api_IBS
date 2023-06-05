import allure
import pytest

from api.pages.main_page_api import MainPageApi
from api.tests.data_json import *


@allure.epic("TestApi")
class TestApi:

    @staticmethod
    @allure.description("Checking api get valid")
    @pytest.mark.parametrize('get_url', GET_URL_VALID)
    def test_api_requests_get_valid(request, get_url):
        response_api, json_response_api = MainPageApi.get_request(request, get_url)
        assert response_api.status_code == 200

    @staticmethod
    @allure.description("Checking api get invalid")
    @pytest.mark.parametrize('get_url', GET_URL_INVALID)
    def test_api_requests_get_invalid(request, get_url):
        response_api, json_response_api = MainPageApi.get_request(request, get_url)
        assert response_api.status_code == 404

    @staticmethod
    @allure.description("Checking api post valid")
    @pytest.mark.parametrize('post_url, data_json', POST_URL_VALID)
    def test_api_requests_post_valid(request, post_url, data_json):
        response_api, json_response_api = MainPageApi.post_request(request, post_url, data_json)
        assert response_api.raise_for_status

    @staticmethod
    @allure.description("Checking api post invalid")
    @pytest.mark.parametrize('post_url, data_json', POST_URL_INVALID)
    def test_api_requests_post_invalid(request, post_url, data_json):
        response_api, json_response_api = MainPageApi.post_request(request, post_url, data_json)
        assert response_api.status_code == 400

    @staticmethod
    @allure.description("Checking api put valid")
    @pytest.mark.parametrize('put_url, data_json', PUT_URL_VALID)
    def test_api_requests_put_valid(request, put_url, data_json):
        response_api, json_response_api = MainPageApi.put_request(request, put_url, data_json)
        assert response_api.raise_for_status

    @staticmethod
    @allure.description("Checking api put invalid")
    @pytest.mark.parametrize('put_url, data_json', PUT_URL_INVALID)
    def test_api_requests_put_invalid(request, put_url, data_json):
        pass  # Требуется доработать
        # response_api, json_response_api = MainPageApi.put_request(request, put_url, data_json)
        # assert response_api.status_code == 404

    @staticmethod
    @allure.description("Checking api patch valid")
    @pytest.mark.parametrize('patch_url, data_json', PATCH_URL_VALID)
    def test_api_requests_patch_valid(request, patch_url, data_json):
        response_api, json_response_api = MainPageApi.patch_request(request, patch_url, data_json)
        assert response_api.status_code == 200

    @staticmethod
    @allure.description("Checking api patch invalid")
    @pytest.mark.parametrize('patch_url, data_json', PATCH_URL_INVALID)
    def test_api_requests_patch_invalid(request, patch_url, data_json):
        pass  # Требуется доработать
        # response_api, json_response_api = MainPageApi.patch_request(request, patch_url, data_json)
        # assert response_api.status_code == 404

    @staticmethod
    @allure.description("Checking api delete valid")
    @pytest.mark.parametrize('delete_url', DELETE_URL_VALID)
    def test_api_requests_delete_valid(request, delete_url):
        response_api = MainPageApi.delete_request(request, delete_url)
        assert response_api.status_code == 204

    @staticmethod
    @allure.description("Checking api delete invalid")
    @pytest.mark.parametrize('delete_url', DELETE_URL_INVALID)
    def test_api_requests_delete_invalid(request, delete_url):
        pass  # Требуется доработать
        # response_api = MainPageApi.delete_request(request,delete_url)
        # assert response_api.status_code == 404

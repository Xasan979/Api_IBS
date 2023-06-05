import json
import allure
import pytest
import requests

from selenium import webdriver
from api.pages.main_page_api import MainPageApi
from api.tests.data_json import *
from web.pages.main_page import MainPage
from web.tests.XPath import *
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service('path/to/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@allure.epic("TestWeb")
class TestWeb:

    @staticmethod
    @allure.description("Checking web get valid")
    @pytest.mark.parametrize("button_xpath, element_xpath, get_url",
                             zip(get_xpath_valid, get_xpath_valid_element, GET_URL_VALID))
    def test_web_comparison_api_request_get_valid(main_page, button_xpath, element_xpath, get_url):
        main_page.open()
        response_web, json_response_web = main_page.click_submit_button_get(button_xpath, element_xpath)
        # API
        api = MainPageApi(requests)
        response_api, json_response_api = api.get_request(get_url)
        json_response_api = response_api.json()
        # Проверяем соответствие результатов
        assert response_web.status_code == 200
        assert response_web.status_code == response_api.status_code
        assert json_response_web == json.dumps(json_response_api, indent=4), " WEB совпадает API запросу"

    @staticmethod
    @allure.description("Checking web get invalid")
    @pytest.mark.parametrize("button_xpath, element_xpath, get_url",
                             zip(get_xpath_invalid, get_xpath_invalid_element, GET_URL_INVALID))
    def test_web_comparison_api_request_get_invalid(main_page, button_xpath, element_xpath, get_url):
        main_page.open()
        response_web, json_response_web = main_page.click_submit_button_get(button_xpath, element_xpath)
        api = MainPageApi(requests)
        response_api, json_response_api = api.get_request(get_url)
        json_response_api = response_api.json()
        assert response_web.status_code == 404
        assert response_web.status_code == response_api.status_code
        assert json_response_web == json.dumps(json_response_api, indent=4), " WEB совпадает API запросу"

    @staticmethod
    @allure.description("Checking web post valid")
    @pytest.mark.parametrize("button_xpath, element_xpath, datas_json, post_url",
                             zip(post_xpath_valid, post_xpath_valid_element, post_data_valid, POST_URL_VALID))
    def test_web_comparison_api_request_post_valid(main_page, button_xpath, element_xpath, datas_json, post_url):
        main_page.open()
        response_web, json_response_web = main_page.click_submit_button_post(button_xpath, element_xpath, datas_json)
        json_response_web = json.loads(json_response_web)
        api = MainPageApi(requests)
        response_api, json_response_api = api.post_request(*post_url)
        json_response_api = response_api.json()
        assert response_api.raise_for_status
        assert response_web.status_code == response_api.status_code
        assert len(json_response_web.keys()) == len(json_response_api.keys())

    @staticmethod
    @allure.description("Checking web post invalid")
    @pytest.mark.parametrize("button_xpath, element_xpath, datas_json, post_url",
                             zip(post_xpath_invalid, post_xpath_invalid_element, post_data_invalid, POST_URL_INVALID))
    def test_web_comparison_api_request_post_invalid(main_page, button_xpath, element_xpath, datas_json, post_url):
        main_page.open()
        response_web, json_response_web = main_page.click_submit_button_post(button_xpath, element_xpath, datas_json)
        json_response_web = json.loads(json_response_web)
        api = MainPageApi(requests)
        response_api, json_response_api = api.post_request(*post_url)
        json_response_api = response_api.json()
        assert response_web.status_code == 400
        assert response_web.status_code == response_api.status_code
        assert json_response_web["error"] == json_response_api["error"]

    @staticmethod
    @allure.description("Checking web put valid")
    @pytest.mark.parametrize('button_xpath,element_xpath, datas_json ,put_url',
                             zip(put_xpath_valid, put_xpath_valid_element, put_data_valid, PUT_URL_VALID))
    def test_web_comparison_api_request_put_valid(main_page, button_xpath, element_xpath, datas_json, put_url):
        main_page.open()
        response_web, json_response_web = main_page.click_submit_button_put(button_xpath, element_xpath, datas_json)
        json_response_web = json.loads(json_response_web)
        api = MainPageApi(requests)
        response_api, json_response_api = api.put_request(*put_url)
        json_response_api = response_api.json()
        assert response_web.status_code == 200
        assert response_web.status_code == response_api.status_code
        assert json_response_web["name"] == json_response_api["name"]
        assert json_response_web["job"] == json_response_api["job"]

    @staticmethod
    @allure.description("Checking web put invalid")
    @pytest.mark.parametrize('button_xpath,element_xpath, datas_json ,put_url',
                             zip(put_xpath_valid, put_xpath_valid_element, put_data_valid, PUT_URL_INVALID))
    def test_web_comparison_api_request_put_invalid(main_page, button_xpath, element_xpath, datas_json, put_url):
        pass  # Требуется доработать
        # main_page.open()
        # response_web, json_response_web = main_page.click_submit_button_put(button_xpath, element_xpath, datas_json)
        # api = MainPageApi(requests)
        # response_api, json_response_api = api.put_request(*put_url)
        # json_response_api = response_api.json()
        # json_response_web = json.loads(json_response_web)
        # assert response_web.status_code == 400
        # assert response_web.status_code == response_api.status_code
        # assert json_response_web["error"] == json_response_api["error"]

    @staticmethod
    @allure.description("Checking web patch valid")
    @pytest.mark.parametrize('button_xpath,element_xpath,datas_json,patch_url',
                             zip(patch_xpath_valid, patch_xpath_valid_element, patch_data_valid, PATCH_URL_VALID))
    def test_web_comparison_api_request_patch_valid(main_page, button_xpath, element_xpath, datas_json, patch_url):
        main_page.open()
        response_web, json_response_web = main_page.click_submit_button_patch(button_xpath, element_xpath, datas_json)
        json_response_web = json.loads(json_response_web)
        api = MainPageApi(requests)
        response_api, json_response_api = api.patch_request(*patch_url)
        json_response_api = response_api.json()
        assert response_web.status_code == 200
        assert response_web.status_code == response_api.status_code
        assert json_response_web["name"] == json_response_api["name"]
        assert json_response_web["job"] == json_response_api["job"]

    @staticmethod
    @allure.description("Checking web patch invalid")
    @pytest.mark.parametrize('button_xpath,element_xpath,datas_json,patch_url',
                             zip(patch_xpath_invalid, patch_xpath_invalid_element, patch_data_invalid,
                                 PATCH_URL_INVALID))
    def test_web_comparison_api_request_patch_invalid(main_page, button_xpath, element_xpath, datas_json, patch_url):
        pass  # Требуется доработать
        # main_page.open()
        # response_web, json_response_web = main_page.click_submit_button_patch(button_xpath, element_xpath, datas_json)
        # json_response_web = json.loads(json_response_web)
        # api = MainPageApi(requests)
        # response_api, json_response_api = api.patch_request(*patch_url)
        # json_response_api = response_api.json()
        # assert response_web.status_code == 400
        # assert response_web.status_code == response_api.status_code
        # assert json_response_web["error"] == json_response_api["error"]

    @staticmethod
    @allure.description("Checking web delete valid")
    @pytest.mark.parametrize('button_xpath,element_xpath ,delete_url',
                             zip(delete_xpath_valid, delete_xpath_valid_element, DELETE_URL_VALID))
    def test_api_requests_delete_valid(main_page, button_xpath, element_xpath, delete_url):
        main_page.open()
        response_web = main_page.click_submit_button_delete(button_xpath, element_xpath)
        api = MainPageApi(requests)
        response_api = api.delete_request(delete_url)
        assert response_api.status_code == 204
        assert response_web.status_code == response_api.status_code

    @staticmethod
    @allure.description("Checking web delete invalid")
    @pytest.mark.parametrize('button_xpath,element_xpath ,delete_url',
                             zip(delete_xpath_invalid, delete_xpath_invalid_element, DELETE_URL_INVALID))
    def test_api_requests_delete_invalid(main_page, button_xpath, element_xpath, delete_url):
        pass  # Требуется доработать
        # main_page.open()
        # response_web = main_page.click_submit_button_delete(button_xpath, element_xpath)
        # api = MainPageApi(requests)
        # response_api = api.delete_request(delete_url)
        # assert response_api.status_code == 204
        # assert response_web.status_code == response_api.status_code

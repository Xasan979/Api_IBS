import json
import requests

from selenium.webdriver.common.by import By
from urls import API_URL


class MainPage:
    def __init__(self, driver):
        # Класс принимает аргумент driver в конструкторе и сохраняет его в атрибут self.driver
        self.driver = driver

    def open(self):
        # Метод open принимает аргумент url и использует driver для открытия указанного URL.
        self.driver.get(API_URL)

    def click_submit_button_get(self, button_xpath, element_xpath):
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
        element = self.driver.find_element(By.XPATH, element_xpath)
        url = element.get_attribute('href')
        response_web = requests.get(url)
        json_response_web = json.dumps(response_web.json(), indent=4)
        print(response_web, json_response_web)
        return response_web, json_response_web

    def click_submit_button_post(self, button_xpath, element_xpath, data_json):
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
        element = self.driver.find_element(By.XPATH, element_xpath)
        url = element.get_attribute('href')
        response_web = requests.post(url, json=data_json)
        json_response_web = json.dumps(response_web.json(), indent=4)
        print(response_web, json_response_web)
        return response_web, response_web.text

    def click_submit_button_put(self, button_xpath, element_xpath, data_json):
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
        element = self.driver.find_element(By.XPATH, element_xpath)
        url = element.get_attribute('href')
        response_web = requests.put(url, json=data_json)
        json_response_web = json.dumps(response_web.json(), indent=4)
        print(response_web, json_response_web)
        return response_web, json_response_web

    def click_submit_button_patch(self, button_xpath, element_xpath, data_json):
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
        element = self.driver.find_element(By.XPATH, element_xpath)
        url = element.get_attribute('href')
        response_web = requests.patch(url, json=data_json)
        json_response_web = json.dumps(response_web.json(), indent=4)
        print(response_web, json_response_web)
        return response_web, json_response_web

    def click_submit_button_delete(self, button_xpath, element_xpath):
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
        element = self.driver.find_element(By.XPATH, element_xpath)
        url = element.get_attribute('href')
        response_web = requests.delete(url)
        print(response_web)
        return response_web



import time
import pytest

from utilities.readProperties import ReadConfig
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


baseURL = ReadConfig.getApplicationURL()


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(4)

    request.cls.driver = driver
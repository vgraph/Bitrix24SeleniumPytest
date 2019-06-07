import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from passwords import passwords

@pytest.fixture(scope="class")
def driver(request):
    # wd = webdriver.Chrome()
    wd = webdriver.Firefox()
    wd.implicitly_wait(5)
    # wd.wait = WebDriverWait(wd, 10)
    request.addfinalizer(wd.quit)
    return wd


class TestCriticalPath:

    def test_login(self, driver):
        password = passwords.Passwords.password
        email = passwords.Passwords.email
        driver.get("https://auth2.bitrix24.net/?user_lang=ru")
        driver.find_element_by_css_selector('input#login').send_keys(email)
        driver.find_element_by_css_selector('button .ui-btn-success').click()
        driver.find_element_by_css_selector('input#password').send_keys(password)
        driver.find_element_by_css_selector('input#remember').click()
        driver.find_element_by_css_selector('button.ui-btn-success').click()


from selenium.webdriver import Chrome
import time
import pytest


@pytest.mark.smoke
def test_launchBrowser_Selenium_Url():
    driver = Chrome(executable_path="C:\\ParamPersonal\\PYTHON\\Driver\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.seleniumeasy.com/test/")
    time.sleep(1)
    print(driver.title)
    driver.quit()


@pytest.mark.sanity
def launchBrowser_Google_Url():
    driver = Chrome(executable_path="C:\\ParamPersonal\\PYTHON\\Driver\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com/")
    time.sleep(1)
    print(driver.title)
    driver.quit()


@pytest.mark.skip
def test_launchBrowser_Amazon_Url():
    driver = Chrome(executable_path="C:\\ParamPersonal\\PYTHON\\Driver\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.amazon.in/")
    # time.sleep(1)
    print(driver.title)
    driver.quit()


@pytest.mark.smoke
def test_launchBrowser_ReqRes_Url():
    driver = Chrome(executable_path="C:\\ParamPersonal\\PYTHON\\Driver\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://reqres.in/")
    # time.sleep(1)
    print(driver.title)
    driver.quit()

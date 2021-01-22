from selenium.webdriver import Chrome
import time
import pytest


@pytest.fixture(scope="class")
def generalMethod(request):
    global driver
    driver = Chrome(executable_path="C:\\ParamPersonal\\PYTHON\\Driver\\chromedriver_win32\\chromedriver.exe")
    yield
    driver.quit()

@pytest.mark.usefixtures("generalMethod")
class Testexample:
    def test_launchBrowser_Toi_Url(self):
        driver.get("https://timesofindia.indiatimes.com/")
        # time.sleep(1)
        print(driver.title)


    def test_launchBrowser_Udemy_Url(self):
        driver.get("https://www.udemy.com/")
        # time.sleep(1)
        print(driver.title)

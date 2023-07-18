import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope='join us')
def driver():
    driver =webdriver.Chrome()
    yield driver
    driver .quit()
#driver = Chrome()
def test_valid_from_submission(driver):
    driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
    driver.maximize_window()
    driver.find_element("xpath","//input[@name ='name']").send_keys("kalirajan")
    driver.find_element("xpath","//input[@name ='email']").send_keys("kalirajan4@gmail.com")
    driver.find_element("xpath","//input[@name ='phone']").send_keys(1234567890)
    driver.find_element("id","inputFile").send_keys("E:\py- part -1.pdf")
    driver.find_element("xpath","//textarea[@name='description']").send_keys("description entered by script")
    driver.find_element("xpath","//button[text()='APPLY NOW']").click()
    success_message = WebDriverwait(driver,10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"success_message")))
    assert success_message.text =="Applicaton submitted successfully"

def test_invalid_from_submission(driver):
    driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
    driver.maximize_window()
    driver.find_element("xpath", "//button[text()='APPLY NOW']").click()
    error_message = WebDriverWait(driver,10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME," error_message")))
    assert error_message.text == "Please fill in all required fields"




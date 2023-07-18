#from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

#driver = Chrome()
class Test1_(unittest.TestCase):
    def toVerifylogo():
        #self.driver = webdriver.Chrome(executable_path="E://chromedriver.exe")
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver,20)
        driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
        driver.maximize_window()
        element=wait.until(EC.element_to_be_clickable((By.ID,"logo")))
        element.click()
        #wait.until(EC.url_to_be("https://www.hashtag-ca.com/"))
        #assert "https://www.hashtag-ca.com/" == driver.current_url
        assertEqual("https://www.hashtag-ca.com/",driver.current_url,"URl is not matching")
        driver.close()
if __name__=="__main__":
    unittest.main()


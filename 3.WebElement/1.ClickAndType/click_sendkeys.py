from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



class OrangeHRM():
    def test_valid_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Elements
        username = driver.find_element(By.XPATH, "//input[@id='txtUsername']")
        password = driver.find_element(By.CSS_SELECTOR, "#txtPassword")
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        time.sleep(10)

        driver.close()


    def test_invalid_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Elements
        username = driver.find_element(By.XPATH, "//input[@id='txtUsername']")
        password = driver.find_element(By.CSS_SELECTOR, "#txtPassword")
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin123')

        password.clear()
        password.send_keys('admin123abc')

        login_btn.click()

        time.sleep(10)

        driver.close()


test_obj = OrangeHRM()
test_obj.test_valid_login()
test_obj.test_invalid_login()
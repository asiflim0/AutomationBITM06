from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class OrangeHRM():
    def login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")

        username = driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("asif@demo.com")
        if username  == 'none':
            print("We found username by XPATH")
        else:
            print("We don't found username by XPATH")
        #time.sleep(5)

        password = driver.find_element(By.CSS_SELECTOR, "#txtPassword")
        if password != None:
            print("We found password by CSS")
        else:
            print("We don't found password by CSS")
        #time.sleep(5)

        driver.close()


test_obj = OrangeHRM()
test_obj.login()
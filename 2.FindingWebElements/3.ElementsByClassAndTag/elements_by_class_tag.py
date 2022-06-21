from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class OrangeHRM():
    def login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        email = driver.find_element(By.CLASS_NAME, 'email-login-box').send_keys("asif@sct.com")
        if email is not None:
            print("We found username by Class")
        else:
            print("We don't found username by Class")
        time.sleep(5)

        password = driver.find_element(By.NAME, "txtPassword")
        if password is not None:
            print("We found password by NAME")
        else:
            print("We don't found password by NAME")

        driver.close()


test_obj = OrangeHRM()
test_obj.login()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class OrangeHRM():
    def login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")

        forgot_password = driver.find_element(By.LINK_TEXT, "¿Olvidó su contraseña?").send_keys("asif@demo.com")
        if forgot_password  != 'none':
            print("We found forgot password by link Text")
        else:
            print("We don't found forgot password by link Text")
        #time.sleep(5)

        driver.close()


test_obj = OrangeHRM()
test_obj.login()
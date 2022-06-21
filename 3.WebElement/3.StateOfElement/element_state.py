from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Element():
    def enable(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        base_url = "http://localhost:3000/files/battlefield/react/react-hotel-reservation-system"
        driver.get(base_url)
        time.sleep(5)

        save_and_continue_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save and continue']")

        actual_state = save_and_continue_btn.is_enabled()
        print(actual_state)

        expected_state = False

        if expected_state == actual_state:
            print("Element Disabled, Test Passed")
        else:
            print("Element enabled, Test Failed")

        driver.close()

test_obj = Element()
test_obj.enable()

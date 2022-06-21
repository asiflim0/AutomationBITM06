from selenium import webdriver


class Chrome():
    def launch(self):
        driver = webdriver.Chrome(executable_path="C:\Demo Project\AutomationBITM06\Drivers\chromedriver_102.0.exe")
        driver.get("http://localhost:3000/files/battlefield/react/react-hotel-reservation-system")
        driver.close()

chrome_obj= Chrome()
chrome_obj.launch()
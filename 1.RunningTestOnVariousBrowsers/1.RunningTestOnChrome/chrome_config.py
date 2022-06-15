from selenium import webdriver

class Test_Chrome():
    def launch_chrome(self):
        driver = webdriver.Chrome(executable_path="C:\Demo Project\AutomationBITM06\Drivers\chromedriver_102.0.exe")

chrome_obj= Test_Chrome()
chrome_obj.launch_chrome()
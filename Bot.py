from selenium import webdriver
import time
class GetIn:
    def __init__(self,name,pwd):
        self.driver =webdriver.Firefox()
        self.username=name
        self.password=pwd
    def closeBrowser(self):
        self.driver.close()

    def login(self):
        drive=self.driver
        drive.get("https://www.indiamart.com/")
        time.sleep(3)
        sign_button = drive.find_element_by_xpath("//*[@id='nav-signin-tooltip']")
        sign_button.click()
        time.sleep(3)
        user_name=drive.find_element_by_xpath("//*[@id='ap_email']")
        user_name.clear()
        user_name.send_keys(self.username)
        time.sleep(1)
        continue_button=drive.find_element_by_xpath("//*[@id='continue']")
        continue_button.click()
        password=drive.find_element_by_xpath("//*[@id='ap_password']")
        password.clear()
        password.send_keys(self.password)
        login_button=drive.find_element_by_xpath("//*[@id='signInSubmit']")
        login_button.click()
        drive.find_elements_by_class_name('galery-')

GetIn("username","password").login()


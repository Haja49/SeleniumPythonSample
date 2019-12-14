'''
Created on 14-Dec-2019

@author: HAJA
'''
class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
        
    def enter_Username(self, uName):
        self.driver.find_element_by_id('username').send_keys(uName)
        
    def enter_Password(self, pwd):
        self.driver.find_element_by_id('password').send_keys(pwd)
        
    def click_login(self):
        self.driver.find_element_by_class_name('decorativeSubmit').click()
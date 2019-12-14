'''
Created on 14-Dec-2019

@author: HAJA
'''
from selenium import webdriver
import unittest
from page.LoginPage import LoginPage


class Login(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('F:\Photon\workspace\Python\drivers\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    
    def test_login(self):
        self.driver.get('http://leaftaps.com/opentaps/control/main')
        lp = LoginPage(self.driver)
        lp.enter_Username('DemoSalesManager')
        lp.enter_Password('crmsfa')
        lp.click_login()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

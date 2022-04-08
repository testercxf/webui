from selenium.webdriver.common.action_chains import  ActionChains
import unittest
from time  import  sleep
class  Mylogin():

    def __init__(self,driver):
        self.driver=driver

    def  login(self):
        self.driver.find_element_by_xpath("/html/body/div[4]/div/img[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div/div/div/div[2]/a[2]/span").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@placeholder='请输入手机号/邮箱']").send_keys("17666888991")
        sleep(1)
        self.driver.find_element_by_xpath("//*[@placeholder='请输入密码']").send_keys("123456")
        self.driver.find_element_by_xpath("//body/div[3]/div/div/div[1]/div[3]/button").click()
        sleep(2)

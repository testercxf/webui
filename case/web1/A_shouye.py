from selenium import  webdriver
from public.log_in import Mylogs
import unittest
import time
import os


class Testshouye(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://39.106.51.187:8080/index.html#/login?redirect=%2F404")
        self.driver.maximize_window()
        time.sleep(2)
        print("start：" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        file_1 = "D:/test/"
        # if not os.path.exists(file_1):
        #     os.makedirs(os.path.join("D:/","wukongCRM/"))
        print("end：" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        src_1 = file_1+ time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))+ ".png"
        self.driver.get_screenshot_as_file(src_1)
        time.sleep(3)
        self.driver.quit()


    def  testShouye1(self):
        '''检查客户管理首页显示'''
        Mylogs(self.driver).logs()
        time.sleep(6)
        self.driver.find_element_by_xpath("//*[@id='app']/section/header/div/div/div/a[2]/div").click()
        time.sleep(6)
        leftText = self.driver.find_element_by_xpath("//div[@class='user-name']")
        rightText = self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/button/span")
        time.sleep(6)
        self.assertNotEqual(leftText.text,"日志")
        self.assertEqual(rightText.text,"数据查重")




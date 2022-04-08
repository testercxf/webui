from selenium import  webdriver
from public.log_in import Mylogs
from public.Enter_the_clue import Theclue
import unittest
import time
import os


class Testclue(unittest.TestCase):

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



    def  testXsuo1_1(self):
        """检查线索页面显示"""
        Mylogs(self.driver).logs()          #登录
        #点击客户管理菜单
        self.driver.find_element_by_xpath("//*[@id='app']/section/header/div/div/div/a[2]/div").click()
        time.sleep(6)
        #点击线索菜单
        self.driver.find_element_by_xpath("//*[@id='app']/section/section/aside/div/ul/a[3]/li/span").click()
        time.sleep(2)
        xsText = self.driver.find_element_by_xpath("//div[@class='c-container']/div[1]")
        self.assertEqual("线索管理",xsText.text)



    def testXsuo1_2(self):
        """新建线索"""
        Mylogs(self.driver).logs()
        time.sleep(6)
        Theclue(self.driver).Enterclue()
        time.sleep(3)
        #点击新建线索
        self.driver.find_element_by_xpath("//*[@class='right-container']/button/span").click()
        time.sleep(2)
        #在线索名称输入线索自动化2
        self.driver.find_element_by_xpath(
            "//*[@class='crm-create-body']/form/div[1]/div[1]/div[1]/input").send_keys("线索自动化2")
        time.sleep(2)
        #点击线索来源
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div/div/input").click()
        time.sleep(2)
        #选择下拉框中的第一条“促销”
        self.driver.find_element_by_xpath("//*[@x-placement='bottom-start']/div[1]/div[1]/ul/li[1]/span").click()
        time.sleep(2)
        #点击保存
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[3]/button[2]/span").click()
        time.sleep(2)
        Theclue(self.driver).Search_for_clues("线索自动化2")
        time.sleep(2)
        #断言:是否新建成功
        xj = self.driver.find_element_by_xpath("//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[2]/div")
        self.assertEqual("线索自动化2",xj.text)



    def testXsuo1_3(self):
        '''新建已存在的线索'''
        Mylogs(self.driver).logs()                              #登录
        Theclue(self.driver).Enterclue()                        #进入线索
        Theclue(self.driver).New_clue("线索自动化2")            #新建已存在的线索名称
        #点击保存
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[3]/button[2]/span").click()
        time.sleep(2)
        # 断言:能否新建已存在的线索
        clue = self.driver.find_element_by_xpath("//*[@class='el-message__content']")
        self.assertEqual("线索名称已存在",clue.text)



    def testXsuo1_4(self):
        '''检查线索详情页显示'''
        Mylogs(self.driver).logs()                              #登录
        Theclue(self.driver).Enterclue()                        #进入线索
        Theclue(self.driver).Search_for_clues("线索自动化2")    #搜索“线索自动化2”
        #点击线索名称
        self.driver.find_element_by_xpath(
            "//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[2]/div").click()
        time.sleep(2)
        #断言:线索详情显示
        xq = self.driver.find_element_by_xpath("//*[@id='slide']/div/div/div[1]/div[1]/div[1]")
        self.assertEqual("线索自动化2",xq.text)



    def testXsuo1_5(self):
        '''检查线索编辑按钮能否跳转'''
        Mylogs(self.driver).logs()                               #登录
        Theclue(self.driver).Enterclue()                         #进入线索
        Theclue(self.driver).Search_for_clues("线索自动化2")     #搜索新建的线索
        #点击线索名称进入详情
        self.driver.find_element_by_xpath("//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[2]/div").click()
        time.sleep(2)
        #点击编辑按钮
        self.driver.find_element_by_xpath(
            "//*[@id='slide']/div/div/div[1]/div[1]/button[2]/span").click()
        time.sleep(2)
        #断言:是否能进入线索编辑页
        xs = self.driver.find_element_by_xpath("//*[text()='编辑线索']")
        self.assertEqual("编辑线索",xs.text)



    def testXsuo1_6(self):
        '''删除新建的线索'''
        Mylogs(self.driver).logs()                           #登录
        Theclue(self.driver).Enterclue()                     #进入线索
        Theclue(self.driver).Search_for_clues("线索自动化2") #搜索新建的线索
        #选中线索
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span").click()
        time.sleep(2)
        # 断言选中线索后，该控件处是否有“删除”两字
        toptext = self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div/div[2]/div[2]/div[4]/div")
        self.assertEqual(toptext.text, "删除")
        time.sleep(1)
        #点击删除的按钮
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[2]/div/div[2]/div[2]/div[4]/div").click()
        time.sleep(2)
        # 断言点击删除后，是否弹出二次确认框
        tishitext =self.driver.find_element_by_xpath("//*[@class='el-message-box']/div/div/span")
        self.assertEqual("提示",tishitext.text)
        time.sleep(1)
        #点击二次确认框中的确定按钮
        self.driver.find_element_by_xpath("//*[@class='el-message-box']/div[3]/button[2]/span").click()
        time.sleep(3)
        #定位搜索框,并清空输入框内容
        self.driver.find_element_by_xpath("//*[@style='height: 100%;']/div/div[1]/div[2]/input").clear()
        time.sleep(2)
        Theclue(self.driver).Search_for_clues("线索自动化2")
        time.sleep(3)
        #断言是否删除成功
        sc = self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div[3]/div/span[1]")
        self.assertEqual("共 0 条",sc.text)



    def  testXsuo1_7(self):
        '''检查线索翻页能否成功'''
        Mylogs(self.driver).logs()              #登录
        Theclue(self.driver).Enterclue()        #进入线索页
        #向后翻一页
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[2]/div[3]/div/button[2]/i").click()
        time.sleep(2)
        #断言:是否翻页成功
        translate = self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div[3]/div/span[3]/div/input")
        self.assertNotEqual("1",translate.text)



    def testXsuo1_8(self):
        '''选中一条线索转化为客户'''
        Mylogs(self.driver).logs()          #登录
        Theclue(self.driver).Enterclue()    #进入线索页
        # 搜索新建的线索
        self.driver.find_element_by_xpath("//*[@style='height: 100%;']/div/div[1]/div[2]/input").send_keys("线索自动化3")
        self.driver.find_element_by_xpath("//*[@style='height: 100%;']/div/div[1]/div[2]/div/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[2]/span").click()
        time.sleep(3)
        text_1 = self.driver.find_element_by_xpath("/html/body/div[3]/p")
        self.assertEqual("转化成功",text_1.text)
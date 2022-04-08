import time

class  Thecontacts():
    def  __init__(self,driver):
        self.driver = driver

    def Enter_contacts(self):
        time.sleep(3)
        # 进入客户管理界面
        self.driver.find_element_by_xpath("//*[@id='app']/section/header/div/div/div/a[2]/div").click()
        time.sleep(8)
        # 点击联系人
        self.driver.find_element_by_xpath("//*[@id='app']/section/section/aside/div/ul/a[5]/li/span").click()
        time.sleep(6)


    def Search_for_contacts(self,lianxiss):
        #搜索框
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/div[2]/input").send_keys(lianxiss)
        time.sleep(2)
        #点击搜索按钮
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/div[2]/div/button").click()
        time.sleep(2)
import time

class  Theclue():
    def  __init__(self,driver):
        self.driver = driver

    def  Enterclue(self):
        time.sleep(3)
        # 点击客户管理菜单
        self.driver.find_element_by_xpath("//*[@id='app']/section/header/div/div/div/a[2]/div").click()
        time.sleep(8)
        # 点击线索菜单
        self.driver.find_element_by_xpath("//*[@id='app']/section/section/aside/div/ul/a[3]/li/span").click()
        time.sleep(6)

    def  New_clue(self,xjxiansuo):
        time.sleep(3)
        #新建线索
        self.driver.find_element_by_xpath("//*[@class='right-container']/button/span").click()
        time.sleep(3)
        #输入已存在的线索名称
        self.driver.find_element_by_xpath("//*[@class='crm-create-body']/form/div[1]/div[1]/div[1]/input").send_keys(xjxiansuo)

    def  Search_for_clues(self,sousuo):
        time.sleep(3)
        #搜索新建的线索
        self.driver.find_element_by_xpath("//*[@style='height: 100%;']/div/div[1]/div[2]/input").send_keys(sousuo)
        time.sleep(2)
        #点击搜索按钮
        self.driver.find_element_by_xpath("//*[@style='height: 100%;']/div/div[1]/div[2]/div/button").click()
        time.sleep(6)



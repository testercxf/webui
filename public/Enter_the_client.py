import  time

class  Theclient():
    def  __init__(self,driver):
        self.driver = driver

    def Enterclient(self):
        time.sleep(3)
        # 点击客户管理菜单
        self.driver.find_element_by_xpath("//*[@id='app']/section/header/div/div/div/a[2]/div").click()
        time.sleep(8)
        #点击客户
        self.driver.find_element_by_xpath("//*[@id='app']/section/section/aside/div/ul/a[4]/li/span").click()
        time.sleep(8)

    def New_custome(self):
        # 点击新建客户按钮
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/div[3]/button/span").click()
        time.sleep(3)
        # 点击later正向按钮
        self.driver.switch_to.alert.accept()
        time.sleep(3)


    def Search_the_customer(self,kehusousuo):
        time.sleep(2)
        #搜索客户
        self.driver.find_element_by_xpath(
            "//*[@id='app']/section/section/main/div/div/div[1]/div[2]/input").send_keys(kehusousuo)
        time.sleep(3)
        #点击搜索按钮
        self.driver.find_element_by_xpath(
            "//*[@id='app']/section/section/main/div/div/div[1]/div[2]/div/button").click()
        time.sleep(3)

    def Enter_the_details(self,genjin):
        time.sleep(3)
        # 点击客户名称进入详情后输入跟进记录
        self.driver.find_element_by_xpath(
            "//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[3]/div").click()
        time.sleep(3)
        #输入数据
        self.driver.find_element_by_xpath("//*[@class='i-cont']/div/textarea").send_keys(genjin)
        #点击发布
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "//*[@class='el-card__body']/div/div[3]/div/div[1]/div[2]/button/span").click()


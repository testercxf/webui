from  selenium import  webdriver
from  public.log_in import Mylogs
from  public.Enter_the_contacts import Thecontacts
from  selenium.webdriver.common.keys import Keys
import  time,os
import  unittest


class  Testclient(unittest.TestCase):

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



    def testLxi1_1(self):
        '''查看联系人界面显示'''
        Mylogs(self.driver).logs()                      #登录
        Thecontacts(self.driver).Enter_contacts()        #进入联系人界面
        #断言是否成功进入联系人界面
        lianxi = self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/div[1]")
        self.assertEqual("联系人管理",lianxi.text)



    def testLxi1_2(self):
        '''新建联系人'''
        Mylogs(self.driver).logs()                     #登录
        Thecontacts(self.driver).Enter_contacts()       #进入联系人界面
        #点击新建联系人
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/div[3]/button/span").click()
        time.sleep(2)
        #断言是否已进入新建联系人界面
        lianxi = self.driver.find_element_by_xpath("//*[@class='el-card__body']/div/div[1]/div")
        self.assertEqual("新建联系人",lianxi.text)
        #在联系人名称栏输入李四1
        lianxi_name = self.driver.find_element_by_xpath("//*[@class='crm-create-flex']/div/div[2]/div/div/form/div[1]/div/div[1]/input")
        lianxi_name.send_keys("董小姐")
        self.driver.find_element_by_xpath("//*[@class='el-card__body']/div/div[2]/div/div[2]/div/div/form/div[2]/div/span/div/div").click()
        time.sleep(2)
        #勾选客户
        self.driver.find_element_by_xpath("//*[@class='cr-body-content']/div[2]/div[3]/table/tbody/tr[1]/td/div/label/span[1]/span").click()
        #点击确定
        self.driver.find_element_by_xpath("//*[@class='cr-contianer']/div[3]/button[2]/span").click()
        time.sleep(2)
        #点击保存
        self.driver.find_element_by_xpath("//*[@class='el-card__body']/div/div[3]/button[2]/span").click()
        time.sleep(2)
        #搜索董小姐
        Thecontacts(self.driver).Search_for_contacts("董小姐")
        #断言:新建联系人是否成功
        later = self.driver.find_element_by_xpath("//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[2]/div")
        self.assertEqual("董小姐",later.text)



    def testLxi1_3(self):
        '''删除联系人'''
        Mylogs(self.driver).logs()                              #登录
        Thecontacts(self.driver).Enter_contacts()               #进入联系人界面
        Thecontacts(self.driver).Search_for_contacts("董小姐")  #搜索
        #勾选联系人
        self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span").click()
        #点击删除
        self.driver.find_element_by_xpath("//*[@class='crm-container']/div[1]/div[2]/div[2]/div[3]/div").click()
        time.sleep(1)
        #点击二次确认框中的确认按钮
        self.driver.find_element_by_xpath("//*[@class='el-message-box']/div[3]/button[2]/span")
        time.sleep(2)
        Thecontacts(self.driver).Search_for_contacts("董小姐")
        time.sleep(2)
        #断言:是否已删除成功
        delete = self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div[3]/div/span[1]")
        self.assertEqual("共 0 条",delete.text)
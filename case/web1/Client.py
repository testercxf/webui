from  selenium import  webdriver
from  public.log_in import Mylogs
from  public.Enter_the_client import Theclient
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



    def testKhu1_1(self):
        '''检查客户界面显示'''
        Mylogs(self.driver).logs()                  #登录
        Theclient(self.driver).Enterclient()        #进入客户页面
        time.sleep(2)
        #断言:是否已进入客户界面
        client_text = self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/div[1]")
        self.assertEqual("客户管理",client_text.text)



    def testKhu1_2(self):
        '''检查新建客户界面显示'''
        Mylogs(self.driver).logs()                  #登录
        Theclient(self.driver).Enterclient()        #进入客户页面
        time.sleep(2)
        #点击新建客户按钮
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/div[3]/button/span").click()
        time.sleep(2)
        #点击later正向按钮
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # 断言:是否进入新建客户界面
        kehu_interface  = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/div")
        self.assertEqual("新建客户",kehu_interface.text)



    def testKhu1_3(self):
        '''新建客户'''
        Mylogs(self.driver).logs()                  #登录
        Theclient(self.driver).Enterclient()        #进入客户页面
        Theclient(self.driver).New_custome()        #进入新建客户按钮
        #输入客户名称
        kehu_name = self.driver.find_element_by_xpath(
            "//*[@class='el-card__body']/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input")
        kehu_name.send_keys("客户自动化2")
        time.sleep(2)
        #点击保存按钮
        self.driver.find_element_by_xpath("//*[@class='el-card__body']/div/div[3]/button[3]/span").click()
        time.sleep(6)
        Theclient(self.driver).Search_the_customer("客户自动化2")       #搜索
        time.sleep(2)
        # 断言:是否新建成功
        kehu = self.driver.find_element_by_xpath("//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[3]/div")
        self.assertEqual("客户自动化2",kehu.text)


    def  testKhu1_4(self):
        '''新建已存在的客户'''
        Mylogs(self.driver).logs()                  #登录
        Theclient(self.driver).Enterclient()        #进入客户页面
        Theclient(self.driver).New_custome()    #进入新建客户界面
        #输入已存在的客户名称
        kehu_name = self.driver.find_element_by_xpath(
            "//*[@class='el-card__body']/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input")
        kehu_name.send_keys("客户自动化2")
        time.sleep(2)
        # 点击保存按钮
        self.driver.find_element_by_xpath("//*[@class='el-card__body']/div/div[3]/button[3]/span").click()
        time.sleep(2)
        #断言:是否能新建已存在的客户
        kehu_name_rem = self.driver.find_element_by_xpath("//*[@class='content']/div/div/form/div[1]/div/div[2]")
        self.assertEqual("客户名称已存在",kehu_name_rem.text)



    def  testKhu1_5(self):
        '''检查搜索能否正常使用'''
        Mylogs(self.driver).logs()                                   #登录
        Theclient(self.driver).Enterclient()                         #进入客户页面
        Theclient(self.driver).Search_the_customer("客户自动化2")    #搜索客户
        time.sleep(2)
        # 断言:搜索客户后，能否过滤掉其他客户信息
        kehu_num = self.driver.find_element_by_xpath("//*[@class='el-pagination__total']")
        self.assertEqual("共 1 条",kehu_num.text)



    def testKhu1_6(self):
        '''检查单击客户进入详情页显示'''
        Mylogs(self.driver).logs()                     #登录
        Theclient(self.driver).Enterclient()           #进入客户页面
        Theclient(self.driver).Search_the_customer("客户自动化2")   #搜索客户
        time.sleep(2)
        #点击客户名称进入详情
        self.driver.find_element_by_xpath("//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[3]/div").click()
        time.sleep(2)
        #断言:详情页对应的信息是否对应点击的客户信息
        page = self.driver.find_element_by_xpath("//*[@class='t-name']")
        self.assertEqual("客户自动化2",page.text)



    def testKhu1_7(self):
        '''检查能否翻页'''
        Mylogs(self.driver).logs()              #登录
        Theclient(self.driver).Enterclient()    #进入客户页面
        #点击向后翻页
        self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div[3]/div/button[2]/i").click()
        #断言页数是否有变化
        time.sleep(2)
        page_num = self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div[3]/div/span[3]/div/input")
        self.assertNotEqual(" 1 ",page_num.text)



    def testKhu1_8(self):
        '''更改成交状态'''
        Mylogs(self.driver).logs()                      #登录
        Theclient(self.driver).Enterclient()            #进入客户界面
        Theclient(self.driver).Search_the_customer("客户自动化2")    #搜索名为“客户自动化2”的客户
        #勾选名为“客户自动化2”的客户
        self.driver.find_element_by_xpath(
            "//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[1]/div/label").click()
        #点击更改成交状态
        self.driver.find_element_by_xpath("//*[@class='crm-container']/div[1]/div[2]/div[2]/div[3]/div").click()
        #断言点击更改成交状态后的弹出框界面显示
        state = self.driver.find_element_by_xpath("//*[@aria-label='客户成交状态']/div[1]/span")
        time.sleep(2)
        self.assertEqual("客户成交状态",state.text)
        #点击更改状态
        self.driver.find_element_by_xpath("//*[@class='el-dialog__body']/div/div/div[2]/div/input").click()
        #点击保存
        self.driver.find_element_by_xpath("//*[@aria-label='客户成交状态']/div[3]/span/button[2]/span").click()
        time.sleep(2)
        # 断言:是否更改成交状态成功
        win = self.driver.find_element_by_xpath("//*[@id='crm-table']/div[3]/table/tbody/tr/td[12]/div")
        self.assertEqual("已成交",win.text)



    def testKhu1_9(self):
        '''在客户详情里新建联系人'''
        Mylogs(self.driver).logs()                                 #登录
        Theclient(self.driver).Enterclient()                       #进入客户页面
        Theclient(self.driver).Search_the_customer("客户自动化1")  #搜索“客户自动化1”
        #点击客户自动化1进入详情
        self.driver.find_element_by_xpath(
            "//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[3]/div").click()
        time.sleep(2)
        #点击联系人
        self.driver.find_element_by_xpath("//*[@id='tab-contacts']").click()
        #点击新建联系人
        self.driver.find_element_by_xpath("//*[@id='follow-log-content']/div/div/button/span").click()
        time.sleep(2)
        #断言是否进入新建联系人界面
        linkman = self.driver.find_element_by_xpath("//*[@class='c-view']/div/div[1]/div/div[1]/div")
        self.assertEqual("新建联系人",linkman.text)
        time.sleep(2)
        #在联系人姓名输入框输入“玫瑰”
        input_name = self.driver.find_element_by_xpath(
            "//*[@class='c-view']/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/input")
        input_name.send_keys("玫瑰")
        #点击保存
        self.driver.find_element_by_xpath("//*[@class='handle-bar']/button[2]/span").click()
        time.sleep(2)
        #断言新建联系人能否成功
        lx = self.driver.find_element_by_xpath("//*[@class='el-table__row']/td[1]/div[1]")
        self.assertEqual("玫瑰",lx.text)



    def testKhu2_1(self):
        '''将选中的客户放入公海'''
        Mylogs(self.driver).logs()                                   #登录
        Theclient(self.driver).Enterclient()                         #进入客户界面
        Theclient(self.driver).Search_the_customer("客户自动化1")    #搜索“客户自动化1”
        #勾选客户
        self.driver.find_element_by_xpath(
            "//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[1]/div/label").click()
        #点击放入公海
        self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div/div[2]/div[2]/div[4]/div").click()
        time.sleep(2)
        #断言:是否弹出转移到公海二次确认框
        hint = self.driver.find_element_by_xpath("//*[@class='el-message-box__content']/div[2]/p")
        self.assertEqual("确定转移到公海吗?",hint.text)
        #点击二次确认框的确定按钮
        self.driver.find_element_by_xpath("//*[@class='el-message-box__btns']/button[2]/span").click()
        time.sleep(2)
        Theclient(self.driver).Search_the_customer("客户自动化1")
        # 断言:转移到公海是否成功
        no = self.driver.find_element_by_xpath("//*[@class='el-table__empty-text']")
        self.assertEqual("暂无数据",no.text)



    def testKhu2_2(self):
        '''在客户详情里跟进记录'''
        Mylogs(self.driver).logs()                                       #登录
        Theclient(self.driver).Enterclient()                             #进入客户界面
        Theclient(self.driver).Search_the_customer("客户自动化2")        #搜索“客户自动化1”
        Theclient(self.driver).Enter_the_details("给长城贴瓷砖第一天")   #跟进记录输入数据
        time.sleep(2)
        #断言:能否正常发布跟进记录
        genjin = self.driver.find_element_by_xpath(
            "//*[@class='fl-b-content']")
        self.assertEqual("给长城贴瓷砖第一天",genjin.text)



    def testKhu2_3(self):
        '''查看我负责的客户'''
        Mylogs(self.driver).logs()                  #登录
        Theclient(self.driver).Enterclient()        #进入客户界面
        time.sleep(2)
        #定位场景并点击
        self.driver.find_element_by_xpath(
            "//*[@id='app']/section/section/main/div/div/div[2]/div[1]/div[1]/span/div/i").click()
        #点击我负责的客户
        self.driver.find_element_by_xpath("//*[@class='scene-container']/div[1]/div[2]").click()
        time.sleep(2)
        #断言:筛选后是否呈现我负责的客户
        cj = self.driver.find_element_by_xpath(
            "//*[@id='app']/section/section/main/div/div/div[2]/div[1]/div[1]/span/div/div")
        self.assertEqual("我负责的客户",cj.text)



    def testKhu2_4(self):
        '''删除客户'''
        Mylogs(self.driver).logs()                                 #登录
        Theclient(self.driver).Enterclient()                       #进入客户界面
        Theclient(self.driver).Search_the_customer("客户自动化2")  #搜索客户“客户自动化2”
        # 勾选名为“客户自动化2”的客户
        self.driver.find_element_by_xpath(
            "//*[@id='crm-table']/div[4]/div[2]/table/tbody/tr/td[1]/div/label").click()
        time.sleep(2)
        #点击删除
        self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div/div[2]/div[2]/div[5]/div").click()
        time.sleep(2)
        #断言是否弹出二次确认框
        delete = self.driver.find_element_by_xpath("//*[@class='el-message-box__content']/div[2]/p")
        self.assertEqual("确定要删除这些数据吗?",delete.text)
        time.sleep(2)
        #点击二次确认框中的删除
        self.driver.find_element_by_xpath("//*[@aria-label='提示']/div/div[3]/button[2]/span").click()
        time.sleep(3)
        #定位搜索框并清空内容
        self.driver.find_element_by_xpath(
            "//*[@id='app']/section/section/main/div/div/div[1]/div[2]/input").clear()
        time.sleep(6)
        Theclient(self.driver).Search_the_customer("客户自动化2")
        time.sleep(3)
        #断言:是否删除成功
        delete_1 = self.driver.find_element_by_xpath(
            "//*[@id='crm-main-container']/div/div/div[2]/div[3]/div/span[1]")
        self.assertEqual("共 0 条",delete_1.text)
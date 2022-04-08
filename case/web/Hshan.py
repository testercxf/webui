from selenium import  webdriver
from public.log_in_hs import Mylogin
import  unittest
import time


class  TestHs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sit1-sxs-web.mshare.cn/")
        self.driver.maximize_window()
        time.sleep(2)
        print("start：" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))


    def tearDown(self):
        file_1 = "D:/test/"
        # if not os.path.exists(file_1):
        #     os.makedirs(os.path.join("D:/","wukongCRM/"))
        print("end：" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        src_1 = file_1 + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(src_1)
        time.sleep(8)
        self.driver.quit()

    def  testSxs_01(self):
        '''投递京东校招岗位'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(7)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/img[1]").click()
        self.driver.find_element_by_xpath(
            "//*[@id='__layout']/div/div[2]/div[2]/div/div[2]/div[1]/form/input[2]").send_keys("京东")
        self.driver.find_element_by_xpath(
            "//*[@class='top-bar']/div/div[2]/div[1]/form/input[1]").click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.1)")
        #选择校招
        self.driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div[1]/div/div[1]/span[2]").click()
        print(self.driver.window_handles)  # 打印当前页面信息
        #进入第一个职位
        self.driver.find_element_by_xpath(
            "//*[@id='__layout']/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/p[1]/a").click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div[1]/div[1]/div[6]/div/div[3]").click()

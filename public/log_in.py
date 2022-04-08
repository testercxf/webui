import  time
class  Mylogs():

    def __init__(self,driver):
      self.driver = driver

    def logs(self):
        #输入用户名
        self.driver.find_element_by_name("username").send_keys("admin")
        #输入密码
        self.driver.find_element_by_name("password").send_keys("123456")
        #点击登录按钮
        self.driver.find_element_by_css_selector(".el-form-item__content>button").click()
        time.sleep(6)
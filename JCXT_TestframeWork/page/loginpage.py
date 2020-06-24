from selenium.webdriver.common.by import By #定位方式

#创建LoginPage类
class LoginPage(BasePage):
    username_loc = (By.XPATH, "//input[@id='txtUserID")
    password_loc = (By.XPATH, "//input[@id='txtPassword")
    loginInfo_loc = (By.XPATH, "//input[@id='txtVal")
    loginButton_loc = (By.XPATH, "//button[@id='loginBtn")


    #输入用户名
    def type_username(self.username_loc):
        self.find_element(*self.username_loc).send_keys("xht")
    #输入密码
    def type_password(self.password_loc):
        self.find_element(*self.password_loc).send_keys("xht631020")
    #输入验证码
    def type_longinInfo(self.lon)

    #点击登录
    def type_login(self):
        self.find_element(*self.login_loc).click()
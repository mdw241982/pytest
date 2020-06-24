class TestJCXT:
    def setUp(self):
        # 访问检测基础版v2.1
        self.webdriver = webdriver.chrome()
        self.base_url = "p://192.168.0.213:8081/"
        # 窗口最大化
        self.webdriver.maximize_window()
        # 设置隐式等待30s
        self.webdriver.implicitly_wait(10)

    def login(self):
        # 输入账号
        self.webdriver.find_element_by_xpath("//input[@id='txtUserID']").send_keys('xht')
        # 输入密码
        self.webdriver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("xht631020")
        # 输入验证码
        self.webdriver.find_element_by_xpath("//input[@id='txtVal']").send_keys("3")
        # 点击登录
        self.webdriver.find_element_by_xpath("//button[@id='loginBtn']").click()
        sleep(5)
        # 点击检测系统
        self.webdriver.find_element_by_xpath("//span[@id='div_m_menu__1043420190109165951']").click()
        sleep(2)



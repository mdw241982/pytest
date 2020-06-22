import pytest
from selenium import webdriver

driver.get("http://192.168.0.213:8081/")
# 窗口最大化
driver.maximize_window()
# 设置隐式等待30s
driver.implicitly_wait(30)
# 输入账号
driver.find_element_by_xpath("//input[@id='txtUserID']").send_keys('xht')
# 输入密码
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("xht631020")
# 输入验证码
driver.find_element_by_xpath("//input[@id='txtVal']").send_keys("3")
# 点击登录
driver.find_element_by_xpath("//button[@id='loginBtn']").click()
sleep(5)
# 点击检测系统
driver.find_element_by_xpath("//span[@id='div_m_menu__1043420190109165951']").click()
sleep(2)
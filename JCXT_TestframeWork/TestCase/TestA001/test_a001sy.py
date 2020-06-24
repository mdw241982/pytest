#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pytest
import allure
from selenium import webdriver
from time import sleep

@allure.feature('试验管理')
@allure.story('数据采集')
@allure.title('A001项目试验页面功能按钮测试')
@allure.severity('blocker')
@allure.setup('点击试验管理')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170048']").click()
sleep(2)
@allure.setup('点击数据采集菜单')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170630']").click()
sleep(2)
#
@allure.setup('选择打开混凝土抗压试验界面')
webdriver.switch_to.frame("ifm_m_page__1043420190109170630")
webdriver.find_element_by_xpath("//li[@id='A001']").click()
''' 
# 切换回默认窗体
driver.switch_to.default_content()
sleep(2)
# 查询出试验编号为 A0012006-00015 的记录
driver.find_element_by_xpath("//input[@id='txt_divPageBody__JCCX01G001A001divJCLst_1']").send_keys(sybh)
driver.find_element_by_xpath("//span[text()='查询']").click()
'''
sleep(3)
@allure.setup('选择列表中的第一条数据，点击编辑')
webdriver.find_element_by_xpath("//tr[@id='trLstdivPageBody__JCCX01G001A001divJCLst0']/td/a[text()='编辑']").click()

# 切换iframe
webdriver.switch_to.frame("ifmBody_divF0____")
@allure.setup('打开编辑页面，先点击保存')
webdriver.find_element_by_xpath("//input[@id='btnSave']").click()
sleep(3)
@allure.setup('录入试验数据')
webdriver.find_element_by_xpath("//input[@id='uc6_KYHZ1']").send_keys(1200)
webdriver.find_element_by_xpath("//input[@id='uc6_KYHZ2']").send_keys(1300)
webdriver.find_element_by_xpath("//input[@id='uc6_KYHZ3']").send_keys(1400)
# 点击保存
@allure.setup('点击保存')
webdriver.find_element_by_xpath("//input[@id='btnSave']").click()
sleep(3)
@allure.setup('点击提交')
webdriver.find_element_by_xpath("//input[@value='提交']").click()

#关闭浏览器，释放资源
webdriver.quit()
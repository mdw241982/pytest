#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pytest
import allure
from selenium import webdriver
from time import sleep

@allure.feature('委托管理')
@allure.story('业务受理')
@allure.title('委托页面A001项目功能按钮测试')
@allure.setup('点击委托管理')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170028']").click()
sleep(3)
@allure.setup('点击业务受理')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170233']").click()
sleep(2)
# 通过iframe的id来切换
webdriver.switch_to.frame("ifm_m_page__1043420190109170233")
@allure.setup('选择A001项目')
webdriver.find_element_by_xpath("//li[@id='A001']/a[1]").click()
# 切换回默认窗体
webdriver.switch_to.default_content()
@allure.setup('在A001委托页面新增数据')
webdriver.find_element_by_xpath("//td[@id='divPageBody__WTCX01G001A001divWTLst_td_btns']/a[text()='新增']").click()
# 切换iframe
webdriver.switch_to.frame("ifmBody_divF0____")
# 录入委托信息
@allure.setup('新增接样批号')
webdriver.find_element_by_xpath("//input[@id='sel_WTPH']").click()
# 切换回默认窗体
webdriver.switch_to.default_content()
@allure.setup('点击确认')
webdriver.find_element_by_xpath("//a[@id='aBtndiv_alert_form_']").click()
# 切换iframe
webdriver.switch_to.frame("ifmBody_divF0____")
sleep(2)
@allure.setup('录入委托单位')
webdriver.find_element_by_xpath("//input[@id='ct9']").send_keys("委托单位")
@allure.setup('点击选择检测项目')
webdriver.find_element_by_xpath("//input[@id='sel_JYXM']").click()
# 切换回默认窗体
webdriver.switch_to.default_content()

@allure.setup('选择检测项目')
webdriver.find_element_by_xpath("//input[@id='chkTrdivF2__db_UnitPrice_List0']").click()
@allure.setup('点击确定')
webdriver.find_element_by_xpath("//input[@id='btnSave']").click()
# 切换iframe
webdriver.switch_to.frame("ifmBody_divF0____")
@allure.setup('选择规格尺寸')
webdriver.find_element_by_xpath("//input[@id='ct28']").click()
webdriver.find_element_by_xpath("//a[text()='150×150×150']").click()
@allure.setup('选择养护方法')
webdriver.find_element_by_xpath("//input[@id='ct29']").click()
webdriver.find_element_by_xpath("//a[text()='标准养护']").click()
@allure.setup('选择设计等级')
webdriver.find_element_by_xpath("//input[@id='ct30']").click()
@allure.setup('选择检测类别')
webdriver.find_element_by_xpath("//input[@id='ct18']").click()
webdriver.find_element_by_xpath("//a[text()='委托抽检']").click()
@allure.setup('选择要求试验日期')
webdriver.find_element_by_xpath("//input[@id='ct26']").click()
webdriver.find_element_by_xpath("//a[text()='C45']").click()
# 切换回默认窗体
webdriver.switch_to.default_content()
# 切换iframe，选择日期
webdriver.switch_to.frame(webdriver.find_element_by_xpath("//div[@lang='zh-cn']/iframe"))
# 点击选择当天
@allure.setup('点击选择当天日期')
webdriver.find_element_by_xpath("//input[@id='dpTodayInput']").click()
# 切换回默认窗体
webdriver.switch_to.default_content()
# 切换iframe，回到委托录入页面
webdriver.switch_to.frame("ifmBody_divF0____")
@allure.setup('点击保存')
webdriver.find_element_by_xpath("//input[@id='btnSave']").click()
# 获取试验编号
# sybh=driver.find_element_by_xpath("//input[@id='ct2']").get_attribute("value")
#
@allure.setup('把数据提交到试验')
webdriver.find_element_by_xpath("//input[@value='提交']").click()

#关闭浏览器，释放资源
webdriver.quit()
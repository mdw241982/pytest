#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pytest
import allure
from selenium import webdriver
from time import sleep

@allure.feature('报告管理')
@allure.story('打印管理')
@allure.title('A001项目打印页面功能按钮测试')
@allure.setup('点击报告管理菜单')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170102']").click()
sleep(2)
@allure.setup('点击打印管理')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190220182429']").click()
sleep(2)

@allure.setup('点击预览')
webdriver.find_element_by_xpath("//tr[@id='trLstdivPageBody__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190220182519divLst20']/td/a[text()='预览']").click()
sleep(2)
@allure.setup('关闭预览界面')
webdriver.find_element_by_xpath("//div[@id='dh_divF0__']/div/label[1]").click()

@allure.setup('勾选列表中的第一条数据')
webdriver.find_element_by_xpath("//input[@id='chkTrdivPageBody__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190220182519divLst20']").click()

@allure.setup('点击打印按钮')
webdriver.find_element_by_xpath("//a[text()='打印']").click()
sleep(3)
@allure.setup('点击首页')
webdriver.find_element_by_xpath("//span[@id='div_m_menu__1043420180718082646']").click()

#关闭浏览器，释放资源
webdriver.quit()
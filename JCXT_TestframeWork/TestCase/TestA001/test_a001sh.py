#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pytest
import allure
from selenium import webdriver
from time import sleep

@allure.feature('审批管理')
@allure.story('报告审核')
@allure.title('A001项目审核页面功能按钮测试')
@allure.severity('blocker')
@allure.setup('点击审批管理菜单')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170053']").click()
sleep(2)
@allure.setup('打开报告审核页面')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170753']").click()
sleep(2)
# 打开审核编辑页面
@allure.setup('打开审核编辑页面')
webdriver.find_element_by_xpath("//tr[@id='trLstdivPageBody__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190219082020divLst10']/td/a[text()='审核']").click()
sleep(2)
# 切换iframe
webdriver.switch_to.frame("ifmBody_divF0____")
@allure.setup('点击通过')
webdriver.find_element_by_xpath("//input[@id='8b11080a-3d5b-4cef-8ebd-13ef5f150bbe']").click()

#关闭浏览器，释放资源
webdriver.quit()




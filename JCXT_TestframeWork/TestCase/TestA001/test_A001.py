import pytest
import allure
from login import TestJCXT
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



# -----------------------委托界面操作----begin---------------------------------
# 点击委托管理

@allure.feature('委托管理')
@allure.story('业务受理')
@allure.title('A001项目功能按钮测试')
@allure.setup('点击委托管理')
webdriver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170028']").click()
sleep(3)
# 点击业务受理
driver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170233']").click()
sleep(2)
# 通过iframe的id来切换
driver.switch_to.frame("ifm_m_page__1043420190109170233")
@allure.setup('选择A001项目')
driver.find_element_by_xpath("//li[@id='A001']/a[1]").click()
# 切换回默认窗体
driver.switch_to.default_content()
# 在混凝土抗压委托委托页面新增数据
driver.find_element_by_xpath("//td[@id='divPageBody__WTCX01G001A001divWTLst_td_btns']/a[text()='新增']").click()
# 切换iframe
driver.switch_to.frame("ifmBody_divF0____")
# 录入委托信息
# 新增接样批号
driver.find_element_by_xpath("//input[@id='sel_WTPH']").click()
# 切换回默认窗体
driver.switch_to.default_content()
# 点击确认
driver.find_element_by_xpath("//a[@id='aBtndiv_alert_form_']").click()
# 切换iframe
driver.switch_to.frame("ifmBody_divF0____")
sleep(2)
# 录入委托单位
driver.find_element_by_xpath("//input[@id='ct9']").send_keys("委托单位")
# 点击选择检测项目
driver.find_element_by_xpath("//input[@id='sel_JYXM']").click()
# 切换回默认窗体
driver.switch_to.default_content()

# 选择检测项目
driver.find_element_by_xpath("//input[@id='chkTrdivF2__db_UnitPrice_List0']").click()
# 点击确定
driver.find_element_by_xpath("//input[@id='btnSave']").click()
# 切换iframe
driver.switch_to.frame("ifmBody_divF0____")
# 选择规格尺寸
driver.find_element_by_xpath("//input[@id='ct28']").click()
driver.find_element_by_xpath("//a[text()='150×150×150']").click()
# 选择养护方法
driver.find_element_by_xpath("//input[@id='ct29']").click()
driver.find_element_by_xpath("//a[text()='标准养护']").click()
# 选择设计等级
driver.find_element_by_xpath("//input[@id='ct30']").click()
driver.find_element_by_xpath("//a[text()='C45']").click()
# 选择检测类别
driver.find_element_by_xpath("//input[@id='ct18']").click()
driver.find_element_by_xpath("//a[text()='委托抽检']").click()
# 选择要求试验日期
driver.find_element_by_xpath("//input[@id='ct26']").click()
# 切换回默认窗体
driver.switch_to.default_content()
# 切换iframe，选择日期
driver.switch_to.frame(driver.find_element_by_xpath("//div[@lang='zh-cn']/iframe"))
# 点击选择当天
driver.find_element_by_xpath("//input[@id='dpTodayInput']").click()
# 切换回默认窗体
driver.switch_to.default_content()
# 切换iframe，回到委托录入页面
driver.switch_to.frame("ifmBody_divF0____")
# 点击保存
driver.find_element_by_xpath("//input[@id='btnSave']").click()
# 获取试验编号
sybh=driver.find_element_by_xpath("//input[@id='ct2']").get_attribute("value")
# 把数据提交到试验
driver.find_element_by_xpath("//input[@value='提交']").click()

#关闭浏览器，释放资源
webdriver.quit()
# -----------------------委托界面操作--------end-----------------------------


# -----------------------试验界面操作----begin---------------------------------
# 切换回默认窗体
driver.switch_to.default_content()
# 点击试验管理
driver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170048']").click()
sleep(2)
# 点击数据采集菜单
driver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170630']").click()
sleep(2)
# 选择打开混凝土抗压试验界面
driver.switch_to.frame("ifm_m_page__1043420190109170630")
driver.find_element_by_xpath("//li[@id='A001']").click()
# 切换回默认窗体
driver.switch_to.default_content()
sleep(2)
# 查询出试验编号为 A0012006-00015 的记录
driver.find_element_by_xpath("//input[@id='txt_divPageBody__JCCX01G001A001divJCLst_1']").send_keys(sybh)
driver.find_element_by_xpath("//span[text()='查询']").click()
sleep(3)
# 打开试验编辑页面
driver.find_element_by_xpath("//a[text()='编辑']").click()

# 切换iframe
driver.switch_to.frame("ifmBody_divF0____")
# 先点击保存
driver.find_element_by_xpath("//input[@id='btnSave']").click()
sleep(3)
# 录入试验数据
driver.find_element_by_xpath("//input[@id='uc6_KYHZ1']").send_keys(1200)
driver.find_element_by_xpath("//input[@id='uc6_KYHZ2']").send_keys(1300)
driver.find_element_by_xpath("//input[@id='uc6_KYHZ3']").send_keys(1400)
# 点击保存
driver.find_element_by_xpath("//input[@id='btnSave']").click()
sleep(3)
# 点击提交
driver.find_element_by_xpath("//input[@value='提交']").click()

# -----------------------试验界面操作--------end-----------------------------

# ------------------------审核管理---begin------------------------------------

# 切换回默认窗体
driver.switch_to.default_content()
# 点击审批管理菜单
driver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170053']").click()
sleep(2)
# 打开报告审核页面
driver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170753']").click()
sleep(2)
# 输入试验编号
driver.find_element_by_xpath(
    "//input[@id='txt_divPageBody__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190219082020divLst1_2']").send_keys(
    sybh)
driver.find_element_by_xpath("//span[text()='查询']").click()
sleep(3)
# 打开审核编辑页面
driver.find_element_by_xpath("//a[text()='审核']").click()
sleep(2)
# 切换iframe
driver.switch_to.frame("ifmBody_divF0____")
# 点击通过
driver.find_element_by_xpath("//input[@id='8b11080a-3d5b-4cef-8ebd-13ef5f150bbe']").click()
sleep(2)

# ------------------------审核管理---end--------------------------------------

# ------------------------批准管理---begin------------------------------------
# 切换回默认窗体
driver.switch_to.default_content()
# 打开批准列表
driver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170804']").click()
sleep(2)
# 查询试验编号对应的数据
driver.find_element_by_xpath(
    "//input[@id='txt_divPageBody__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190219091741divLst1_2']").send_keys(
    sybh)
sleep(3)
driver.find_element_by_xpath("//span[text()='查询']").click()
driver.find_element_by_xpath("//a[text()='批准']").click()
sleep(2)
# 切换iframe
driver.switch_to.frame("ifmBody_divF0____")
# 点击通过
driver.find_element_by_xpath("//input[@id='8b11080a-3d5b-4cef-8ebd-13ef5f150bbe']").click()
sleep(2)

# ------------------------批准管理---end--------------------------------------

# ------------------------报告管理---begin------------------------------------
# 切换回默认窗体
driver.switch_to.default_content()
# 点击报告管理
driver.find_element_by_xpath("//div[@id='div_m_menu__1043420190109170102']").click()
sleep(2)
# 点击打印管理
driver.find_element_by_xpath("//div[@id='div_m_menu__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190220182429']").click()
sleep(2)
# 查询试验编号对应的数据
driver.find_element_by_xpath("//input[@id='txt_divPageBody__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190220182519divLst2_2']").send_keys(sybh)
sleep(3)
driver.find_element_by_xpath("//span[text()='查询']").click()
sleep(2)
# 点击打印
driver.find_element_by_xpath("//input[@id='chkTrdivPageBody__8805F4BE-201B-4FB8-9FA9-F37BA776FEE320190220182519divLst20']").click()

# 点击预览
driver.find_element_by_xpath("//a[text()='预览']").click()
sleep(2)
driver.find_element_by_xpath("//div[@id='dh_divF0__']/div/label[1]").click()

driver.find_element_by_xpath("//a[text()='打印']").click()
sleep(3)

driver.find_element_by_xpath("//span[@id='div_m_menu__1043420180718082646']").click()

if __name__ =="__main__":
    pytest

# ------------------------报告管理---end--------------------------------------

# 关闭浏览器，释放资源
# driver.quit()
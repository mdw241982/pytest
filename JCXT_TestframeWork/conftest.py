from selenium import webdriver
import pytest
driver = None
driver = webdriver.Chrome()


"""
测试报告环境信息配置
"""
def pytest_sessionfinish(session):
    with open("{}/temp/environment.properties".format(session.config.rootdir), "w") as f:
        f.write("borwser=chrome\nServer=windows2012/sql2008\ndomain=http://192.168.0.213:8081/Default.html\nuser=\npwd=")















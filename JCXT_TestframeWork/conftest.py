import os
from datetime import datetime
def pytest_configure(config):
    """Pytest初始化时配置方法"""
    if config.getoption('htmlpath'):  # 如果传了--html参数
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        config.option.htmlpath = os.path.join(config.rootdir, 'reports', f'report_{now}.html')
"""
测试报告环境信息配置
"""
def pytest_sessionfinish(session):
    with open("{}/temp/environment.properties".format(session.config.rootdir), "w") as f:
        f.write("borwser=chrome\nServer=windows2012/sql2008\ndomain=http://192.168.0.213:8081/Default.html\nuser=\npwd=")















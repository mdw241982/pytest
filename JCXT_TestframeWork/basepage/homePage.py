from selenium.webdriver.support.wait import WebDriverWait #显示等待
from selenium.webdriver.support import expected_conditions as EC #判断元素是否定位到

#基础类

class BasePage(object):
    '''初始化页面'''
    def __init__(self,dr,base_url):
        self.base_url = base_url
        self.dr = dr

    # 封装元素定位方式
    def find_element(self, *loc):
        try:
            WebDriverWait(self.dr, 10).until(EC.visibility_of_element_located(loc))
            return self.dr.find_element(*loc)
        except:
            print(*loc + '元素定位在页面中无法找到')
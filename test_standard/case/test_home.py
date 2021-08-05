# coding:utf-8
import unittest
from selenium import webdriver
from test_standard.page.login_page import LoginPage,loginurl
from test_standard.page.heom_page import HomePage,home_url


class TestLogin(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.ChromeOptions()
        self.driver =webdriver.Chrome()
        self.xflogin = LoginPage(self.driver) # 初始化
        self.home = HomePage(self.driver)   # 初始化
        #self.xflogin.move_h5_browser("iPhone X")

        # 因ChromeOptions() 无get方法 暂未找到方法
        self.driver.get(loginurl)     # 每次都打开登录地址，但只打开一个浏览器
        self.xflogin.login(13074538365,"Qwe123456")

    def test_01(self):
        # 点击精选下的分类
        self.driver.get(home_url)    # 打开首页
        self.home.fel_click()

        # 获取返回结果
        result=self.home.iread_is_text()
        print(result)
        # 断言
        fel = "分类精选"
        self.assertEqual(result,fel) # 要将用例执行完


    def tearDown(self):
        #self.driver.delete_all_cookies()    #删除所有cookies
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
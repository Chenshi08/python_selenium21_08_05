# coding:utf-8
import unittest
from selenium import webdriver
from test_standard.page.login_page import LoginPage,loginurl

class TestLogin(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):      # 不可用   只打开一次浏览器
    #     cls.driver = webdriver.ChromeOptions()
    #     cls.xflogin = XifeLogin(cls.driver) # 初始化
    #     cls.xflogin.move_h5_browser("iPhone X")

    def setUp(self):
        self.driver = webdriver.ChromeOptions()
        self.xflogin = LoginPage(self.driver) # 初始化
        self.xflogin.move_h5_browser("iPhone X")
        self.xflogin.open(loginurl)     # 每次都打开登录地址，但只打开一个浏览器

    def test_01(self):
        # 输入账号
        self.xflogin.iread_user("17693119640")
        # 输入密码
        self.xflogin.iread_posword("Qwe123456")
        # 点击登陆
        self.xflogin.iread_drag(260)
        # 获取返回结果
        result = self.xflogin.is_longin_sucess()
        # 断言为真时使用True
        self.assertTrue(result)



    def tearDown(self):
        # self.driver.delete_all_cookies()    #删除所有cookies,次方法只可用在self.driver= webdriver.Chorme()中
        self.xflogin.driver.quit()

    # @classmethod
    # def tearDownClass(cls):    # classmethod 此方法不能使用
    #     cls.driver.qiut()

if __name__ == "__main__":
    unittest.main()
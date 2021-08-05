# coding:utf-8
from selenium import webdriver
from test_standard.page.login_page import LoginPage,loginurl
import ddt
from  test_standard.common.read_excel import ExcelUtil
import unittest
# date=[
#     {"usernaem":"18515393439","psw":"Qwe123456","exp":"更多"},
#     {"usernaem":"18515393439","psw":"Qwe12345","exp":" "}
#     ]
filepath = "E:\\数据.xlsx"
sheetName = "Sheet1"
d = ExcelUtil(filepath,sheetName)
date = d.dict_data() # 将读取数据赋值
print(date)
# dat_login1={"usernaem":"18515393438","pws":"Qwe123456","exp":"更多"}
# dat_login2={"usernaem":"18515393438","pws":"Qwe12345","exp":" "}

@ddt.ddt()      #ddt数据驱动
class TestLogin(unittest.TestCase):
    '''
    # @classmethod
    # def setUpClass(cls):      # 不可用   只打开一次浏览器
    #     cls.driver = webdriver.ChromeOptions()
    #     cls.xflogin = XifeLogin(cls.driver) # 初始化
    #     cls.xflogin.move_h5_browser("iPhone X")
    '''
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.ChromeOptions()
        self.xflogin = LoginPage(self.driver) # 初始化
        self.xflogin.move_h5_browser("iPhone X")

        #self.xflogin.move_h5_browser("iPhone X")
        self.xflogin.driver.get(loginurl)     # 每次都打开登录地址，但只打开一个浏览器

    def login_all(self,usernaem,psw,exp):
        # 输入账号
        self.xflogin.iread_user(usernaem)
        # 输入密码
        self.xflogin.iread_posword(psw)
        # 点击登陆
        self.xflogin.iread_drag(260)
        # 获取返回结果
        result = self.xflogin.is_longin_sucess()
        return result==exp

    @ddt.data(*date)
    def test_01(self,testdate):
        # print(testdate)
        # 调用登录
        # result=self.login_all(18515393438,"Qwe123456","更多")   # 参数化方法1
        # 数据驱动方法1
        # result=self.login_all(dat_login1["usernaem"],dat_login1["pws"],dat_login1["exp"])     # 数据驱动
        result=self.login_all(**testdate)
        # 断言为真时使用True
        self.assertFalse(result)

    # def test_02(self,testdate1):
    #     # 调用登录
    #     # result = self.login_all(18515393438,"Qwe123456"," ")  # 参数化 方法1
    #     # 方法1
    #     # result=self.login_all(dat_login2["usernaem"],dat_login2["pws"],dat_login2["exp"])     # 数据驱动
    #     result=self.login_all(**testdate1)
    #     # 断言为真时使用True
    #     self.assertTrue(result)


    def tearDown(self):
        # self.driver.delete_all_cookies()    #删除所有cookies,次方法只可用在self.driver= webdriver.Chorme()中
        self.xflogin.driver.quit()
    '''
    # @classmethod
    # def tearDownClass(cls):    # classmethod 此方法不能使用 只有在wenbdriver.Chorme()可使用
    #     cls.driver.qiut()
    '''

if __name__ == "__main__":
    unittest.main()
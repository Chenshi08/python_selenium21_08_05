# coding:utf-8
from test_standard.common.selenium_common import Test_customization
from test_standard.config import readconfig
url = readconfig.iread_url
loginurl = url+"userinfo/login/gotoLoginPage.action"

class LoginPage(Test_customization):
    u'''细分步骤，每一个步骤写一个方法
        以百度登录为例
        denglu_loc
    '''
    user_loc = ('id',"loginName")   # 点击登录按钮
    posword_loc = ('id',"loginPass")     # 点击用户
    drag_loc = ('id',"label")       # 进度条

    # 写元素页面是不需要重新初始化
    # def __init__(self,driver):
    #     self.driver =driver

    def iread_user(self , text):
        # 输入账号
        self.is_send_key(self.user_loc,text)

    def iread_posword(self,text):
        # 输入密码
        self.is_send_key(self.posword_loc,text)
    def iread_drag(self,right):
        # 拖动进度条登录
        self.move_h5_action(self.drag_loc,right)

    def login(self,username,password):
        self.iread_user(username)
        self.iread_posword(password)
        self.iread_drag(260)
    # 断言
    def is_longin_sucess(self):
        try:
            sucess_loc = ("xpath","//div[@class='c-main']/div/a[2]")
            result = self.is_exists(sucess_loc)
            print(result)
            return True
        except:
            print("未获取到")
            return ''

if __name__ == "__main__":
    from selenium import webdriver
    import time
    driver = webdriver.ChromeOptions()
    lon = LoginPage(driver)
    lon.move_h5_browser("iPhone X")
    lon.open(loginurl)
    time.sleep(3)
    lon.iread_user('18515393438')
    lon.iread_posword("Qwe123456")
    time.sleep(3)
    lon.iread_drag(260)
    time.sleep(2)
    lon.is_longin_sucess()
    time.sleep(1)
    lon.driver.quit()
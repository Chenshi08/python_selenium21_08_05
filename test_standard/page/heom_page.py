# coding:utf-8
from test_standard.common.selenium_common import Test_customization
from test_standard.config import readconfig
url = readconfig.iread_url
home_url =url + "index.action?indexType=book"
class HomePage(Test_customization):

    fel_loc = ("xpath","//div[@class=' awf90p']/ul/li[1]")  # 精选分类
    panh_loc = ("xpath","//div[@class=' awf90p']/ul/li[2]")
    bay_loc = ("xpath","//div[@class=' awf90p']/ul/li[3]")
    zhuanti_loc = ("xpath","//div[@class=' awf90p']/ul/li[4]")
    huodong_loc = ("xpath","//div[@class=' awf90p']/ul/li[4]")

    def fel_click(self):
        self.is_click(self.fel_loc)

    def pah_click(self):
        self.is_click(self.panh_loc)

    def bay_click(self):
        self.is_click(self.bay_loc)

    def iread_is_text(self):
        try:
            fel = ("xpath","//div[@class= 'nav_ct']")
            result = self.is_text_in_element(fel," 分类精选")
            return result
        except:
            print("元素获取异常，返回' ' ")
            return ' '
if __name__ == "__main__":
    from selenium import webdriver
    import time
    driver = webdriver.ChromeOptions()
    home=HomePage(driver)
    home.move_h5_browser("iPhone X")
    home.driver.get(home_url)
    home.fel_click()
    time.sleep(2)
    fl=home.iread_is_text()
    print(fl)
    home.driver.quit()

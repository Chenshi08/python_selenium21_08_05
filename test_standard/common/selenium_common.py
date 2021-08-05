# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time


class Test_customization():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 20 # 超时时间

    def open(self,url):
        '''
        使用get,打开浏览器，最大化窗口
        '''
        self.driver.get(url)        # 打开浏览器
        self.driver.maximize_window()    # 将打开浏览器设置全屏

    def find_element(self,locator):
        '''
        定位元素参数locator 是元组类型
        查找元素和判断元素结合，所以方法都可以使用
        self.driver：浏览器调用
        locator 参数是定位方式，如("id", "kw"),把两个参数合并为一个
        *号是把两个参数分开传值
        在20s内去查定位的元素，每隔1s查一次
        '''
        try:
            element = WebDriverWait(self.driver,self.timeout,1).until(EC.presence_of_element_located(locator))  # presence_of_element_located查找元素
            return element      # 查找元素和判断元素结合
        except:
            return False

    def find_elements(self,locator):
        '''
        定位一组元素
        self.driver：浏览器调用
        locator 参数是定位方式，如("id", "kw"),把两个参数合并为一个
        *号是把两个参数分开传值
        在20s内去查定位的元素，每隔1s查一次
        '''
        try:
            element = WebDriverWait(self.driver,self.timeout,1).until(EC.presence_of_all_elements_located(locator))
            return element
        except:
            return False

    def is_find_element(self,locator):
        '''
        locator 参数是定位方式，如("id", "kw"),把两个参数合并为一个
        *号是把两个参数分开传值
        Usage:
            locator = ("id", "kw")
            driver.find_element(*locator)
         WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        '''
        try:
            element = WebDriverWait(self.driver,self.timeout,1).until(lambda x:x.find_element(*locator))
            return element      # 判断元素存在
        except Exception as e:
            return False

    def is_not_find_element(self,locator):
        '''        判断元素不存在：元素在指定时间内找不到，返回Ture,否则抛超时异常
         Usage:
             locator = ("id", "kw")
             driver.element_is_disappeared(*locator)
         '''
        try:
            is_element = WebDriverWait(self.driver, self.timeout, 1, (ElementNotVisibleException)).\
                until_not(lambda x:x.find_element(*locator).is_displayed())
            # is_disappeared = WebDriverWait(self.driver, timeout, 1, (ElementNotVisibleException)).\
            #     until_not(lambda x: x.find_element(*locator).is_displayed())
            return is_element       # 判断元素不存在
        except Exception as e:
            print("is_element：",format(e))
            return False

    def is_click(self,locator):
        '''
        调用find_element方法，在进行点击操作
        '''
        element=self.find_element(locator)
        element.click()  # 点击事件 *locator 可以为locator

    def is_send_key(self,locator,text,is_clear = True):
        '''
        发送文本，清空后输入
        使用send_keys输入

        '''
        element=self.find_element(locator)   # 输入框输入内容    *locator 可以为locator
        if is_clear == True:element.clear()
        return element.send_keys(text)

    def is_text_in_element(self,locator,text):
        '''
        判断在元素里，没有定位到元素返回False，定位到返回布尔值
        判断文本是否相等,locator无需使用*
        locator :为定位文本
        test：验证输入的文本
         查找文本和判断文本
         WebDriverWait(self.driver,20,1).until(EC.text_to_be_present_in_element(locator, text)))
        '''
        try:
            rtext =WebDriverWait(self.driver,self.timeout ,1).until(EC.text_to_be_present_in_element(locator,text))
             # 判断文本是否相等,locator无需使用*
            return rtext
        except :
            return False

    def is_text_in_vlue(self,vlue,test):
        '''
        判断vlue值,没有定位到元素返回False，定位到返回布尔值
        test为校验vlue的值
        '''
        try:
            isvlue=WebDriverWait(self.driver,self.timeout ,1).until(EC.text_to_be_present_in_element_value(vlue,test))        # 判断vlue值是否相等,locator无需使用*
            return isvlue
        except :
            return False

    def is_title(self,title):
        '''
        判断title完全等于
        title = EC.title_is(u'百度一下， 你就知道')
        '''
        try:
            rtitle =WebDriverWait(self.driver,self.timeout ,1).until(EC.title_is(title))    # 验证页面tilie相等
            return rtitle
        except Exception as e:
            return False

    def is_all_title(self,title):
        ''' 判断title包含 title1 = EC.title_contains(u'百度一下') '''
        try:
            rtitle  =WebDriverWait(self.driver,self.timeout ,1).until(EC.title_contains(title))       # 验证页面tilie包含
            return rtitle
        except:
            return False

    def is_selectd(self,locator):
        '''判断元素被选中，返回布尔值;案例百度设置的下拉框'''
        try:
            elemnet  =WebDriverWait(self.driver,self.timeout ,1).until(EC.element_located_to_be_selected(locator))       # 验证页面tilie包含
            return elemnet
        except:
            return False

    def is_alert(self):
        '''
        判断页面是否有alert
        返回alert，（这里的alert不是True）
        没有就返回False
        '''
        try:
            aler =WebDriverWait(self.driver ,self.timeout,1).until(EC.alert_is_present())
            return aler
        except:
            return False

    def is_locator(self,locator):
        '''判断元素被定位到（并不意味着可见），定位到返回element，没有定位到返回False'''
        rlocator=WebDriverWait(self.driver,self.timeout,1).until(EC.presence_of_element_located(locator))
        return rlocator

    def is_exists(self,locator):
        '''判断元素存在'''
        try:
            self.is_locator(locator)
            return True
        except:
            return False

    def is_iframe(self,locator):
        ''' locator是tuple类型，locator的id和name是名称，返回布尔值'''
        try:
            frame=WebDriverWait(self.driver,self.timeout,1).until(EC.frame_to_be_available_and_switch_to_it(locator))
            return frame
        except:
            return False

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        elemnet=self.find_element(locator)
        ActionChains(self.driver).move_to_element(elemnet).perform() # 移动到某个元素

    def move_h5_action(self,locator,right):
        ''' 拖动H5页面进度条 '''
        try:
            canvas  = self.find_element(locator)  #.find_element(locator) #
            action = ActionChains(self.driver)
            action.click_and_hold(canvas)
            #移动鼠标
            action.move_by_offset(right,0)
            # 第三步：释放鼠标
            action.release()
            # 执行动作
            action.perform()
            time.sleep(2)
            return action
        except Exception as e:
            print("False:".format(e))
            return False

    def move_h5_browser(self,model):
        '''设置h5浏览器模式
        self.driver = webdriver.ChromeOptions()
        model:手机型号'iPhone X'
        在赋值后使用
        webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=self.options)
        '''
        self.options = webdriver.ChromeOptions()
        #options.add_experimental_option('prefs', prefs)  # 关掉浏览器左上角的通知提示
         #关闭'chrome正受到自动测试软件的控制'提示
        self.options.add_argument("disable-infobars")
        # #定义打开手机型号
        mobileEmulation = {'deviceName': model}
        #使用add_experimental_option方法打开
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        #将selenium中的webdriver赋值
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=self.options)
        self.driver.implicitly_wait(20)
        return self.driver

    def highLightElement(self, element):
        '''
        封装好的高亮显示页面元素的方法
        使用JS代码将传入的页面元素对象的背景颜色和边框
    　　 颜色分别设置为绿色和红色
        '''
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                                    element,
                                    "background:green;border:2px solid red;")       # 暂时无法适用于

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_screenshor(self,image_path):
        ''' 获取屏幕截图  image_path 存放的文件路径'''
        mowtime = time.strftime("%Y-%m-%d %H_%M_%S")
        try:
            fpath = os.path.join(image_path,mowtime+".png")
            self.driver.get_screenshot_as_file(fpath)
            print("screenshor :s%" %fpath)
        except Exception as e:
            print("Error screenshor :%s"%e)

    def is_get_text(self,locator):
        '''获取元素的文本'''
        try:
            rtext=self.find_element(locator).text
            return rtext
        except:
            return False

    def get_attribute(self,lcoator,name):
        ''' 获取属性  name 为class name id'''
        element = self.find_element(lcoator)
        return element.get_attribute(name)

    def select_by_index(self,locator,index=0):
        ''' 通过索引，index是索引第几个，从0开始，默认选择第一个  '''
        element = self.find_element(locator)
        Select(element).select_by_index(index)
        element.click()

    def select_all_index(self,locator):
        ''' 清除所有的选项'''
        element = self.find_element(locator)
        Select(element).deselect_all()

    def get_current_handle(self):
        ''' 获取当前句柄'''
        return self.driver.current_window_handle

    def get_handles(self):
        '''  获取所有句柄   '''
        time.sleep(2)
        h = self.driver.window_handles
        if len(h) <= 1:
            print("只获取到一个句柄，等待3s后重新获取")
            h = self.driver.window_handles
        return h

    def switch_iframe(self,locator):
        ''' 进入ifarme'''
        return self.is_iframe(locator)

    def js_execute(self,js):
        '''执行js'''
        self.driver.execute_script(js)

    def js_focus_element(self,locator):
        '''聚集元素,定位到 元素后在移动到元素位置'''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''移动到元素顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        # 滚动到底部
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def is_text_iframe(self,jstext):
        '''
        js写法只是专门处理富文本（有iframe）相关的问题，其它地方遇到iframe不一定通用
        jstext = "输入内容！！！！！"
        Editor_Edit_EditorBody_ifr 为查找到iframe的id
        s 为参数化输出内容
        此方法不一定有效
        '''
        js ='document.getElementById("Editor_Edit_EditorBody_ifr").contentWindow.document.body.innerHTML="%s"' % jstext
        self.driver.execute_script(js)

if __name__ == "__main__":
    # driver = webdriver.ChromeOptions()
    driver =webdriver.Chrome()
    iread = Test_customization(driver) # 实例化
    iread.driver.get("https://www.baidu.com/")
    time.sleep(2)

    user_col = ('id',"kw")
    user_cl = ('id',"su")
    iread.is_send_key(user_col,"python")
    time.sleep(2)
    iread.is_click(user_cl)

    # iread.move_h5_browser('iPhone X')
    # iread.open("https://m.iread.wo.cn/index.action?indexType=book")
    # time.sleep(2)
    # user_col = ('id',"loginName")   # 点击登录按钮
    # posword_col = ('id',"loginPass")     # 点击用户
    # drag_col = ('id',"label")       # 进度条
    # # iread.is_send_key(user_col,18515393438)
    # # iread.is_send_key(posword_col,"Qwe123456")
    # # time.sleep(2)
    # # print("2")
    # # iread.move_h5_action(drag_col,260)      #移动进度条
    # fel_loc = ("xpath","//div[@class=' awf90p']/ul/li[1]")  # 精选分类
    # iread.is_click(fel_loc)
    # time.sleep(2)
    # fel = ("xpath","//div[@class= 'nav_ct']")
    # result = iread.is_text_in_element(fel,"分类精选")
    # print(result)

    print("3")
    time.sleep(2)

    iread.driver.quit()
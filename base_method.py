from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import Logger
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import ActionChains
import pymysql
import os
import inspect
import pywintypes
import win32api
import win32clipboard as w
import win32con
import random
import time
class BasePage:
    def __init__(self,driver,title):
        self.driver=driver
        self.logger = Logger(title)
    def get_window_position(self):
        self.logger.info("正在准备获取当前窗口的位置")
        try:
            position = self.driver.get_window_position()
            self.logger.info("获取当前窗口成功为_{}".format(position))
            return position
        except Exception as e:
            self.logger.error("获取当前窗口位置失败")
            #raise e
    def set_window_position(self,y,x):
        self.logger.info("正在准备设置当前窗口的位置")
        try:
            y = int(y)
            x= int(x)
            self.driver.set_window_position(y,x)
            self.logger.info("设置当前窗口位置成功")
        except Exception as e:
            self.logger.error("设置当前窗口位置失败")
            #raise e

    def get_window_size(self):
        self.logger.info("正在准备获取当前窗口的大小")
        try:
            size = self.driver.get_window_size()
            self.logger.info("获取当前窗口大小成功为_{}".format(size))
            return size
        except Exception as e:
            self.logger.error("获取当前窗口大小失败")
            #raise e
    def set_window_size(self,width,height):
        self.logger.info("正在准备设置当前窗口的大小")
        try:
            width = int(width)
            height= int(height)
            self.driver.set_window_size(width,height)
            self.logger.info("设置当前窗口大小成功")
        except Exception as e:
            self.logger.error("设置当前窗口大小失败")
            #raise e
    def title(self):
        self.logger.info("正在准备获取当前页面的title")
        try:
            title = self.driver.title
            self.logger.info("获取当前页面的title成功_{}".format(title))
            return title
        except Exception as e:
            self.logger.error("获取当前页面的title失败")
            #raise e
    def get_page_source(self):
        self.logger.info("正在准备获取当前页面的html源码")
        try:
            page_source = self.driver.page_source
            self.logger.info("获取当前页面的html源码成功_{}".format(page_source))
            return page_source
        except Exception as e:
            self.logger.error("获取当前页面的html源码失败")
            #raise e
    def get_current_url(self):
        self.logger.info("正在准备获取当前页面的网址")
        try:
            current_url = self.driver.current_url
            self.logger.info("获取当前页面的网址成功_{}".format(current_url))
            return current_url
        except Exception as e:
            self.logger.error("获取当前页面的网址失败")
            #raise e
    # def

    def alter_is_present(self, timeout=30, frequency=1):
        self.logger.info("正在准备判断alter是否出现")
        try:
            timeout = int(timeout)
            frequency = int(frequency)
            WebDriverWait(self.driver, timeout, frequency).until(EC.alert_is_present())
            self.logger.info("alter 弹框已经出现")
        except Exception as e:
            self.logger.error("alter 弹框没有出现")
            raise  e
    def click_by_object(self,ele_object):
        self.logger.info("正在准备点击{}对象".format(ele_object))
        try:
            ele_object.click()
            self.logger.info("{}对象点击成功".format(ele_object))
        except Exception as e:
            self.logger.error("{}对象点击失败".format(ele_object))
            #raise e

    def click_elements_for_one(self, loc, index):
        self.logger.info("正在准备点击{}元素下标为{}的元素".format(loc, index))
        try:
            self.find_elements(loc, index).click()
            self.logger.info("{}元素下标为{}的元素点击成功".format(loc, index))
        except Exception as e:
            self.logger.error("{}元素下标为{}元素点击失败".format(loc, index))
            raise  e
    def click_element(self,loc):
        self.logger.info("正在准备点击{}元素".format(loc))
        try:
            self.find_element(loc).click()
            self.logger.info("{}元素点击成功".format(loc))
        except Exception as e:
            self.logger.error("{}元素点击失败".format(loc))
            #raise e
    def clear(self,loc):
        self.logger.info("正在准备清除{}元素输入框内容".format(loc))
        try:
              self.find_element(loc).clear()
              self.logger.info("{}元素输入框内容清除成功".format(loc))
        except Exception as e:
              self.logger.error("{}元素输入框内容清除失败".format(loc))
              raise  e
    def back(self):
        self.logger.info("正在准备后退")
        try:
            self.driver.back()
            self.logger.info("网页回退成功")
        except Exception as e:
            self.logger.error("网页回退失败")
            #raise e

    def forward(self):
        self.logger.info("正在准备前进")
        try:
            self.driver.forward()
            self.logger.info("网页前进成功")
        except Exception as e:
            self.logger.error("网页前进失败")
            #raise e

    def accept_or_dismiss_alter(self, value=1):  # driver.switch_to.alert.accept()
        self.logger.info("正在准备处理alter弹框")
        try:
            if int(value) == 1:
                text = self.driver.switch_to.alert.text
                self.driver.switch_to.alert.accept()
                self.logger.info("alter接受成功")
                return text
            else:
                text = self.driver.switch_to.alert.text
                self.driver.switch_to.alert.dismiss()
                self.logger.info("alter 取消接收")
                return text
        except Exception as e:
            self.logger.error("alter弹框处理失败")
            #raise e
    def find_element(self,loc):
        self.logger.info("正在准备查找{}元素".format(loc))
        try:
            ele_object=self.driver.find_element(*loc)
            self.logger.info("{}元素查找成功".format(loc))
            return ele_object
        except Exception as e:
            self.logger.error("{}元素查找失败")
            #raise e
    def find_elements_back_length(self,loc):
        self.logger.info("正在准备查找一些{}元素".format(loc))
        try:
            ele_object_list=self.driver.find_elements(*loc)
            self.logger.info("一些{}元素查找成功".format(loc))
            return len(ele_object_list)
        except Exception as e:
            self.logger.error("一些{}元素查找失败".format())
            #raise e

    def find_elements_back_object(self,loc,index):
        self.logger.info("正在准备查找一些{}元素".format(loc))
        try:
            ele_object=self.driver.find_elements(*loc)
            self.logger.info("一些{}元素查找成功".format(loc))
            index=int(index)
            return ele_object[index]
        except Exception as e:
            self.logger.error("一些{}元素查找失败".format(loc))
            #raise e

    def find_elements_back_objects(self,loc):
        self.logger.info("正在准备查找一些{}元素".format(loc))
        try:
            ele_objects=self.driver.find_elements(*loc)
            self.logger.info("一些{}元素查找成功".format(loc))
            return ele_objects
        except Exception as e:
            self.logger.error("一些{}元素查找失败".format(loc))
            #raise e

    def get(self,url):
        self.logger.info("正在准备访问{}".format(url))
        try:
            self.driver.get(url)
            self.logger.info("访问{}网址成功".format(url))
        except Exception as e:
            self.logger.error("访问{}网址失败".format(url))
            #raise e
    def text(self,loc):
        self.logger.info("正在准备获取{}元素的文本值".format(loc))
        try:
            text_value=self.find_element(loc).text
            self.logger.info("获取{}元素文本值成功_{}".format(loc,text_value))
            return text_value
        except Exception as e:
            self.logger.error("获取{}元素文本值失败".format(loc))
            #raise e

    # def is_selected(self, loc):
    #     self.logger.info("正在准备判断{}元素是否可被选中".format(loc))
    #     try:
    #         is_selected_value = self.find_element(loc).is_selected()
    #         if is_selected_value:
    #             self.logger.info("{}元素已经被选中".format(loc))
    #             return is_selected_value
    #         else:
    #             self.logger.info("{}元素没有被选中".format(loc))
    #             return is_selected_value
    #     except Exception as e:
    #         self.logger.error("判断{}元素是否被选中失败".format(loc))
    #         #raise e

    # def is_selected_by_ele(self, ele):
    #     self.logger.info("正在准备判断{}对象是否可被选中".format(ele))
    #     try:
    #         is_selected_value = ele.is_selected()
    #         if is_selected_value:
    #             self.logger.info("{}对象已经被选中".format(ele))
    #             return is_selected_value
    #         else:
    #             self.logger.info("{}对象没有被选中".format(ele))
    #             return is_selected_value
    #     except Exception as e:
    #         self.logger.error("判断{}对象是否被选中失败".format(ele))
    #         #raise e
    def refresh(self):
        self.logger.info("正在准备刷新页面")
        try:
            self.driver.refresh()
            self.logger.info("页面刷新成功")
        except:
            self.logger.error("页面刷新失败")

    def send_keys(self,loc,value):
        self.logger.info("正在准备在{}元素输入框输入内容".format(loc,value))
        try:
            self.find_element(loc).send_keys(value)
            self.logger.info("{}元素输入框输入_{}_内容成功".format(loc,value))
        except Exception as e:
            self.logger.error("{}元素输入框输入{}内容失败".format(loc,value))
            #raise e

    def scroll_into_view(self,loc):
        self.logger.info("正在准备滚动屏幕到目标元素{}".format(loc))
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();",self.find_element(loc))
            self.logger.info("滚动到目标元素{}成功".format(loc))
        except Exception as e:
            self.logger.error("滚动到目标元素{}失败".format(loc))
            #raise e

    def select_by_value(self,loc,select_value):
        self.logger.info("正在准备选中下拉列表的value值为{}的元素".format(select_value))
        try:
            select=Select(self.find_element(loc))
            select.select_by_value(select_value)
            self.logger.info("下拉列表value值为{}的元素被选中".format(select_value))
        except Exception as e:
            self.logger.error("下拉列表value值为{}的元素选中失败".format())
            #raise e
    def sql_search_one(self,sql):
        self.logger.info("正在准备查询数据库值")
        try:
            file_path = os.path.join(os.path.dirname(__file__),"MYSQL.ini")
            with open(file_path,"r") as f:
                read_text = f.read()
                read_list = read_text.split(";")
                ip = read_list[0]
                username = read_list[1]
                password= read_list[2]
                port = int(read_list[3])
                database = read_list[4]
                conn = pymysql.connect(host=ip, port=port, user=username, password=password,
                                       database=database)
                cursor = conn.cursor()
                cursor.execute(sql)
                text = cursor.fetchone()[0]
                cursor.close()
                conn.close()
                self.logger.info("数据库查询成功为_{}".format(text))
                return  text
        except Exception as e:
            self.logger.error("数据库查询失败")
            #raise e
    def title(self):
        self.logger.info("正在准备获取网页的标题")
        try:
            title = self.driver.title
            self.logger.info("标题获取成功为：{}".format(title))
            return title
        except Exception as e:
            self.logger.error("标题获取失败")
            #raise e
    def presence_of_element_located(self,loc,timeout=30,frequency=1):
        """等待元素被加载到dom树并不一定可见"""
        self.logger.info("正在准备等待元素{}被加载到dom树中".format(loc))
        try:
            timeout =int(timeout)
            frequency=int(frequency)
            WebDriverWait(self.driver,timeout,frequency).until(EC.presence_of_element_located(loc))
            self.logger.info("{}元素被成功加载到dom树".format(loc))
        except Exception as e:
            self.logger.error("{}元素不存在dom树中")
            #raise e
    def visibility_of_element_located(self,loc,timeout=30,frequency=1):
        """等待元素可见"""
        self.logger.info("正在准备等待{}元素可见".format(loc))
        try:
             timeout = int(timeout)
             frequency =int(frequency)
             WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
             self.logger.info("{}元素可见成功".format(loc))
        except Exception as e:
             self.logger.error("等待{}元素可见失败".format(loc))
             #raise e
    def double_click(self,loc):
        self.logger.info("正在准备双击{}元素".format(loc))
        try:
            action_chains = ActionChains(self.driver)
            action_chains.double_click(self.find_element(loc)).perform()
            self.logger.info("{}元素双击成功".format(loc))
        except Exception as e:
            self.logger.error("{}元素双击失败".format(loc))
            #raise e

    def select_by_visible_text(self,loc,select_text):
        self.logger.info("正在准备选中下拉列表的text值为{}的元素".format(select_text))
        try:
            select=Select(self.find_element(loc))
            select.select_by_visible_text(select_text)
            self.logger.info("下拉列表text值为{}的元素被选中".format(select_text))
        except Exception as e:
            self.logger.error("下拉列表text值为{}的元素选中失败".format())
            #raise e

    def select_by_index(self, loc, select_index):
        self.logger.info("正在准备选中下拉列表的索引值为{}的元素".format(select_index))
        try:
            select = Select(self.find_element(loc))
            select.select_by_index(select_index)
            self.logger.info("下拉列表的索引值为{}的元素被选中".format(select_index))
        except Exception as e:
            self.logger.error("下拉列表的索引值为{}的元素选中失败".format())
            #raise e
    def get_select_text(self, loc):
        self.logger.info("正在准备获取下拉列表选中的文本_{}的元素".format(loc))
        try:
            select = Select(self.find_element(loc))
            text=select.all_selected_options[0].text
            self.logger.info("下拉列表选中的文本为{}".format(text))
            return text
        except Exception as e:
            self.logger.error("获取下拉列表选中的文本失败".format())
            #raise e
    def set_clipboard_data(self,data):
        self.logger.info("正在设置剪切板内容为_{}".format(data))
        try:
            w.OpenClipboard()
            # 清空剪切板
            w.EmptyClipboard()
            # 剪切内容
            w.SetClipboardData(win32con.CF_UNICODETEXT,data)
            # 关闭剪切板
            w.CloseClipboard()
            self.logger.info("设置剪切板内容成功为_{}".format(data))
        except Exception as e:
            self.logger.error("设置剪切板内容失败")
            #raise e
    def ctrl_c(self):
        self.logger.info("正在准备复制内容")
        try:
            VK_CODE = {
                'enter': 0x0D,
                'ctrl': 0x11,
                'v': 0x56,
            }
            win32api.keybd_event(VK_CODE["ctrl"], 0, 0, 0)
            # 按下v键
            win32api.keybd_event(VK_CODE["v"], 0, 0, 0)
            # 释放ctrl键
            win32api.keybd_event(VK_CODE["ctrl"], 0, win32con.KEYEVENTF_KEYUP, 0)
            # 释放v键
            win32api.keybd_event(VK_CODE["v"], 0, win32con.KEYEVENTF_KEYUP, 0)
            self.logger.info("复制内容成功")
        except Exception as e:
            self.logger.error("复制内容失败")
            #raise e
    def enter(self):
        self.logger.info("正在准备按下enter按键")
        try:
            VK_CODE = {
                'enter': 0x0D,
                'ctrl': 0x11,
                'v': 0x56,
            }
            win32api.keybd_event(VK_CODE["enter"], 0, 0, 0)
            #释放enter键
            win32api.keybd_event(VK_CODE["enter"], 0, win32con.KEYEVENTF_KEYUP, 0)
            self.logger.info("按下enter按键成功")
        except Exception as e:
            self.logger.error("按下enter按键失败")
            #raise e
    def context_click(self,loc):
        self.logger.info("正在准备点击鼠标右键")
        try:
            ActionChains(self.driver).context_click(self.find_element(loc)).perform()
            self.logger.info("点击鼠标右键成功")
        except Exception as e:
            self.logger.error("点击鼠标右键失败")
            #raise e
    def click_and_hold(self,loc):
        self.logger.info("正在准备按住鼠标左键")
        try:
            ActionChains(self.driver).click_and_hold(self.find_element(loc)).perform()
            self.logger.info("按住鼠标左键成功")
        except Exception as e:
            self.logger.error("按住鼠标左键失败")
            #raise e
    def release(self,loc):
        self.logger.info("正在准备释放鼠标左键")
        try:
            ActionChains(self.driver).release(self.find_element(loc)).perform()
            self.logger.info("释放鼠标左键成功")
        except Exception as e:
            self.logger.error("释放鼠标左键失败")
            #raise e
    def move_to_element(self,loc):
        self.logger.info("正在准备移动到该元素_{}".format(loc))
        try:
            ActionChains(self.driver).move_to_element(self.find_element(loc)).perform()
            self.logger.info("移动元素成功")
        except Exception as e:
            self.logger.error("移动元素失败")
            #raise e
    def invisibility_of_element_located(self,loc,timeout=30,frequency=1):
        """等待元素不可见"""
        self.logger.info("正在准备等待{}元素不可见".format(loc))
        try:
             timeout = int(timeout)
             frequency =int(frequency)
             WebDriverWait(self.driver,timeout,frequency).until_not(EC.visibility_of_element_located(loc))
             self.logger.info("{}元素不可见成功".format(loc))
        except Exception as e:
             self.logger.error("等待{}元素不可见失败".format(loc))
             #raise e
    def switch_to_frame_by_id_or_name(self,value):
        self.logger.info("正在准备跳转到id或name为_{}_的frame".format(value))
        try:
            self.driver.switch_to.frame(value)
            self.logger.info("跳转到frame成功")
        except Exception as e:
            self.logger.error("跳转到frame失败")
            #raise e

    def switch_to_frame_by_ele(self,loc):
        self.logger.info("正在准备跳转到_{}_的frame".format(loc))
        try:
            self.driver.switch_to.frame(self.find_element(loc))
            self.logger.info("跳转到frame成功")
        except Exception as e:
            self.logger.error("跳转到frame失败")
            #raise e
    def switch_to_default_context(self):
        self.logger.info("正在准备跳出iframe")
        try:
            self.driver.switch_to.default_context()
            self.logger.info("返回主界面成功")
        except Exception as e:
            self.logger.error("返回主界面失败")
            #raise e
    def get_attribute(self,loc,name):
        self.logger.info("正在准备获取元素_{}_的{}的值".format(loc,name))
        try:
            value = self.find_element(loc).get_attribute(name)
            self.logger.info("取元素_{}_的{}的值成功为_{}".format(loc,name,value))
            return value
        except Exception as e:
            self.logger.error("获取元素属性值失败")
            #raise e
    def test_screenshot_png(self,filename):
        self.logger.info("正在准备截图")
        try:
            self.driver.get_screenshot_as_file(filename)
            self.logger.info("截图成功")
        except Exception as e:
            self.logger.error("截图失败")
            #raise e
    def get_register_name(self):
        self.logger.info("正在准备创建注册用户名")
        try:
           name = "zqc_test_" + str(random.randint(0,100000))
           self.logger.info("创建用户名成功为_{}".format(name))
           return  name
        except Exception as e:
            self.logger.error("创建用户名失败")
            #raise e
    def get_mobile_phone(self):
        self.logger.info("正在准备创建手机号")
        try:
            mobile = "182"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
            self.logger.info("创建手机号成功为_{}".format(mobile))
            return mobile
        except Exception as e:
            self.logger.error("创建手机号失败")
            #raise e
    def scrollBy(self,y):
        self.logger.info("正在准备竖着移动滚动条移动量为_{}".format(y))
        try:
            y = int(y)
            self.driver.execute_script("window.scrollBy(0,{});".format(y))
            self.logger.info("竖着移动滚动条成功移动量为_{}".format(y))
        except Exception as e:
            self.logger.error("竖着移动滚动条失败")
            raise  e
    def sleep(self,s):
        self.logger.info("正在准备强制等待_{}秒".format(s))
        try:
            s= int(s)
            time.sleep(s)
            self.logger.info("强制等待_{}秒_成功".format(s))
        except Exception as e:
            self.logger.error("强制等待失败")
            #raise e

    def back_method_dict(self):
        return {
        "get_window_position":self.get_window_position,"set_window_position":self.set_window_position,
        "get_window_size":self.get_window_size,"set_window_size":self.set_window_size,
        "title":self.title,"get_page_source":self.get_page_source,
        "get_current_url":self.get_current_url,"alter_is_present":self.alter_is_present,
        "click_by_object":self.click_by_object,"click_elements_for_one":self.click_elements_for_one,
        "click_element":self.click_element,"clear":self.clear,
        "back":self.back,"forward":self.forward,
        "accept_or_dismiss_alter":self.accept_or_dismiss_alter,"find_element":self.find_element,
        "find_elements_back_length":self.find_elements_back_length,"find_elements_back_object":self.find_elements_back_object,
        "find_elements_back_objects":self.find_elements_back_objects,"get":self.get,
        "text":self.text,"refresh":self.refresh,
        "send_keys":self.send_keys,"scroll_into_view":self.scroll_into_view,
        "select_by_value":self.select_by_value,"sql_search_one":self.sql_search_one,
        "title":self.title,"presence_of_element_located":self.presence_of_element_located,
        "visibility_of_element_located":self.visibility_of_element_located,"double_click":self.double_click,
        "select_by_visible_text":self.select_by_visible_text,"select_by_index":self.select_by_index,
        "get_select_text":self.get_select_text,"set_clipboard_data":self.set_clipboard_data,
        "ctrl_c":self.ctrl_c,"enter":self.enter,"context_click":self.context_click,
        "click_and_hold":self.click_and_hold,"release":self.release,
        "invisibility_of_element_located":self.invisibility_of_element_located,
        "switch_to_frame_by_id_or_name":self.switch_to_frame_by_id_or_name,"switch_to_frame_by_ele":self.switch_to_frame_by_ele,
        "switch_to_default_context":self.switch_to_default_context,"get_attribute":self.get_attribute,
        "test_screenshot_png":self.test_screenshot_png,"get_register_name":self.get_register_name,
        "get_mobile_phone":self.get_mobile_phone,"scrollBy":self.scrollBy,
        "sleep":self.sleep
    }
    # def cutting(self,file_path):
    #     logger.info("正在准备剪切本地路径为:{}的图片".format(file_path))
    #     try:
    #         w.OpenClipboard()
    #         w.EmptyClipboard()
    #         w.SetClipboardData(win32con.CF_UNICODETEXT,file_path)
    #         w.CloseClipboard()
    #         time.sleep(2)
    #         logger.info("剪切本地路径{}图片成功".format(file_path))
    #     except:
    #         logger.error("本地路径为:{}的图片上传失败".format(file_path))
    # def upload_image(self):
    #     logger.info("正在准备打开图片")
    #     try:
    #         VK_CODE = {
    #            "ctrl": 0x11,
    #            "v": 0x56,
    #            "enter": 0x0D,
    #          }
    #         win32api.keybd_event(VK_CODE["ctrl"],0,0,0)
    #         win32api.keybd_event(VK_CODE["v"], 0, 0, 0)
    #         win32api.keybd_event(VK_CODE["ctrl"], 0, win32con.KEYEVENTF_KEYUP, 0)
    #         win32api.keybd_event(VK_CODE["v"], 0, win32con.KEYEVENTF_KEYUP, 0)
    #         win32api.keybd_event(VK_CODE["enter"], 0, 0, 0)
    #         win32api.keybd_event(VK_CODE["enter"], 0, win32con.KEYEVENTF_KEYUP, 0)
    #         time.sleep(2)
    #         logger.info("图片打开成功")
    #     except:
    #         logger.error("图片打开失败")
    #

    # def get_ele_sreenshot(self,loc,filename):
    #     logger.info("正在准备对{}元素对象进行截屏操作")
    #     try:
    #         self.find_element(loc).screenshot(os.path.join(ele_screenshot_path,filename))
    #         logger.info("{}元素对象截屏成功,并命名为{}".format(loc,filename))
    #     except:
    #         logger.error("{}元素对象截屏失败".format(loc))
    # def get_ele_sreenshot_by_ele(self,ele,filename):
    #     logger.info("正在准备对{}元素对象进行截屏操作")
    #     try:
    #         ele.screenshot(os.path.join(ele_screenshot_path,filename))
    #         logger.info("{}元素对象截屏成功,并命名为{}".format(ele,filename))
    #     except:
    #         logger.error("{}元素对象截屏失败".format(ele))
if __name__ == '__main__':
    base =BasePage("driver","test.log")
    a=inspect.getfullargspec(base.get_url)
    print(len(a.args))
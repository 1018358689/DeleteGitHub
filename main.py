#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pprint import pprint
import pickle
import time

with open('project_name', 'r') as f:
    pro_names = f.read().split('\n')

login_url = 'https://github.com/login'
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap['phantomjs.page.settings.userAgent'] = (ua)
# driver = webdriver.PhantomJS(desired_capabilities=dcap)


options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="{}"'.format(ua))
driver = webdriver.Chrome(chrome_options=options)

# user_name = input('user_name: ')
# email = input('email: ')
# password = input('password: ')

user_name = '1018358689'

# 获取cooks
# driver.get(login_url)
# driver.find_element_by_id('login_field').send_keys(email)
# driver.find_element_by_id('password').send_keys(password)
# driver.find_element_by_name('commit').click()
# cookies = driver.get_cookies()
# pprint(cookies)
# pickle.dump(cookies,open("cookies.pkl", "wb"))

# 调用cookies
url = 'https://github.com/'
cookies2 = pickle.load(open("cookies.pkl", "rb"))

driver.get(url)
for cookie in cookies2:
    driver.add_cookie(cookie)
# driver.implicitly_wait(55)
for pro_name in pro_names:
    try:
        res_url = 'https://github.com/{}/{}/settings'.format(user_name, pro_name)
        driver.get(res_url)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//div[@class="Box Box--danger"]/ul/li[last()]/button').click()
        driver.find_element_by_xpath('(//input[@class="form-control input-block"])[last()]').send_keys(pro_name)
        # forms[len(forms)-1].send_keys('python_dt')
        driver.find_elements_by_xpath('//button[@class="btn btn-block btn-danger"]')[-1].click()
    except:
        pass
driver.quit()

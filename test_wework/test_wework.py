import pytest
from appium import webdriver
from time import sleep

class TestWeWork():
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_men(self):
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"b78") and @index="2"]').send_keys("laowang")
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"b8_") and @class="android.widget.RelativeLayout"]').click()
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"elq") and @text="男"]').click()
        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys("1234567890123")
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()

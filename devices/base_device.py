from selenium.webdriver.support.ui import WebDriverWait

class BaseDevice:
    def __init__(self, driver, wait: WebDriverWait, config):
        self.driver = driver
        self.wait = wait
        self.config = config

    def login(self):
        """子類別必須實作登入邏輯"""
        raise NotImplementedError("請實作 login 方法")

    def logout(self):
        """子類別必須實作登出邏輯"""
        raise NotImplementedError("請實作 logout 方法")

    def run_action(self):
        """可選：如果某些設備有特殊動作（如更新韌體）可在此定義"""
        pass
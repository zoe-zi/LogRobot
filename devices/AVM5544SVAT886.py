from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from .base_device import BaseDevice
import time

class AVM5544(BaseDevice):
    def login(self):
        # 移轉原本的登入邏輯
        user_field = self.wait.until(EC.presence_of_element_located((By.NAME, "Username")))
        user_field.send_keys(self.config.USER)
        
        pass_field = self.driver.find_element(By.NAME, "Password")
        pass_field.send_keys(self.config.PWD)
        pass_field.send_keys(Keys.ENTER)

    def logout(self):
        # 移轉原本的登出邏輯
        logout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='登出']")))
        logout_btn.click()
        time.sleep(0.5)
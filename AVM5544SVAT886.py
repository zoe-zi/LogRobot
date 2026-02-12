from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 基礎設定：處理內網 SSL 警告
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
# 如果不想看視窗一直跳，可以考慮加上這一行開啟「無頭模式」
# chrome_options.add_argument('--headless') 

# 2. 初始化瀏覽器
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

target_url = "https://172.31.0.38/"
total_loops = 500

try:
    for i in range(1, total_loops + 1):
        print(f"正在執行第 {i} / {total_loops} 次登入...")
        
        # 開啟網站
        driver.get(target_url)
        
        # 執行登入 
        # 等待帳號欄位出現
        user_field = wait.until(EC.presence_of_element_located((By.NAME, "Username")))
        user_field.clear() # 清除欄位確保乾淨
        user_field.send_keys("admin1234")
        
        # 輸入密碼並按 Enter
        pass_field = driver.find_element(By.NAME, "Password")
        pass_field.clear()
        pass_field.send_keys("P@ss1234")
        pass_field.send_keys(Keys.ENTER)
        
        # 稍微等一下頁面跳轉完成
        time.sleep(1) 
        
        # 執行登出 
        # 使用文字定位 '登出' 標籤
        logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='登出']")))
        logout_btn.click()
        
        print(f"第 {i} 次循環完成。")
        
        # 循環間的小緩衝，避免設備反應不過來 (可視情況縮短)
        time.sleep(0.5)

    print("\n--- 500 次測試已全數完成 ---")

except Exception as e:
    print(f"\n程式在第 {i} 次時發生中斷。")
    print(f"錯誤訊息: {e}")

finally:
    # 測試結束後關閉瀏覽器
    driver.quit()
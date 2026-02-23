import time
from driver_factory import create_driver
from config import Config
from devices.AVM5544SVAT886 import AVM5544
from devices.NIB4823_E import NIB4823_E

def start_logging_test(device_class, iterations=10):
    """
    這是一個『動態流程引擎』
    傳入 Class 名稱，它會自動決定要用哪種循環方式
    """
    
    # 判斷一：如果是 NIB 這種 HTTP Auth 設備，必須每回重啟
    if device_class.__name__ == "NIB4823_E":
        for i in range(1, iterations + 1):
            print(f"[{device_class.__name__}] 第 {i} 次獨立循環（重啟瀏覽器清快取）")
            driver, wait = create_driver() # 每一輪都重新開啟瀏覽器
            try:
                device_instance = device_class(driver, wait, Config)
                device_instance.login()
                time.sleep(1) # 讓 Log 產生的等待時間
            finally:
                driver.quit() # 徹底關掉，清空記憶體
                time.sleep(0.5)
                
    # 判斷二：如果是 AVM 等一般網頁登入設備，可以用快速循環
    else:
        driver, wait = create_driver() # 只開一次瀏覽器
        device_instance = device_class(driver, wait, Config)
        try:
            for i in range(1, iterations + 1):
                print(f"[{device_class.__name__}] 第 {i} 次快速循環...")
                device_instance.driver.get(Config.URL)
                device_instance.login()
                time.sleep(1)
                device_instance.logout()
        finally:
            driver.quit()

if __name__ == "__main__":
    # --- 關鍵：你只要改這裡傳進去的類別名稱就好NIB4823_E ---
    # 想測 NIB 就傳 NIB4823_E
    # 想測 AVM 就傳 AVM5544
    start_logging_test(NIB4823_E, iterations=Config.TOTAL_LOOPS)
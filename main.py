import time
from driver_factory import create_driver
from config import Config
from devices.AVM5544SVAT886 import AVM5544
# 如果以後有新設備：from devices.router_abc import RouterABC

def start_logging_test(device_instance, iterations=500):
    """
    通用執行引擎：它不在乎是哪台設備，只要該設備有 login/logout 即可。
    """
    try:
        for i in range(1, iterations + 1):
            print(f"[{type(device_instance).__name__}] 執行第 {i} 次循環...")
            device_instance.driver.get(Config.URL)
            
            device_instance.login()
            time.sleep(1) # 成功登入後讓系統產生 log
            
            device_instance.logout()
            
    except Exception as e:
        print(f"測試中斷！錯誤原因：{e}")
    finally:
        device_instance.driver.quit()

if __name__ == "__main__":
    # 初始化環境
    driver, wait = create_driver()
    
    # --- 在這裡決定你要執行哪台設備 ---
    # 只需要把 AVM5544 換成其他設備 Class 即可切換
    target_device = AVM5544(driver, wait, Config)
    
    # 開始執行
    start_logging_test(target_device, iterations=500)
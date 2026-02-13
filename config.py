class Config:
    # 設備登入網址
    URL = "http://192.168.1.1"  # 換成你設備的 IP 或網址
    
    # 登入憑證
    USER = "admin"
    PWD = "your_password_here"
    
    # 測試設定
    TOTAL_LOOPS = 500
    WAIT_TIME = 10  # Selenium 等待元素出現的最長時間（秒）
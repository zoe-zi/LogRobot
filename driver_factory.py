from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager # 建議安裝此套件自動管理 driver

def create_driver():
    chrome_options = Options()
    
    # 常用專業設定
    chrome_options.add_argument("--incognito") # 強制開啟無痕模式
    chrome_options.add_argument("--start-maximized") # 視窗最大化
    chrome_options.add_experimental_option("detach", True) # 程式跑完不關閉瀏覽器(除錯用)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation']) # 隱藏自動化控制條
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    
    # 如果之後要跑無介面模式，取消下面註解即可
    # chrome_options.add_argument("--headless") 

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # 統一設定隱式等待或 Explicit Wait 的實例
    wait = WebDriverWait(driver, 15) 
    
    return driver, wait
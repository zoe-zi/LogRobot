# Device Logging Automation Tool

## 專案簡介

本專案是一個基於 Selenium 的自動化工具，旨在解決不同設備（如 AVM5544）需要反覆登入以產生系統 Log 的需求。透過模組化設計，讓測試腳本更易於維護與擴充。

## 安裝與執行

1. **環境需求**：確保已安裝 Python 3.x。

2. **安裝必要套件**：
   本專案使用 `webdriver-manager` 實現 Driver 自動化管理，無需手動下載 chromedriver。執行前請先在終端機執行：

   ```bash
   pip install -r requirements.txt
   設定參數：請於 config.py 中設定設備的 URL、帳號與密碼。

   ```

3. **執行程式**：
   python main.py

4. **架構說明**：

- 模組化設計：將設備操作（Devices）、環境配置（Config）與瀏覽器驅動（Driver Factory）完全分離。
- 高擴展性：採用策略模式思想，支援不同設備的登入流程切換。
- 自動化驅動管理：整合 webdriver-manager，解決 Chrome 瀏覽器版本不相容問題。

5. **如何新增設備**：
   5.1. 在 devices/ 目錄下建立新的類別。
   5.2. 繼承 BaseDevice 並實作專屬的 login 與 logout 方法。
   5.3. 在 main.py 中修改實例化的對象，例如：
   target_device = NewDevice(driver, wait, Config)

6. **檔案結構**：
   main.py: 執行入口，負責串接設備邏輯與循環控制
   config.py: 存放變動資訊（IP、帳密）
   driver_factory.py: 負責瀏覽器啟動與 WebDriver 管理
   devices/: 存放各個不同設備的實作類別

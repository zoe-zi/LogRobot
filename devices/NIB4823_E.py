from .base_device import BaseDevice
from urllib.parse import urlparse

class NIB4823_E(BaseDevice):
    def login(self):
        # 使用 urlparse 自動拆解網址，這比 replace 安全 100 倍
        parsed_url = urlparse(self.config.URL)
        
        # 取得協議 (http 或 https)
        scheme = parsed_url.scheme if parsed_url.scheme else "https"
        
        # 取得不含協議的位址 (例如 172.31.0.75)
        netloc = parsed_url.netloc if parsed_url.netloc else parsed_url.path
        
        # 組合出正確的 Auth URL 格式：https://user:pwd@172.31.0.75
        auth_url = f"{scheme}://{self.config.USER}:{self.config.PWD}@{netloc}"
        
        print(f"正在連線至: {scheme}://{netloc} (使用 HTTP Auth)")
        self.driver.get(auth_url)

    def logout(self):
        # 留空，因為這台設備是靠關閉瀏覽器來登出的
        pass
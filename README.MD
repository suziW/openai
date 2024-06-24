# proxy 大法

1. 修改 \_base_client.y BaseClient 类的 \_proxies 属性，356 行
   `self._proxies = {'http': 'http://localhost:7890','https': 'http://localhost:7890'}`
2. 文件开头添加
   `os.environ["http_proxy"] = "http://localhost:7890"`
   `os.environ["https_proxy"] = "http://localhost:7890"`

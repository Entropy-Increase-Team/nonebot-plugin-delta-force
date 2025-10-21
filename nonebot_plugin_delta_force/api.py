'''
api数据对接

'''


import httpx


class DeltaForceAPI:
    BASE_URL = "https://df-api.shallow.ink/df"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def _init__api_names(self):
        '''
        api定义
        '''
        self.get_qq_qr_login = "/login/qq/qr"
        self.get_wx_qr_login = "/login/wx/qr"
        # 轮询扫码状态
        self.get_scan_status = "/login/scan/status"
        ...  # 其他API路径定义,先做框架，后面补充


    # api 调用框架
    async def DeltaForceAPI_use_demo(self, api: str) -> dict:

        '''
        API 调用示例

        api: str API路径，例如 /login/qq/qr
        '''

        url = f"{self.BASE_URL}+{api}"
        async with httpx.AsyncClient(timeout=20.0) as client:
            r = await client.get(url, headers=self.headers)
            r.raise_for_status()
            return r.json()



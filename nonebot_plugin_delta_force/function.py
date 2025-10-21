# from . import DeltaForceAPI, Delta_Force_API_KEY, logger
from .api import DeltaForceAPI
from .config import Delta_Force_API_KEY



'''
command 具体功能实现

'''

DFApi = DeltaForceAPI(Delta_Force_API_KEY)

# api使用实例
"""

通用api框架，三角洲QQ扫码登录示例


async def delta_qq_scan_logindemo():

    logindata = await DFApi.DeltaForceAPI_use_demo(DFApi.get_qq_qr_login)

    return logindata
    
"""

# 三角洲帮助
async def delta_help(bot):
    '''
    用于返回功能清单，使用 无头浏览器渲染截图
    '''
    await bot.call_api("send_private_msg", user_id=417148909, message="三角洲帮助功能待定")
    # logger.info("三角洲帮助功能待定")
    pass

# 三角洲QQ扫码登录
async def delta_qq_scan_login(bot):

    pass

# 三角洲微信扫码登录
async def delta_wx_scan_login(bot):

    pass

# 三角洲QQ授权登录
async def delta_qq_oauth_login(bot):

    pass
# 三角洲微信授权登录
async def delta_wx_oauth_login(bot):

    pass

# 三角洲cookie登录
async def delta_cookie_login(bot):

    pass


# 三角洲QQ令牌刷新
async def delta_qq_refresh_token(bot):

    pass

# 三角洲微信令牌刷新
async def delta_wx_refresh_token(bot):

    pass

... # 其他功能函数
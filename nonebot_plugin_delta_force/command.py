'''

存放所有用户可以调用的指令


'''
from nonebot import on_command
from nonebot.internal.adapter import Bot

from .rule import * # 通用规则，目前还不知道要什么规则，先占位

from .function import(
    delta_help,
    delta_qq_scan_login,
    delta_wx_scan_login,
    delta_qq_oauth_login,
    delta_wx_oauth_login,
    delta_cookie_login,
    delta_qq_refresh_token,
    delta_wx_refresh_token
)



bind_df_help = on_command("三角洲帮助")

bind_df_login = on_command("三角洲登录")

bind_df_player_info = on_command("三角洲信息")
bind_df_password = on_command("三角洲密码")
bind_df_safehouse = on_command("三角洲特勤处")
bind_df_safehouse_remind_open_close = on_command("三角洲特勤处提醒")
bind_df_daily_report = on_command("三角洲日报")
bind_df_weekly_report = on_command("三角洲周报")
bind_df_ai_comment = on_command("三角洲AI锐评", aliases={"三角洲ai锐评"})
bind_df_get_record = on_command("三角洲战绩")
bind_df_broadcast_record_open_close = on_command("三角洲战绩播报")


# 响应处理

'''
在尝试更简化的调用方式
'''

@bind_df_help.handle()
async def _(bot: Bot):
    await delta_help(bot)
    # logger.info("已执行三角洲帮助指令")

... # 其他指令响应处理类似，后续补充
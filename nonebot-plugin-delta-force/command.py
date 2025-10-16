'''

存放所有用户可以调用的指令


'''

from nonebot import on_command

bind_df_help = on_command("三角洲帮助")
bind_df_login = on_command("三角洲登录")

'''
分 qq和微信扫码 手动cookie登录 ，记得设置额外指令   cookie登录记得设计帮助信息 

还要wegame的qq微信登录，已经安全中心登录
'''

bind_df_player_info = on_command("三角洲信息")
bind_df_password = on_command("三角洲密码")
bind_df_safehouse = on_command("三角洲特勤处")
bind_df_safehouse_remind_open_close = on_command("三角洲特勤处提醒")
bind_df_daily_report = on_command("三角洲日报")
bind_df_weekly_report = on_command("三角洲周报")
bind_df_ai_comment = on_command("三角洲AI锐评", aliases={"三角洲ai锐评"})
bind_df_get_record = on_command("三角洲战绩")
bind_df_broadcast_record_open_close = on_command("三角洲战绩播报")

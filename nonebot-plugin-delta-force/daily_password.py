import httpx
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent, PrivateMessageEvent, MessageSegment
from nonebot.log import logger

API_URL = "https://df-api.shallow.ink/df/tools/dailykeyword"
API_KEY = "sk-3K2vYMC8y7EsJOKZIvsDHCPl8foidy3i"

daily_password = on_message(priority=3, block=True)

@daily_password.handle()
async def handle(bot: Bot, event: MessageEvent):
    msg = str(event.get_message()).strip()
    if msg not in ["#三角洲每日密码", "^每日密码"]:
        return

    try:
        text = await fetch_daily_password()
        reply = MessageSegment.reply(event.message_id) + (f"今日三角洲密码：\n{text}" if text else "获取每日密码失败，请稍后重试")
        await send(bot, event, reply)
    except Exception as e:
        logger.error(f"每日密码处理出错: {e}")
        await send(bot, event, MessageSegment.reply(event.message_id) + "发生错误，请稍后重试")

async def fetch_daily_password():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    async with httpx.AsyncClient(timeout=20.0) as client:
        r = await client.get(API_URL, headers=headers)
        if not r.is_success:
            return None
        data = r.json()
        if not data.get("success"):
            return None

        lst = data.get("data", {}).get("list", [])
        return "\n".join(f"{i.get('mapName', '未知地图')} - {i.get('secret', '未知')}" for i in lst) if lst else None

async def send(bot: Bot, event: MessageEvent, msg):
    try:
        if isinstance(event, GroupMessageEvent):
            await bot.send_group_msg(group_id=event.group_id, message=msg)
        elif isinstance(event, PrivateMessageEvent):
            await bot.send_private_msg(user_id=event.user_id, message=msg)
    except Exception as e:
        logger.error(f"发送消息失败: {e}")
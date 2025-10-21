'''
用于管理敏感配置项

这里改为从环境变量中获取

在.env 或者 .env.{ENVIRONMENT} 中添加配置项

Delta_Force_API_KEY="your_api_key_here"


'''

import logging

import nonebot

config = nonebot.get_driver().config

Delta_Force_API_KEY = config.delta_force_api_key

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"apikey为 : {Delta_Force_API_KEY}")


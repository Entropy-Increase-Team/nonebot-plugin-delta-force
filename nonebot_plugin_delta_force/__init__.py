from .command import *



import logging
# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# from nonebot.plugin import PluginMetadata, inherit_supported_adapters
# # nonebot 插件元信息
# __plugin_name__ = "Delta Force"
# __plugin_version__ = "0.1.0"
# __plugin_author__ = "Your Name"
# __plugin_description__ = "A plugin that provides Delta Force functionalities."



# __plugin_meta__ = PluginMetadata(
#     name="三角洲助手",
#     description="描述-待定",
#     usage="使用方式-待定",

#     type="application",
#     # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

#     homepage="https://github.com/BraveCowardp/nonebot-plugin-delta-helper",
#     # 发布必填。

#     # config=Config,
#     # 插件配置项类，如无需配置可不填写。

#     supported_adapters=inherit_supported_adapters("nonebot_plugin_saa"),
#     # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
#     # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。

# )










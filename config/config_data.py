from dotenv import load_dotenv
from os import getenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class TelegramBot:
    bot_token: str


@dataclass
class ConfigData:
    tg_bot: TelegramBot


def load_config() -> ConfigData:
    return ConfigData(
        tg_bot=TelegramBot(
            bot_token=getenv('BOT_TOKEN')
        )
    )

Config = load_config()

__all__ = (
    'Config',
)
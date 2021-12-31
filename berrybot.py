
import asyncio
import os
import logging as log

from config import Config
from messenger import COMMAND_SMS, Telegram
from phone import Phone


class BerryBot:

    def __init__(self, config_path: str) -> None:
        self.config = Config(config_path)
        self.messenger = Telegram(self.config)
        self.timer = asyncio.get_event_loop().time

    def send_sms(self, number, message):
        log.debug(f"Sending message: {number} {message}")
        phone = Phone()
        phone.send_sms(number, message)

    def check_telegram(self):
        for cmd in self.messenger.get_commands():
            if cmd.command == COMMAND_SMS:
                self.send_sms(cmd.data['recipient'], cmd.data['txt'])

    def check_sms():
        pass

    async def run(self):
        interval = 10
        while True:
            await asyncio.sleep(interval - self.timer() % interval)
            self.check_telegram()

if __name__ == "__main__":
    LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
    log.basicConfig(level=LOGLEVEL)

    berrybot = BerryBot("./config.yaml")
    asyncio.run(berrybot.run())
        
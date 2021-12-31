

from typing import List
from config import Config
import telegram
import logging as log

COMMAND_SMS = 1

class Message:

    def __init__(self, command: int, data: dict) -> None:
        self.command = command
        self.data = data

class Telegram:

    def __init__(self, config: Config) -> None:
        self.bot = telegram.Bot(token=config.telegram_token)
        self.offset = 0

    def updates(self):
        try:
            messages = self.bot.get_updates(offset=self.offset)
        except Exception as e:
            log.error(e)
            messages = []
        if messages:
            self.offset = messages[-1]['update_id'] + 1
        return messages

    def send(self, chat_id, message):
        self.bot.send_message(chat_id=chat_id, text=message)

    def get_commands(self) -> List[Message]:
        messages = []
        for message in self.updates():
            if '/sms' in message['message']['text']:
                parts = message['message']['text'].split('\n')
                command_data = {
                    'recipient': parts[1],
                    'txt': parts[2] 
                }
                messages.append(Message(COMMAND_SMS, command_data))
            else:
                log.debug(message['message']['text'])
        return messages

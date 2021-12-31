import yaml

class Config:

    def __init__(self, path: str) -> None:
        with open(path, 'r') as _f:
            config = yaml.safe_load(_f)
        self.telegram_token = config['telegram']['token']
        self.chat_id = config['telegram']['chat']['id']
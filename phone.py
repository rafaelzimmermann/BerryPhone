import gammu
import logging as log

class Phone:

    def __init__(self):
        self.sm = gammu.StateMachine()
        # Read ~/.gammurc
        self.sm.ReadConfig()
        self.sm.Init()
        self.print_status()

    def send_sms(self, recipient: str, message: str):
        smsinfo = {
            "Class": -1,
            "Unicode": False,
            "Entries": [
                {
                    "ID": "ConcatenatedTextLong",
                    "Buffer": message,
                }
            ],
        }
        encoded = gammu.EncodeSMS(smsinfo)

        # Send messages
        for message in encoded:
            # Fill in numbers
            message["SMSC"] = {"Location": 1}
            message["Number"] = recipient

            # Actually send the message
            self.sm.SendSMS(message)
    
    def print_status(self):
        netinfo = self.sm.GetNetworkInfo()

        log.info(f"Network name: {netinfo['NetworkName']}") 
        log.info(f"Network code: {netinfo['NetworkCode']}")
        log.info(f"LAC: {netinfo['LAC']}")
        log.info(f"CID: {netinfo['CID']}")
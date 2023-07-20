# Original: https://github.com/JeremyRuhland/klipper_network_status
import os, logging

class network_status:
    def __init__(self, config):
        self.interval = config.getint('interval', 60, minval=10)
        self.intethname = config.get('intethname', 'eth0')
        self.intwifiname = config.get('intwifiname','wlan0')
        self.ethip = "N/A"
        self.wifiip = "N/A"
        self.wifissid = "N/A"
        self.mdns = "N/A"
        self.last_eventtime = 0

    def get_status(self, eventtime):
        if eventtime - self.last_eventtime > self.interval:
            self.last_eventtime = eventtime
            logging.info("network_status get_status %d" % eventtime)
            try:
                self.ethip = os.popen("ip addr show %s" % self.intethname).read().split("inet ")[1].split("/")[0]
            except:
                self.ethip = "N/A"

            try:
                self.wifiip = os.popen("ip addr show %s" % self.intwifiname).read().split("inet ")[1].split("/")[0]
                self.wifissid = os.popen('iwgetid -r').read()[:-1]
            except:
                self.wifiip = "N/A"
                self.wifissid = "N/A"

            self.mdns = os.popen('hostname').read()[:-1] + '.local'

        return {'ethip': self.ethip,
            'wifiip': self.wifiip,
            'wifissid': self.wifissid,
            'mdns': self.mdns}

def load_config(config):
    return network_status(config)

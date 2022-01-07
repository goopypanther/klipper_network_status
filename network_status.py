import os

class network_status:
	def __init__(self, config):
		self.ethip = "N/A"
		self.wifiip = "N/A"
		self.wifissid = "N/A"
		self.mdns = "N/A"

	def get_status(self, eventtime):
		try:
		    self.ethip = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
		except:
		    self.ethip = "N/A"
	    
	    try:
            self.wifiip = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
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

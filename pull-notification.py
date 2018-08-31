# python 2.7.x
import time
from datetime import datetime
from time import sleep
from mbed_cloud import ConnectAPI

connect_api = ConnectAPI()

device_id = "<< Your Device ID >>"

start_time = time.time()
period = 5

while True:
  now = datetime.now().strftime("%H:%M:%S")
  resource_value = connect_api.get_resource_value(device_id, "/3200/0/5501")
  print(now + ' btn=' + resource_value)
  time.sleep(period - ((time.time() - start_time) % period))



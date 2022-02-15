import time
from datetime import datetime
import pandas
import numpy
import matplotlib.pyplot as plt
import os
from mail import Messenger
import sys


system = 'Unknown' if len(sys.argv) < 2 else sys.argv[1]
report_path = f'{os.path.dirname(os.path.realpath(__file__))}/data/report.csv'

try:
    import httplib
except:
    import http.client as httplib

def is_connected():
    conn = httplib.HTTPConnection("www.google.com", timeout=1)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return 1
    except:
        conn.close()
        return 0

if os.path.exists(report_path):
    df = pandas.read_csv(report_path)
else:
    df = pandas.DataFrame(columns=['Time', 'Status'])

format = '%m/%d/%y %H:%M:%S'
was_connected = not is_connected()


messenger = Messenger()
if is_connected():
    messenger.send(f"{system}'s wifi monitor online")

while True: 
    date = time.localtime(time.time())
    connected = is_connected()
    now = datetime.now().strftime(format)
    message = f"{system}'s wifi is {'up' if connected else 'down'} | {now}"
    if not connected and was_connected:
        print(message)
        df = df.append( { 'Time': datetime.now().strftime(format), 'Status': 'down' }, ignore_index=True)
        df.to_csv(report_path, index=False)
    if connected and not was_connected:
        print(message)
        messenger.send(message)
        df = df.append( { 'Time': datetime.now().strftime(format), 'Status': 'up'}, ignore_index=True)
        df.to_csv(report_path, index=False)
    was_connected = connected
    time.sleep(1)

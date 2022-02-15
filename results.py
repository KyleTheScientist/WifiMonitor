import time
from datetime import datetime
import pandas
import numpy
import matplotlib.pyplot as plt

# plt.style.use('ggplot')
df = pandas.read_csv('data/report.csv', parse_dates=['Time'])
df.replace('down', value=0, inplace=True)
df.replace('up', value=1, inplace=True)
df['Time'] = pandas.to_datetime(df['Time'])
df = df.set_index('Time')
new_index = pandas.date_range(start=df.index[0], end=df.index[-1], freq='1s')
df = df.reindex(new_index.sort_values()).ffill()
df.plot()
plt.show()





down_duration = df['Status'].value_counts()[0]
down_minutes,seconds = divmod(down_duration, 60)

total_duration = len(df)
total_days  = int(divmod(total_duration, 86400)[0]) 
total_hours = int(divmod(total_duration, 3600)[0]) % 24
total_minutes = int(divmod(total_duration, 60)[0]) % 60


print(f"Total WiFi downtime: {int(down_minutes)} minute(s), or {int(down_duration/total_duration * 100)}%")
print(f"Total time elapsed: {total_days} days, {total_hours} hours, {total_minutes} minutes")
import serial
import matplotlib.pyplot as plt
import numpy as np
import time
import Read_and_Write as RaW
from datetime import datetime

plt.figure(figsize=(16, 4))
plt.ion()
plt.show()

data = np.array([])
time_stamp = np.array([])
time_at_start = float(time.time() % (24 * 3600))

txt_log = 'log_data_0.txt'
folder_name = '_Log_data_texts'
text_log_path = RaW.GetPathOfText(folder_name,txt_log)

while True:
    content = RaW.ReadFromSerialCom('COM1',2)
    #content = serial_com.readline()
    #content.decode()
    try:
        formatted_content = float(content[0:8])
    except ValueError:
        print("Done plotting!")
        break
    print(formatted_content)
    current_time = float(time.time() % (24 * 3600)) - time_at_start
    data = np.append(data, formatted_content)
    time_stamp = np.append(time_stamp,current_time)
    plt.cla()
    plt.xlim(left=0, right=100)
    plt.ylim(bottom=0, top=10)
    plt.plot(data[-100:])

    plt.pause(0.0125)                                                #Adjust this base on your device's spec so it's sync as much as possible
plt.close()
RaW.NewFolder(folder_name)

with open(text_log_path, 'a') as file:
    file.write("Run at {0}\n".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    file.write("=========\n")
    file.write("Time (s) |  Value\n")

    for index in range (0,len(data)):
        file.write("{0:<9.2f}|  {1:.4f}\n".format(time_stamp[index],data[index]))

print("Text log {0} created!".format(text_log_path))

exit()


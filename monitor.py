import socket
import os

os.system('ifconfig wlan0 down')
os.system('iwconfig wlan0 mode monitor')
os.system('ifconfig wlan0 up')
s=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
print s.recvfrom(65565)

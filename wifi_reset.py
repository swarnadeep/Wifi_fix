import os

import time


# os.system("netsh interface show interface")


def enable():
    os.system("netsh interface set interface 'Wi-Fi' enabled")


def disable():
    os.system("netsh interface set interface 'Wi-Fi' disabled")


hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

while True:
    print("This prints once 15 seconds.")
    time.sleep(15)  # Delay for 15 seconds.
    if response != 0:
        print("now wifi will turn off")
        disable()
        print("now wifi will turn on")
        enable()
        time.sleep(60)  # Delay for 1 minute
    else:
        print("wifi working fine")
        time.sleep(15)  # Delay for 15 seconds.

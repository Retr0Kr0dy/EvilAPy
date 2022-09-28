import subprocess, re, csv, sys, os, time, shutil, argparse

active_wireless_networks = []


def check_for_essid(essid, lst):

    check_status = True

    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status


def get_AP(hacknic):

    discover_access_points = subprocess.Popen(["sudo", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:

        while True:
            subprocess.call("clear", shell=True)

            for file_name in os.listdir():
                    fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']

                    if ".csv" in file_name:
                        with open(file_name) as csv_h:

                            csv_h.seek(0)
                            csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)

                            for row in csv_reader:
                                if row["BSSID"] == "BSSID":
                                    pass
                                elif row["BSSID"] == "Station MAC":
                                    break
                                elif check_for_essid(row["ESSID"], active_wireless_networks):
                                    active_wireless_networks.append(row)

            print("[+] - Scanning. Press Ctrl+C ready.\n")
            print("Index |\tBSSID              |\tESSID                    |")
            print("______|\t___________________|\t_________________________|")

            for index, item in enumerate(active_wireless_networks):
                print(f"{index}\t{item['BSSID']}\t\t{item['ESSID']}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStoping scan.")

    while True:
        choice = input("Select access point : ")
        try:
            if active_wireless_networks[int(choice)]:
                break
        except:
            print("Try again.")
        
    hackbssid = active_wireless_networks[int(choice)]["BSSID"]
    hackchannel = active_wireless_networks[int(choice)]["channel"].strip()

    return hacknic, hackbssid, hackchannel

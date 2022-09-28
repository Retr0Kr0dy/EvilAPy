import os

def GenerateFakeAP(hacknic, hackbssid, hackchannel):
    command = "airbase-ng -e " + hackbssid + " -c " + hackchannel + " " + hacknic
    os.system('gnome-terminal -- ' + command)

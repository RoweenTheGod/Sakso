#!/usr/bin/env python
# -*- coding: utf-8 -*-
#~> TG:@RoweenTheGod
#~> :v RoweenTheFucker
#~> ShellAdamlar
import urllib
import re
import time
from urllib import FancyURLopener

class colors:
        def __init__(self):
                self.green = "\033[92m"
                self.blue = "\033[96m"
                self.bold = "\033[1m"
                self.yellow = "\033[93m"
                self.red = "\033[91m"
                self.end = "\033[0m"
ga = colors()

class UserAgent(FancyURLopener):
	version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'

useragent = UserAgent()

class HTTP_HEADER:
    HOST = "Host"
    SERVER = "Server"

def headers_reader(url):
	print ga.bold+" \n [TARAMA BAŞLADI] ~> "+ ga.end + ga.red+ "TABAN BILGILERI ALINIYOR"+ga.end
	opener = urllib.urlopen(url)
	if opener.code == 200:
		 print ga.green+" ~> DURUM: 200 OK"+ga.end
	if opener.code == 404:
		 print ga.red+"                             [DİKKAT ERROR 404] SAYFA BULUNAMADI TEKRAR DENEYIN ! \n"+ga.end
		 exit()
	#Host = opener.headers.get(HTTP_HEADER.HOST)
	Server = opener.headers.get(HTTP_HEADER.SERVER)
	Host = url.split("/")[2]
	print ga.green+" ~> HOSTNAME: " + str(Host) +ga.end
	print ga.green+" ~> SERVER: " + str(Server) +ga.end
	for item in opener.headers.items():
	    for powered in item:
		sig = "x-powered-by"		
		if sig in item:
		    print ga.green+                        " ~> " + str(powered).strip() + ga.end

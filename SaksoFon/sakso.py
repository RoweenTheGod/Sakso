#!/usr/bin/env python
# -*- coding: utf-8 -*-
#~> TG:@RoweenTheGod
#~> :v RoweenTheFucker
#~> ShellAdamlar
#~>Req python 2.7 lib
import re
import urllib
from serewi import *
from xirremin import *

print ga.yellow+'''          
                               AM ÜSTÜNDE REÇEL BUGÜNLERDE GEÇER . . !
								   '''+ga.end  			
print ga.blue+'''
                                     CODED BY SHELL ADAMLAR

			SPIDER - CREED - DUALITY - MY SPY - HIVRON - ROWEEN
					          '''+ga.end  	
print ga.red+'''         
            *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
           ||	       								      ||
	   || 			S E C U R I T Y    F U C K E R    V 1   	      ||
	   ||							                      ||
           ||                	       H E L L O   W O R L D                          ||
	   ||						                              ||
           ||                           Desteklenen Türler;                           ||
	   ||									      ||
           ||     Remote Code & Command Execution & Evaluation - XSS - SQL Injection  ||
	   ||  			 						      ||
            *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*'''+ga.end 
print ga.bold+'''
			     I L L E G A L  P L A T F O R M  .  O R G
							        '''+ga.end
print ga.green+'''


'''+ga.end


def urls_or_list():
	url_or_list = raw_input("		        |~> TEK URL=1<~| |~>URL LISTE=2<~| SAYI GIRINIZ => ")
	if url_or_list == "1":
	 	 url = raw_input( ga.bold+" Taranacak URL'yi Gir Caz Yapma:"+ga.end)
		 # URL & ("http://"): & balamazsa.
                     #print ga.red+'''\n Hatalı url, url'de http veya https olmalıdır  \"http://\" \n'''+ga.end
                     #exit()
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [HATALI URL GIRDIN !] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" URL'DE DEĞER EKSIK "+ga.end	
			print ga.bold +"\n [ÇÖZÜM :D =>] "+ ga.end + ga.green+"URL BU ŞEKİLDE OLMALIDIR =>" +ga.end + ga.bold +" http://illegalplatform.org/sayfa.php?id=31 "+ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.blue+" URL LİSTESİNİ GİR ÇOK KONUŞMA - ÖRNEK: siteler.txt: "+ga.end)
		 open_list = open(urls_list).readlines()
		 for line in open_list:
			 if "?" in line:
			 	links = line.strip()
		  	 	url = links
		  	 	print ga.green+" \n [TARANIYOR] %s"%url +ga.end
		  	 	rce_func(url)
			 	xss_func(url)
			 	error_based_sqli_func(url)
			 else:
			 	links = line.strip()
		  	 	url = links
				print ga.red +"\n [HATA !] "+ ga.end + ga.yellow+"%s"%url +ga.end + ga.red +" URL'DE DEĞER EKSIK "+ga.end				
				print ga.bold +"\n [ÇÖZÜM :D =>] "+ ga.end + ga.green+"URL BU ŞEKİLDE OLMALIDIR =>" +ga.end + ga.bold +" http://illegalplatform.org/sayfa.php?id=31 "+ga.end
		 exit()				

urls_or_list()






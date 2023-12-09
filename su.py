'''Module'''
import os,urllib2,time,sys
from time import sleep
'''COLOR'''
if sys.platform in ["linux","linux2"]:
	W = ("\033[0m")
	G = ("\033[32;1m")
	R = ("\033[31;1m")
'''Script'''
'''banner'''
banner = (G+" .d8888. d888888b \n 88'  YP `~~88~~' "+R+"Tools : su-Termux\n"+G+" `8bo.      88    "+R+"Version : 1.0\n"+G+"   `Y8b.    88    "+R+"Author : FARHAN-MUH-TASIM\n"+G+" db   8D    88    "+R+"https://github.com/Gtajisan\n"+G+" `8888Y'    YP    ")
def xnchan():
 try:
    print (R+"-----------------------------------------")
    print (banner)
    print (R+"-----------------------------------------")
    print (G+"[+] installing su-termux...\n")
    sleep(3)
    os.system("apt install ncurses-utils")
    sleep(3)
    u = urllib2
    site = ("https://github.com/Gtajisan/Su-Termux/raw/master/su")
    u.Request(site)
    r = u.urlopen(site)
    c = r.read()
    file = open("/data/data/com.termux/files/usr/bin/su","w")
    file.write(c)
    os.chmod("/data/data/com.termux/files/usr/bin/su", 0700)
    print (G+"\n[+] Success install su-termux")
 except:
    print (R+"\n[!] Failed install su-termux")
if __name__ == "__main__":
	xnchan()

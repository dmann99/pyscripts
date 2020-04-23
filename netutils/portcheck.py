#!/usr/bin/python

import socket
import time
import sys

ip=sys.argv[1]
port=sys.argv[2]
retry = 5
delay = 10
timeout = 3

def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

def checkHost(ip, port):
        ipup = False
        for i in range(retry):
                if isOpen(ip, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup

if checkHost(ip, port):
        print ip + " is REACHABLE on port " + str(port)
else:
        print ip + " timeout contacting port " + str(port)

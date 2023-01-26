import socket

def checkport(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(3)
  result = sock.connect_ex((ip,port))
  if result == 0:
    print(ip, port, "Port is open")
  else:
    print(ip, port, "Port NOT Open/Reachable")
  sock.close()



checkport('target.machine.come',22);
checkport('192.168.1.1',1234);

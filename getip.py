
#!/opt/bin/python 
import socket
import psutil
def f():
	hostname=socket.getfqdn(socket.gethostname())
	addr = socket.gethostbyname(hostname)
	return addr



def get_netcard():
	netcard_info = []
	info = psutil.net_if_addrs()
	for k,v in info.items():
		for item in v:
			if item[0] == 2 and not item[1]=='127.0.0.1':
				netcard_info.append((k,item[1]))
	return netcard_info

def get_allip():
	netcard_info = []
	info = psutil.net_if_addrs()
	for k,v in info.items():
		for item in v:
			if item[0] == 2 and not item[1]=='127.0.0.1':
				netcard_info.append(item[1])
	return netcard_info

if __name__ == "__main__":
	print get_netcard()
	print get_allip()
	print f()

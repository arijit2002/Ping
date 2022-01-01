import os
list_ip=["127.0.0.1","www.facebook.com","www.samsung.com"]

cmd="ping -n 1 "

for domain in list_ip:
    cmd=cmd+domain
    res=os.popen(cmd)
    text=res.read().lower()
    
    if "ttl" in text:
        print(domain ," is alive")
    else:
        print(domain ," is not alive")
    cmd="ping -n 1 "

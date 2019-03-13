# net_tools
Various unsophisticated networking tools written in Python 2.7

---
### bhpnet.py
Basic netcat replacement.

Usage: `bhpnet.py -t [target_host] -p [port]`

`-l --listen`  
Listen on [host]:[port] for incoming connections  

`-e --execute=file_to_run`  
Execute the given file upon receiving a connection  

`-c --command`  
Initialize a command shell  

`-u --upload=destination`  
Upon receiving a connection, upload a file and write to [destination]  

Examples  
`bhpnet.py -t 192.168.0.1 -p 5555 -l -c`  
`bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe`  
`bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"`  
`echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135`  

---
### proxy.py
Basic TCP proxy.

Usage: `proxy.py [local_host] [local_port] [remote_host] [remote_port] [receive_first]`  
Example: `proxy.py 127.0.0.1 9000 10.12.132.1 9000 True`  

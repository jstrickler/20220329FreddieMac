#!/usr/bin/env python
import os

os.system("hostname")  # <1>

with os.popen("hostname") as hostname_in:
    raw_hostname = hostname_in.read()
    hostname = raw_hostname.rstrip()
print("hostname: {}\n".format(hostname))


connections = []
with os.popen('netstat -an') as netstat_in:  # <2>
    for raw_line in netstat_in:  # <3>
        if 'ESTABLISHED' in raw_line:  # <4>
            line = raw_line.rstrip()
            proto, local, remote, _ = line.split()
            local_ip, local_port = local.split(':')
            remote_ip, remote_port = remote.split(':')
            data = proto, local_ip, int(local_port), remote_ip, int(remote_port)
            connections.append(data)
            # print(line)
for connection in connections:
    print(connection)
print('-' * 60)
# subprocess module
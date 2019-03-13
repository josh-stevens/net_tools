#!/usr/bin/python
#
# Basic UDP client
# Replace the target_host, target_port, and message to send via UDP
# TODO: take these as command line arguments
#
import socket

target_host = "127.0.0.1"
target_port = 80
message = "AAABBBCCC"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(message, (target_host, target_port))

data, addr = client.recvfrom(4096)

print data
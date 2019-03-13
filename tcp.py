#!/usr/bin/python
#
# Basic TCP client
# Replace the target_host, target_port, and message to send via TCP
# TODO: take these as command line arguments
#
import socket

target_host = "www.google.com"
target_port = 80
message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))
client.send(message)

response = client.recv(4096)
print response

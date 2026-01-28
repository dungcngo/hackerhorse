#!/bin/python3

#SOCKET
import socket

HOST = '127.0.0.1'
PORT = 1105

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))

s.sendall(b"Hello server")

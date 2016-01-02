'''
udpSimpleServer.py - a simple UDP server that echos back strings sent to it.
Copyright (C) 2015  Salim Haniff <salimwp@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should review the GNU General Public License to accept the agreements to 
use this program. Available at http://www.gnu.org/licenses/gpl-3.0.html .
'''
import socket

IP = '127.0.0.1';
PORT = 8088;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.bind((IP, PORT));

while True:
	data, addr = sock.recvfrom(1024);
	print "data: ",data
	sock.sendto("Server> ".encode('utf-16') + data, addr)

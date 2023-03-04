#!/bin/python

import socket

s = socket.socket()

for i in range(20,2000):

   print("This is Banner for the Port: " + str(i))

   try:
       s.connect(("18.195.65.114", i))
       answer = s.recv(1024)
   except:
       continue
   
   try:
       answer = answer.decode('utf8').strip('\r\n')
       print (answer)
   except:
       pass
       
   print (answer)
   
s.close()

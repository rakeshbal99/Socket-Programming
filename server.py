import socket
import sys
import time
from thread import *
 
HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    # conn.send('Welcome to the server.\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        print ("in 00")
        numlist =[]
         
        #Receiving from client
        while True :
            print ("in 11")
            data = conn.recv(1024)
            print type(data)
            # string2 =""
            # numlist=[]
            if data =='*':
                print numlist
                break
            # for char in data :
            #     if char !="\n":
            #         if char !="*":
            #             string2+=char
            #     else:
            #         print ('got', string2)
            print "Lets append\n"
            numlist.append(int(data))
            print "appending done\n"
            print "the list till now looks like this\n"
            print numlist
            print "by now you should have seen the appended list"
            #         string2=""

            # if data =='*':
            #     break

            if not data:
                break
        numlist.sort()
        print numlist
        print "\n"      
        for i in numlist:
            print "Sending :"
            print i
            conn.send(str(i))
            time.sleep(1)
        conn.send(str(999999999))    
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
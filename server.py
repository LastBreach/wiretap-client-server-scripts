#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import time, datetime

class bcolors:
    WARNING = '\033[91m'
    ENDC = '\033[0m'


host = "0.0.0.0"  # Get local machine name
port = 12345                # Reserve a port for your service.


s = socket.socket()         # Create a socket object and allow reuse of socket (for ctrl+c exits)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
    c, addr = s.accept()     # Establish connection with client, log connect and send message to client log.
    now = time.strftime("%Y-%m-%d - %H:%M:%S")

    # Print message from client and send answer
    thismsg = c.recv(1024)
    #print(thismsg)
    c.send('%s: Hello client, this is server' % now)


    # alert if two messages are more than one second apart
    try:
        lastmsg
    except:
        print "Starting..."
    else:
        thistime = thismsg[13:21]
        lasttime = lastmsg[13:21]
     
        #print(lastmsg)
     
        #print int(lastmsg[0:2] + int(lastmsg[3:5] + int(lastmsg[6:8])
        time01 = datetime.datetime(100, 1, 1, int(lasttime[0:2]), int(lasttime[3:5]), int(lasttime[6:8]))
        time02 = datetime.datetime(100, 1, 1, int(thistime[0:2]), int(thistime[3:5]), int(thistime[6:8]))
        if time02 != time01+datetime.timedelta(seconds=1):
            print bcolors.WARNING + thismsg + " (" + lasttime + "/" + thistime + ") - FAIL" + bcolors.ENDC
        else:
            print(thismsg + " (" + lasttime + "/" + thistime + ")")
    
    lastmsg = thismsg

    c.close()                # Close the connection

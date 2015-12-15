#!/usr/bin/python               # This is client.py file
import socket, time, datetime             # Import socket and time modules

class bcolors:
    WARNING = '\033[91m'
    ENDC = '\033[0m'

while True:
    host = "192.168.0.100"      # Get local machine name
    port = 12345                # Reserve a port for your service.

    s = socket.socket()         # Create a socket object
    s.connect((host, port))

    now = time.strftime("%Y-%m-%d - %H:%M:%S")

    # Send hello to server and print answer
    s.send('%s: Hello server, this is client' % now)

    # get current data
    thismsg = s.recv(1024)

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
    
    
    s.close                     # Close the socket when done
    time.sleep(1)               # Wait so as to not spam ourselves



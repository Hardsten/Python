import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given in the command line
server_address = ('', 10000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()

# Listen for incomming connections
sock.listen(1)

msg = []
while True:
    #Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Recieve the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'recieved "%s"' % data
            msg.append(data)

            if data:
                print >> sys.stderr, 'sending back data to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break

    finally:
        msg = ''.join(msg)
        print "repeats the message: %r" % msg
        # clean up the connection
        connection.close()
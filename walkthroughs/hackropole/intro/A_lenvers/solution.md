### Description
Connect to the remote service and for each string received, you need to return the string containing the characters in reverse order.

Example: for the string ANSSI, you should return ISSNA (note: case sensitive).
### Solution
Use this script Python to reverse string:
```bash
import socket
import time

def reverse_string(s):
        return s[::-1]

def main():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('localhost', 4000)
        sock.connect(server_address)

        try:
                while True:
                        time.sleep(1)

                        data = sock.recv(1024)
                        print(f"Recv: {data.decode()}")

                        lines = data.decode().split('\n')

                        if 'Congratulations!! Here is your flag:' in lines:
                                break 

                        for line in lines:
                                if line.startswith('>>>'):
                                        line = line.lstrip('>>> ').rstrip()

                                        response = reverse_string(line)
                                        print(f"Sending: {response}")

                                        response += '\n'

                                        sock.sendall(response.encode())

        finally:
                sock.close()

if __name__ == "__main__":
        main()
```
### Result
`FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}`

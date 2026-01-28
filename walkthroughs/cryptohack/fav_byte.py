from pwn import xor

hex_string = " 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

data = bytes.fromhex(hex_string)

for key in range(256):
        result = xor(data, key)
        try:
                decoded = result.decode('ascii')
                if all(32 <= ord(c) <= 126 for c in decoded):
                        print(f"Key: {key}, Message: {decoded}")
        except UnicodeDecodeError:
                continue

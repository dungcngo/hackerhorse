# Bandit13

## Level Description
The password for the next level is stored in the file `data.txt`, which is a hexdump of a file that has been repeatedly compressed. 

For this level it may be useful to create a directory under `/tmp` in which you can work. Use `mkdir` with a hard to guess directory name. Or better, use the command `mktemp -d`. Then copy the datafile using `cp`, and rename it using `mv` (read the manpages!)

## Method of solving
We start by listing all the files in the home directory.
```bash
bandit12@bandit:~$ ls -la
total 24
drwxr-xr-x   2 root     root     4096 Oct 14 09:26 .
drwxr-xr-x 150 root     root     4096 Oct 14 09:29 ..
-rw-r--r--   1 root     root      220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root     3851 Oct 14 09:19 .bashrc
-rw-r-----   1 bandit13 bandit12 2581 Oct 14 09:26 data.txt
-rw-r--r--   1 root     root      807 Mar 31  2024 .profile
```
There was a file named `data.txt`, so we check on the type of its.
```bash
bandit12@bandit:~$ file data.txt
data.txt: ASCII text
```
It seems like a normal text file, so we try to read it. We use the `cat` command to check the content.
```bash
bandit12@bandit:~$ cat data.txt 
00000000: 1f8b 0808 2817 ee68 0203 6461 7461 322e  ....(..h..data2.
00000010: 6269 6e00 013c 02c3 fd42 5a68 3931 4159  bin..<...BZh91AY
00000020: 2653 59cc 46b5 2d00 0018 ffff da5f e6e3  &SY.F.-......_..
00000030: 9fcd f59d bc69 ddd7 f7ff a7e7 dbdd b59f  .....i..........
00000040: fff7 cfdd ffbf bbdf ffff ff5e b001 3b58  ...........^..;X
00000050: 2406 8000 00d0 6834 6234 d000 6869 9000  $.....h4b4..hi..
00000060: 1a7a 8003 40d0 01a1 a006 8188 340d 1a68  .z..@.......4..h
00000070: d340 d189 e906 8f41 0346 4d94 40d1 91a0  .@.....A.FM.@...
00000080: 681a 0681 a068 0680 c400 3207 a269 a189  h....h....2..i..
00000090: a326 8000 c800 c81a 1883 1000 00d0 c023  .&.............#
000000a0: 4311 a034 30ca 6800 0680 0681 a680 6868  C..40.h.......hh
000000b0: d068 6868 c04c d400 0003 4d06 87a8 d000  .hhh.L....M.....
000000c0: 3086 8c20 3268 068d 000c 9a64 0698 8d04  0.. 2h.....d....
000000d0: 0600 6860 3541 2c85 c8e1 7bc9 479e e369  ..h`5A,...{.G..i
000000e0: 30a1 0250 82e9 64ef 9d40 312f 4bc8 b00f  0..P..d..@1/K...
000000f0: 0c8f 026c d5ca 1008 d7aa 336a ed8f bb7b  ...l......3j...{
00000100: b43f d544 1658 824e a4af 9ce5 612e 8a27  .?.D.X.N....a..'
00000110: c303 0512 cbff dccd f42d 6866 ceec 8127  .........-hf...'
00000120: 5475 ed39 100b f897 7828 46e2 fdf3 efa7  Tu.9....x(F.....
00000130: 43b0 1701 a114 397a 1d81 8d1f 1f23 2ada  C.....9z.....#*.
00000140: 9b18 ee4d d05d 4ae3 d032 e494 ae98 27b0  ...M.]J..2....'.
00000150: 30a0 533c 6696 60ad c546 70c4 322b 7174  0.S<f.`..Fp.2+qt
00000160: 8bb1 52c6 ed0a 267b 7165 208b 77fe 1294  ..R...&{qe .w...
00000170: 2280 3311 354f c68e e004 93e3 abf4 5a0a  ".3.5O........Z.
00000180: a568 c894 27c2 9015 49bb 0147 c253 8e73  .h..'...I..G.S.s
00000190: 2fdd 90e1 6871 c692 1d67 5ebc a5f9 b8a1  /...hq...g^.....
000001a0: 3913 f073 1919 b628 9ae2 c1bf 15ee 493a  9..s...(......I:
000001b0: e375 4d23 71e0 4934 c7a2 15ff 985c a0ba  .uM#q.I4.....\..
000001c0: 9e65 d613 313d 7cef 512a 32bf 835e 50d6  .e..1=|.Q*2..^P.
000001d0: a54f 57ba bceb 6944 03c8 8a50 3542 9140  .OW...iD...P5B.@
000001e0: eb51 0f4c 8a23 9401 0246 0457 d1c0 c33e  .Q.L.#...F.W...>
000001f0: c328 2de7 3d1d 64be 4190 36b0 b803 4f80  .(-.=.d.A.6...O.
00000200: 40bc 3960 ac5e 13a9 3a77 0162 d662 7659  @.9`.^..:w.b.bvY
00000210: fdfd 9535 1188 8588 e8e5 a78d 9b24 c066  ...5.........$.f
00000220: 91c6 4212 fac6 4ed8 ce48 161f cc44 215f  ..B...N..H...D!_
00000230: 330c 5ed7 2709 e578 6efd 3775 c703 8aa1  3.^.'..xn.7u....
00000240: 10b6 2c5d 16bf f352 c7ff c5dc 914e 1424  ..,]...R.....N.$
00000250: 3311 ad4b 40d0 18b2 373c 0200 00         3..K@...7<...
```
Instead of readable text, we see what looks like a hex dump or compressed data. This suggests that the file is encoded or compressed.

Since we will working with multiple extracted files, we create a temporary directory using `mktemp -d` and move into it.
```bash
bandit12@bandit:~$ mktemp -d
/tmp/tmp.JvLJTwYvQ9
bandit12@bandit:~$ cd /tmp/tmp.JvLJTwYvQ9
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ 
```
We copy `data.txt` into the temporary directory.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ cp ~/data.txt .
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ ls
data.txt
```
Since the file appears to be in a hex dump format, we use `xxd -r` convert it back to binary.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ xxd -r data.txt > data.bin
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ ls
data.bin  data.txt
```
Let's check the file type again.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data.bin
data.bin: gzip compressed data, was "data2.bin", last modified: Tue Oct 14 09:26:00 2025, max compression, from Unix, original size modulo 2^32 572
```
It is a `gzip` file, so we rename it and decompress it.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data.bin data.gz
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ gunzip data.gz 
```
We check the new file.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ ls
data  data.txt
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data
data: bzip2 compressed data, block size = 900k
```
The file is now in `bzip2` format, so we rename and decompress it.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data data.bz2
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ bunzip2 data.bz2 
```
Checking the file type again:
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ ls
data  data.txt
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data
data: gzip compressed data, was "data4.bin", last modified: Tue Oct 14 09:26:00 2025, max compression, from Unix, original size modulo 2^32 20480
```
We repeat the decompression process.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data data.gz
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ gunzip data.gz 
```
Checking the file type again:
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ ls
data  data.txt
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data
data: POSIX tar archive (GNU)
```
So the file is now a `.tar` archive, we extract it.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data data.tar
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ tar -xvf data.tar 
data5.bin
```
The reveals a new file, `data5.bin`, which is another `.tar` archive.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data5.bin 
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data5.bin data5.tar
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ tar -xvf data5.tar 
data6.bin
```
This extracts `data6.bin`, which is compressed with `bzip2`.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data6.bin 
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data6.bin data6.bz2
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ bunzip2 data6.bz2 
```
Checking the file:
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ ls
data5.tar  data6  data.tar  data.txt
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data6
data6: POSIX tar archive (GNU)
```
We extract it again:
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data6 data6.tar
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ tar -xvf data6.tar 
data8.bin
```
This gives us `data8.bin`, which is `gzip` compressed.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 14 09:26:00 2025, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ mv data8.bin data8.gz
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ gunzip data8.gz 
```
Checking the file:
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ ls
data5.tar  data6.tar  data8  data.tar  data.txt
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ file data8
data8: ASCII text
```
Finally, A peak of the file already found, `cat` the file and we got the password.
```bash
bandit12@bandit:/tmp/tmp.JvLJTwYvQ9$ cat data8
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```
The password for the next level appeared!

## What we learned
- How to work with hex dumps and convert them back into binary using `xxd -r`.
- The importance of using `file` to identify file types at each stage of extraction.
- How to handle multiple ocmpression formats, including `gzip`, `bzip2`, and `tar`.
- The benefits of using `mktemp -d` to create a temporary working directoyr for clean and organized extraction.
- The iterative process of renaming and extracting files based on their type.
How data can be layered with multiple compression to obscure information.

## Key command
`mv data.old data.new`

`gunzip data.gz`

`bunzip2 data.bz2`

`tar -xvf data.tar`

***You are welcome!***

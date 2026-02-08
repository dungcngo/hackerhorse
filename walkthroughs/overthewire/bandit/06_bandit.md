# Bandit06

## Level Description
The task was to find the password stored in a file located somewhere under the `inhere` directory. The file needed to match all the following criteria:
- Human-readable
- Exactly 1033 bytes in size
- Not executable

## Method of Solving
After logging into the server as `bandit5`, we started by exploring the home directory:
```bash
bandit5@bandit:~$ ls 
inhere
```
We saw a directory named `inhere`. Knowing the file could be buried anywhere within this directory, we decided to use the `find` command to locate it.
```bash
bandit5@bandit:~$ ls ./inhere/
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
```
The `find` command is powerful for searching files with specific attributes. We constructed the following command:
```bash
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ find . -type f -size 1033c ! -executable -exec file {} \;
./maybehere07/.file2: ASCII text, with very long lines (1000)
```
- `.`: Start the search in the current directory.
- `-type f`: Limit the search to files only.
- `-size 1033c`: Look for files exactly 1033 bytes in size (`c` stands for bytes).
- `! -executable`: Exclude executable files.
- `-exec file {} \;`: For each file found, execute the file command to confirm its type.
We used the `cat` command to read the file and retrieve the password:
```bash
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```
## What we learned
- **Advanced `find` Command Usage**: This challenge taught me how to combine `find` options effectively to locate files with specific properties like size and executability.
- **Combining Commands**: Using `-exec` with `find` allowed me to verify file types without manually inspecting each result.
- **Understanding File Properties**: Recognizing that size, readability, and executability can be filtered was key to solving this challenge.

## Key command
`find . -type f -size 1033c ! -executable -exec file {} \;`

`cat ./maybehere07/.file2`

***You are welcome!***

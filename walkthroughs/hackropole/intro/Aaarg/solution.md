### Information
You must display the flag, whatever it takes!
### Solution
Analysis assembler of `aaarg` by `ida`.

This is pseudocode of `main` function:
```bash
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  __int64 result; // rax
  unsigned __int64 v4; // rcx
  unsigned __int64 i; // rbx
  char *endptr; // [rsp+0h] [rbp-10h] BYREF

  result = 1LL;
  if ( a1 >= 2 )
  {
    v4 = strtoul(a2[1], &endptr, 10);
    result = 1LL;
    if ( !*endptr )
    {
      result = 2LL;
      if ( v4 == -a1 )
      {
        for ( i = 0LL; i < 0x116; i += 4LL )
          putc(byte_402010[i], stdout);
        putc(10, stdout);
        return 0LL;
      }
    }
  }
  return result;
```
We see `a1` (`argc`) = 2 -> `-a1` = -2.

### Result
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ./aaarg -2
FCSC{f9a38adace9dda3a9ae53e7aec180c5a73dbb7c364fe137fc6721d7997c54e8d}
```

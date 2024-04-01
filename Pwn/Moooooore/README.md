# I returned to win
Author: [Marin Radu](https://github.com/ChronosPK)

## Description
```
Basic buffer overflow challenge.
```

## Requirements
- analyze `elf` binaries

## Solve


```
The program has an integer variable floor, the value of which needs to be changed. The floor variable is of int type, of size 4 bytes. The coffee array is of character type, each character is 1 byte, hence the array takes 30 bytes. So the main function will be alloted 48 bytes of memory, since that is the nearest multiple of 16 after 30 + 4.

The 4 bytes of the function's stack adjacent to the saved rbp is going to store floor. We can confirm that using GDB. In main <+56>, there is a comparison between [rbp-0x4] and 0x0.

Now, we can simply fill up the entire stack with some random bytes (!= 0), so that the value of the floor variable is changed, leading to a call to the system() function.
```

<br>

> Flag: `CSCTF{7h3_m0r3_y0u_kn0w_7h3_l355_y0u_kn0w}`

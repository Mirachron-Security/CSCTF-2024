# Math Master
Author: [Stratulat Dragoș](https://www.linkedin.com/in/stratulat-dragos-6b9a09227)

<br>

## Description
```
Perform quick math operations sent from a server and return the correct answers.
```

<br>

## Requirements
- Connect to servers
- Automation
- Regex

<br>

## Solve
The server sends an array of numbers separated by column. 
The array's last element is a string which indicates math operation that must be performed. 
If the server doesn't receive the answer in less than one second, it will close the connection.

```bash
┌──(kali㉿kali)-[~]
└─$ nc 127.0.0.1 9999              
980,891,631,711,572,690,571,760,775,add
Answer: 23
Wrong :(

┌──(kali㉿kali)-[~]
└─$ nc 127.0.0.1 9999
882,791,864,988,816,multiply
Answer: asd
Invalid input: Please enter a valid integer.

┌──(kali㉿kali)-[~]
└─$ nc 127.0.0.1 9999
827,809,689,698,879,501,844,640,835,754,859,add
Answer: 124
Too slow mate. Bye!
```

Because we can't perform operation manually, we have to automate the process. 
I used Python's `pwntools` module to compute math operation and send the result in less than one second.

Since we know that the last prompt will be the flag, we calculate until we get it: `CSCTF...`

Check out the [solution script](./solve/solve.py).

```bash
┌──(kali㉿kali)-[~]
└─$ python3 solve.py chal
[+] Opening connection to 127.0.0.1 on port 9999: Done
CSCTF{b241213f12b3eeb7bc769e56fae40dfb33b0a29574fcecbd03137e03d7938551}
[*] Closed connection to 127.0.0.1 port 9999
```

<br>

> Flag: `CSCTF{hash-that-changes-every-5-minutes}`
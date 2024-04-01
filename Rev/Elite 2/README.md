# Elite 2
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Decipher the correct hexadecimal input by understanding the XOR operation performed by the program.
```

<br>

## Requirements
- Decompiled source code
- XOR
- Understanding a C program

<br>

## Solve
Firstly, you should use `ghidra` or another software to analyze the binary and try to reconstruct the C code.

To reverse engineer the given C program, you need to understand the following steps:
- **User Input**: The program prompts the user to enter a hexadecimal number. <br>
    The `%x` format specifier is used with `scanf` to read the user's input as a hexadecimal integer and store it in the input variable.
- **XOR Operation**: The program `XOR`s the user's input (stored in input) with the hexadecimal value `0x10101010` <br>
    and stores the result in a variable named new.
- **Comparison**: The program checks if the value stored in new is equal to `0x499602D2`. <br>
    If the equality condition is met, it prints a message indicating success. <br>
    Otherwise, it prints a message suggesting that the user should try again.
- **Invalid Input**: If the user enters invalid input (e.g., non-hexadecimal characters or an invalid format), <br>
    the program prints an "Invalid input" message.

To reverse engineer the program, you would need to determine what input (in hexadecimal format) <br>
produces the result `0x499602D2` when XOR-ed with `0x10101010`. <br>
You can calculate this in C by performing the reverse XOR operation:
```c
int correctInput = 0x499602D2 ^ 0x10101010;
```

You can check it using `python` as well:
```python
correctInput = 0x499602D2 ^ 0x10101010
print(hex(correct_input))
```

The value of `correctInput` is `0x490c23c0`. <br>
So, when the user enters `0x490c23c0` as input, the program will XOR it with `0x10101010`, <br>
resulting in `0x499602D2`, and the success message will be printed.

<br>

In summary, you reverse engineer the program by calculating the input that, <br>
when XOR-ed with `0x10101010`, produces the expected result `0x499602D2`.<br>

<br>

> Flag: `CSCTF{0x490c23c0}`

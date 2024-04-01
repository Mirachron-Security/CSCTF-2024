# Source
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
The flag is split in variables and can be read from the strings.
```

<br>

## Requirements
- `strings`

<br>

## Solve
One of the first things you can do to analyze a binary is to run `strings` on it.
This will show you plaintext strings from the binary that might give you relevant information.

The following one-liner splits the flag into 5 parts:
```bash
strings -n3 ./vuln | grep -A4 CSCTF{ | tr -d "\n"
```

| Command | Explanation |
|---|---|
|`strings -n3` | lines with at least 3 characters |
|`grep -A4` | read 4 lines after we match `'CSCTF{'` |
|`tr -d "\n"` | remove newlines |

<br>

> Flag: `CSCTF{couldn't_think_of_a_cool_flag_so_there_you_go}`

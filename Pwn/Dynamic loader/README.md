# Dynamic loader
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
The binary writes the flag in a directory hidden in /tmp.
```

<br>

## Requirements
- Dynamic analysis tools

<br>

## Solve
Use a tool like `strace` for dynamic analysis to monitor the system calls.
```bash
strace ./app/vuln
```

You will see a process that opens a file hidden in `/tmp`
```
[SNIPPET]

--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=46916, si_uid=1000, si_status=0, si_utime=0, si_stime=0} ---
wait4(-1, 0x7ffe9baf9990, WNOHANG, NULL) = -1 ECHILD (No child processes)
rt_sigreturn({mask=[]})                 = 0
openat(AT_FDCWD, "/tmp/...|/.hidden", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 3
fcntl(1, F_GETFD)                       = 0
fcntl(1, F_DUPFD, 10)                   = 10
fcntl(1, F_GETFD)                       = 0
fcntl(10, F_SETFD, FD_CLOEXEC)          = 0
dup2(3, 1)                              = 1
close(3)                                = 0
write(1, "CSCTF{d0N-t_rUn_3XeCut@bl3s_y"..., 52) = 52
dup2(10, 1)                             = 1
fcntl(10, F_GETFD)                      = 0x1 (flags FD_CLOEXEC)
close(10)                               = 0
read(255, "", 1474)                     = 0
rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

You can read a location (`openat(AT_FDCWD, "/tmp/...|/.hidden ...`) and part of the flag (`write(1, "CSCTF{d0N-t_rUn_3XeCut@bl3s_y"`)

Just navigate to `"/tmp/...|/.hidden"` and read the flag that has been generated.

<br>

> Flag: `CSCTF{d0N-t_rUn_3XeCut@bl3s_y0U_hAV3n-t_c0mpiL3D}`
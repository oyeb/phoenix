# This file is part of Phoenix
#
# Copyright (c) 2016, 2017 Vasantha Ganesh K.
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with is source code.

import seccomp
import prctl

def syscall_filter():

    prctl.set_dumpable(0)
    prctl.set_no_new_privs(1)

    fltr = seccomp.SyscallFilter(defaction=seccomp.ALLOW)

    fltr.add_rule(seccomp.KILL, 'clone')
    fltr.add_rule(seccomp.KILL, 'fork')
    
    #gives status about the file
    fltr.add_rule(seccomp.KILL, 'stat')
    fltr.add_rule(seccomp.KILL, 'fstat')
    fltr.add_rule(seccomp.KILL, 'lstat')
    
    #repostions offset of the open file
    fltr.add_rule(seccomp.KILL, 'lseek')
    
    #examine and change a signal action 
    fltr.add_rule(seccomp.KILL, 'rt_sigaction')
    
    #examine and change blocked signals 
    fltr.add_rule(seccomp.KILL, 'rt_sigprocmask')
    
    #return from signal handler and cleanup stack frame
    fltr.add_rule(seccomp.KILL, 'rt_sigreturn')
    
    #manipulates device parameters of special files
    fltr.add_rule(seccomp.KILL, 'ioctl')
    
    #create pipe for file descriptors
    fltr.add_rule(seccomp.KILL, 'pipe')
    
    #remap a virtual memory address
    fltr.add_rule(seccomp.KILL, 'mremap')
    
    #synchronize a file with a memory map
    fltr.add_rule(seccomp.KILL, 'msync')
     
    #give advice about use of memory 
    fltr.add_rule(seccomp.KILL, 'madvise')
     
    #shared memory 
    fltr.add_rule(seccomp.KILL, 'shmget')
    fltr.add_rule(seccomp.KILL, 'shmat')
    fltr.add_rule(seccomp.KILL, 'shmctl')
    fltr.add_rule(seccomp.KILL, 'shmdt')
    
    #duplicate file descriptor
    fltr.add_rule(seccomp.KILL, 'dup')
    fltr.add_rule(seccomp.KILL, 'dup2')
    
    #wait for signal
    fltr.add_rule(seccomp.KILL, 'pause')
    
    # high-resolution sleep 
    fltr.add_rule(seccomp.KILL, 'nanosleep')
    
    #get or set value of interval timer
    fltr.add_rule(seccomp.KILL, 'getitimer')
    fltr.add_rule(seccomp.KILL, 'setitimer')
    
    # set an alarm for delivery of a signal 
    fltr.add_rule(seccomp.KILL, 'alarm')
    
    #transfer data between file descriptors
    fltr.add_rule(seccomp.KILL, 'sendfile')
    
    #create an endpoint for communication
    fltr.add_rule(seccomp.KILL, 'socket')
    
    #initiate a connection on a socket
    fltr.add_rule(seccomp.KILL, 'connect')
    
    #accept connection or send message or receive on a socket
    fltr.add_rule(seccomp.KILL, 'accept')
    fltr.add_rule(seccomp.KILL, 'sendto')
    fltr.add_rule(seccomp.KILL, 'recvfrom')
    fltr.add_rule(seccomp.KILL, 'sendmsg')
    fltr.add_rule(seccomp.KILL, 'recvmsg')
    
    #other socket related system calls
    fltr.add_rule(seccomp.KILL, 'shutdown')
    fltr.add_rule(seccomp.KILL, 'bind')
    fltr.add_rule(seccomp.KILL, 'listen')
    fltr.add_rule(seccomp.KILL, 'getsockname')
    fltr.add_rule(seccomp.KILL, 'getpeername')
    fltr.add_rule(seccomp.KILL, 'socketpair')
    fltr.add_rule(seccomp.KILL, 'setsockopt')
    fltr.add_rule(seccomp.KILL, 'getsockopt')
    
    #system calls for child process
    fltr.add_rule(seccomp.KILL, 'clone')
    fltr.add_rule(seccomp.KILL, 'fork')
    fltr.add_rule(seccomp.KILL, 'vfork')
    
    #execute programs
    fltr.add_rule(seccomp.KILL, 'execve')
    
    #gives info about kernel
    fltr.add_rule(seccomp.KILL, 'uname')
    
    #message related sys calls (IPCs)
    fltr.add_rule(seccomp.KILL, 'msgget')
    fltr.add_rule(seccomp.KILL, 'msgsnd')
    fltr.add_rule(seccomp.KILL, 'msgrcv')
    fltr.add_rule(seccomp.KILL, 'msgctl')
    
    #manipulate file descriptor
    fltr.add_rule(seccomp.KILL, 'fcntl')
    
    #apply or remove an advisory lock on an open file
    fltr.add_rule(seccomp.KILL, 'flock')
    
    # truncate a file to a specified length
    fltr.add_rule(seccomp.KILL, 'truncate')
    fltr.add_rule(seccomp.KILL, 'ftruncate')
    
    #directory sys calls 
    fltr.add_rule(seccomp.KILL, 'getdents')
    fltr.add_rule(seccomp.KILL, 'getcwd')
    fltr.add_rule(seccomp.KILL, 'chdir')
    fltr.add_rule(seccomp.KILL, 'fchdir')
    fltr.add_rule(seccomp.KILL, 'mkdir')
    fltr.add_rule(seccomp.KILL, 'rmdir')
    
    #open and possibly create a file or device
    fltr.add_rule(seccomp.KILL, 'creat')
    
    #make a new name for a file 
    fltr.add_rule(seccomp.KILL, 'link')
    
    #other link related system calls
    fltr.add_rule(seccomp.KILL, 'unlink')
    fltr.add_rule(seccomp.KILL, 'symlink')
    fltr.add_rule(seccomp.KILL, 'readlink')
    
    #change file mode bits or owner
    fltr.add_rule(seccomp.KILL, 'chmod')
    fltr.add_rule(seccomp.KILL, 'fchmod')
    fltr.add_rule(seccomp.KILL, 'chown')
    fltr.add_rule(seccomp.KILL, 'fchown')
    fltr.add_rule(seccomp.KILL, 'lchown')
    fltr.add_rule(seccomp.KILL, 'umask')
    
    #resource usage
    fltr.add_rule(seccomp.KILL, 'getrusage')
    
    #system stats info
    fltr.add_rule(seccomp.KILL, 'sysinfo')
    
    #process trace
    fltr.add_rule(seccomp.KILL, 'ptrace')
     
    #get user identity
    fltr.add_rule(seccomp.KILL, 'getuid')
    
    #send messages to the system logger
    fltr.add_rule(seccomp.KILL, 'syslog')
    
    #other id related calls
    fltr.add_rule(seccomp.KILL, 'getgid')
    fltr.add_rule(seccomp.KILL, 'setuid')
    fltr.add_rule(seccomp.KILL, 'setgid')
    fltr.add_rule(seccomp.KILL, 'geteuid')
    fltr.add_rule(seccomp.KILL, 'getegid')
    fltr.add_rule(seccomp.KILL, 'setpgid')
    fltr.add_rule(seccomp.KILL, 'getpgrp')
    fltr.add_rule(seccomp.KILL, 'setsid')
    fltr.add_rule(seccomp.KILL, 'setreuid')
    fltr.add_rule(seccomp.KILL, 'setregid')
    fltr.add_rule(seccomp.KILL, 'setresuid')
    fltr.add_rule(seccomp.KILL, 'getresuid')
    fltr.add_rule(seccomp.KILL, 'setresgid')
    fltr.add_rule(seccomp.KILL, 'getresgid')
    fltr.add_rule(seccomp.KILL, 'getpgid')
    fltr.add_rule(seccomp.KILL, 'setfsuid')
    fltr.add_rule(seccomp.KILL, 'setfsgid')
    fltr.add_rule(seccomp.KILL, 'getsid') 
    fltr.add_rule(seccomp.KILL, 'getgroups')
    fltr.add_rule(seccomp.KILL, 'setgroups')
    
    #get/set capabilities of thread
    fltr.add_rule(seccomp.KILL, 'capget')
    fltr.add_rule(seccomp.KILL, 'capset')
    
    #change file last access and modification times
    fltr.add_rule(seccomp.KILL, 'utime')
    
    #create a special or ordinary file 
    fltr.add_rule(seccomp.KILL, 'mknod')
    
    #load shared library
    fltr.add_rule(seccomp.KILL, 'uselib')
    
    #set the process execution domain 
    fltr.add_rule(seccomp.KILL, 'personality')
    
    #get file system statistics 
    fltr.add_rule(seccomp.KILL, 'statfs')
    fltr.add_rule(seccomp.KILL, 'fstatfs')
    
    #get file system info 
    fltr.add_rule(seccomp.KILL, 'sysfs')
    
    #lock and unlock memory 
    fltr.add_rule(seccomp.KILL, 'mlock')
    fltr.add_rule(seccomp.KILL, 'munlock')
    fltr.add_rule(seccomp.KILL, 'mlockall')
    fltr.add_rule(seccomp.KILL, 'munlockall')
    
    #virtually hangup the current terminal 
    fltr.add_rule(seccomp.KILL, 'vhangup')
    
    #get or set local decriptor table
    fltr.add_rule(seccomp.KILL, 'modify_ldt')
    
    #change the root file system
    fltr.add_rule(seccomp.KILL, 'pivot_root')
    
    #read/write system parameters
    fltr.add_rule(seccomp.KILL, '_sysctl')
    
    #operations on a process
    fltr.add_rule(seccomp.KILL, 'prctl')
    fltr.add_rule(seccomp.KILL, 'arch_prctl')
    
    #tune kernel clock
    fltr.add_rule(seccomp.KILL, 'adjtimex')
    
    #get/set resource limits
    fltr.add_rule(seccomp.KILL, 'setrlimit')
    
    #changing root directory
    fltr.add_rule(seccomp.KILL, 'chroot')
    #get / set time
    fltr.add_rule(seccomp.KILL, 'settimeofday')
    
    #mount and unmount filesystems 
    fltr.add_rule(seccomp.KILL, 'mount')
    fltr.add_rule(seccomp.KILL, 'unmount2')
    
    #enable/disable devices and files for paging and swapping 
    fltr.add_rule(seccomp.KILL, 'swapon')
    fltr.add_rule(seccomp.KILL, 'swapoff')
    
    #reboot or enable/disable Ctrl-Alt-Del
    fltr.add_rule(seccomp.KILL, 'reboot')
    
    #get/set hostname 
    fltr.add_rule(seccomp.KILL, 'sethostname')
    fltr.add_rule(seccomp.KILL, 'setdomainname')
    
    #change I/O privilege level 
    fltr.add_rule(seccomp.KILL, 'iopl')
    
    #set port input/output permissions
    fltr.add_rule(seccomp.KILL, 'ioperm')
     
    #create, initialize or delete a loadable module entry
    fltr.add_rule(seccomp.KILL, 'create_module')
    fltr.add_rule(seccomp.KILL, 'init_module')
    fltr.add_rule(seccomp.KILL, 'delete_module')
    fltr.add_rule(seccomp.KILL, 'query_module')
    
    #retrieve exported kernel and module symbols 
    fltr.add_rule(seccomp.KILL, 'get_kernel_syms')
    
    #manipulate disk quotas 
    fltr.add_rule(seccomp.KILL, 'quotactl')
    
    #syscall interface to kernel nfs daemon
    fltr.add_rule(seccomp.KILL, 'nfsservctl')
    
    fltr.load()

    


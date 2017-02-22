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
    
    #set and get a process's CPU affinity mask
    fltr.add_rule(seccomp.KILL, 'sched_setaffinity')
    fltr.add_rule(seccomp.KILL, 'sched_getaffinity')
    
    #Create or destroy an asynchronous I/O context 
    fltr.add_rule(seccomp.KILL, 'io_setup')
    fltr.add_rule(seccomp.KILL, 'io_destroy')
    
    #submit or cancel asynchronous I/O blocks for processing
    fltr.add_rule(seccomp.KILL, 'io_submit')
    fltr.add_rule(seccomp.KILL, 'io_cancel') 
    
    #return a directory entry's path
    fltr.add_rule(seccomp.KILL, 'lookup_dcookie')
    
    # clock and time functions
    fltr.add_rule(seccomp.KILL, 'clock_settime')
    
    #change file last access and modification times
    fltr.add_rule(seccomp.KILL, 'utimes')
    
    #set memory policy for a memory range
    fltr.add_rule(seccomp.KILL, 'mbind')
    
    #set default NUMA memory policy for a process and its children
    fltr.add_rule(seccomp.KILL, 'set_mempolicy')
    
    #message queue related system calls
    fltr.add_rule(seccomp.KILL, 'mq_open')
    fltr.add_rule(seccomp.KILL, 'mq_unlink')
    fltr.add_rule(seccomp.KILL, 'mq_timedsend')
    fltr.add_rule(seccomp.KILL, 'mq_timedreceive')
    fltr.add_rule(seccomp.KILL, 'mq_notify')
    fltr.add_rule(seccomp.KILL, 'mq_getsetattr')
    
    #load a new kernel for later execution 
    fltr.add_rule(seccomp.KILL, 'kexec_load')
    
    #add or request a key from the kernel's key management facility
    fltr.add_rule(seccomp.KILL, 'add_key')
    fltr.add_rule(seccomp.KILL, 'request_key')
    
    #key management facility control         
    fltr.add_rule(seccomp.KILL, 'keyctl')
    
    #system calls for monitoring file system events
    fltr.add_rule(seccomp.KILL, 'inotify_init')
    fltr.add_rule(seccomp.KILL, 'inotify_add_watch')
    fltr.add_rule(seccomp.KILL, 'inotify_rm_watch')
    fltr.add_rule(seccomp.KILL, 'inotify_init1')
    
    #move all pages in a process to another set of nodes 
    fltr.add_rule(seccomp.KILL, 'migrate_pages')
    
    #system calls relative to a directory file descriptor
    fltr.add_rule(seccomp.KILL, 'mkdirat')
    fltr.add_rule(seccomp.KILL, 'fchownat')
    
    #change timestamps of a file relative to a directory file descriptor 
    fltr.add_rule(seccomp.KILL, 'futimesat')
    
    #retrieve information about the file pointed to by pathname
    fltr.add_rule(seccomp.KILL, 'newfstatat') 
    
    #add or remove a directory entry relative to a directory file descriptor
    fltr.add_rule(seccomp.KILL, 'linkat')
    fltr.add_rule(seccomp.KILL, 'unlinkat')
    
    #create a symbolic link relative to a directory file descriptor
    fltr.add_rule(seccomp.KILL, 'symlinkat')
    
    #change permissions of a file relative to a directory file descriptor
    fltr.add_rule(seccomp.KILL, 'fchmodat')
    
    # check user's permissions of a file relative to a directory file descriptor
    fltr.add_rule(seccomp.KILL, 'faccessat')
    
    # moves data between two fd without copying between kernel addr & user addr
    fltr.add_rule(seccomp.KILL, 'splice')
    
    #duplicating pipe content 
    fltr.add_rule(seccomp.KILL, 'tee')
    
    #splice user pages into a pipe
    fltr.add_rule(seccomp.KILL, 'vmsplice')
    
    #move individual pages of a process to another node
    fltr.add_rule(seccomp.KILL, 'move_pages')
    
    #change file timestamps with nanosecond precision 
    fltr.add_rule(seccomp.KILL, 'utimensat')
    
    #accept a connection on a socket 
    fltr.add_rule(seccomp.KILL, 'accept4')
    
    #duplicate a file descriptor
    fltr.add_rule(seccomp.KILL, 'dup3')
    
    #creates pipe
    fltr.add_rule(seccomp.KILL, 'pipe2')
    
    # queue a signal and data    
    fltr.add_rule(seccomp.KILL, 'rt_tgsigqueueinfo')
    
    # receive multiple messages on a socket 
    fltr.add_rule(seccomp.KILL, 'recvmmsg')
    
    fltr.load()

    


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
    
    
    fltr.load()

    


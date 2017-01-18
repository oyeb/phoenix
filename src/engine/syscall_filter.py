import seccomp
import prctl

def syscall_filter():

    prctl.set_dumpable(0)
    prctl.set_no_new_privs(1)

    fltr = seccomp.SyscallFilter(defaction=seccomp.ALLOW)

    fltr.add_rule(seccomp.KILL, 'clone')
    fltr.add_rule(seccomp.KILL, 'fork')

    fltr.load()

    


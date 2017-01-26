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

    fltr.load()

    


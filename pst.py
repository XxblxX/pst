#!/usr/bin/env python3

import sys
import subprocess
import re
import os
import pexpect

def ssh_i():
    sshpass = ('sshpass -p {2} ssh -oStrictHostKeyChecking=no {1}@{0} -t bash'.format(ip, user, password))
    sh = pexpect.spawn(sshpass, encoding='utf-8', echo=False)
    sh.setwinsize(400,400)
    sh.sendline('source <(curl -s0 curl -s0 https://raw.githubusercontent.com/XxblxX/pst/master/.bashrc)')
    sh.sendline('clear; history -c')
    sh.setecho(True)
    sh.interact()

try:
    ip = sys.argv[1]
    user = "root"
    password = sys.argv[2]
    alias = 'alias nr="service nginx restart"'
    
    if __name__ == "__main__":
        ssh_i()

except IndexError:
    pass
except ValueError:
    pass

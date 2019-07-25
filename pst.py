#!/usr/bin/env python3

import pexpect, struct, fcntl, termios, signal, sys

def get_terminal_size():
    s = struct.pack("HHHH", 0, 0, 0, 0)
    a = struct.unpack('hhhh', fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s))
    return a[0], a[1]

def sigwinch_passthrough(sig, data):
    global p
    p.setwinsize(*get_terminal_size())

try:

    if __name__ == "__main__":
        ip = sys.argv[1]
        user = "root"
        password = sys.argv[2] 
        sshpass = ('sshpass -p {2} ssh -oStrictHostKeyChecking=no {1}@{0} -t bash'.format(ip, user, password))

        p = pexpect.spawn(sshpass, encoding='utf-8', echo=False)
        p.setwinsize(*get_terminal_size())
        signal.signal(signal.SIGWINCH, sigwinch_passthrough)
        p.sendline('source <(wget -O- https://raw.githubusercontent.com/XxblxX/pst/master/.bashrc)')

        p.sendline('clear; history -c')
        p.setecho(True)
        p.interact()

except IndexError:
    pass
except ValueError:
    pass

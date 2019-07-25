#!/usr/bin/env bash

PS1="\[\e[33;40m\]\A\[\e[m\] \[\e[33m\]\h\[\e[m\] \[\e[33m\]😈\[\e[m\] "

alias l='ls -lAXh --color=auto'

alias ports="netstat -tulanp | grep LISTEN"

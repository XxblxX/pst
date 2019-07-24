#!/usr/bin/env bash

PS1="\[\e[33;40m\]\A\[\e[m\] \[\e[33m\]\h\[\e[m\] \[\e[33m\]😈\[\e[m\] "

alias ls="ls --color=auto"
alias l='ls -lah --color=auto'

alias ports="netstat -tulanp | grep LISTEN"

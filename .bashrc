#!/usr/bin/env bash

PS1="\[\e[33;40m\]\A\[\e[m\] \[\e[33m\]\h\[\e[m\] \[\e[33m\]😈\[\e[m\] "

alias ls="ls --color=auto"

alias nr="service nginx restart"

alias ports="netstat -tulanp | grep LISTEN"
alias service="systemctl list-unit-files | egrep '^httpd\.|^apache2\.|^nginx\.|mariadb|mysqld\.'"

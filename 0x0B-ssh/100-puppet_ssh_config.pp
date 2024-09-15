#!/usr/bin/env bash

# Configuration using puppet
file { '~/.ssh/config':
  ensure  => file,
  content => @("EOF"),
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  EOF
}

#!/usr/bin/env bash
# Configuration using puppet
file { '~/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @("EOF"),
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  EOF
}

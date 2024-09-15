#!/usr/bin/env bash
# Configuration using puppet
file { '~/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0777',
  content => @("EOF"),
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  EOF
}

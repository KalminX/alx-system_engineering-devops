# Configuration using puppet
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => @("EOF"),
Host *
    IdentityFile /home/ubuntu/.ssh/school
    PasswordAuthentication no
  EOF
}

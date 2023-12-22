# Ensure Python 3 is installed
package { 'python3':
  ensure => installed,
}

# Ensure Pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask v2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

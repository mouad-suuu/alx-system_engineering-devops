# 1-install_a_package.pp

# Install Python 3.8.10
class { 'python':
  version => '3.8.10',
}

# Install Flask 2.1.0 and Werkzeug 2.1.1
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Class['python'],
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Class['python'],
}

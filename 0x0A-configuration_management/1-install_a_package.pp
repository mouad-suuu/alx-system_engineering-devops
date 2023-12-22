# 1-install_a_package.pp
# task 2
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Puppet Manifest: 2-execute_a_command.pp
# Description: Terminate the process named killmenow

exec { 'killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}

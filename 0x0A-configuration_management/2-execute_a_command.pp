#Using Puppet, create a manifest that kills a process named killmenow

exec { 'killmenow_process':
  command  => 'pkill -f killmenow',
  path     => ['/usr/sbin', '/usr/bin']      
}

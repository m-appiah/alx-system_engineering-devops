#Install flask version 2.1.0 from pip3 using Puppet
#First install werkzeug

package { 'werkzeug':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}

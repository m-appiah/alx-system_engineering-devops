#Install flask version 2.1.0 from pip3 using Puppet

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

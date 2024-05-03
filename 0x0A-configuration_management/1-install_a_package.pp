# 1-install_a_package.pp

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/flask --version | grep "Flask 2.1.0"',
  require => Package['python3-pip'],
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
  unless  => '/usr/bin/flask --version | grep "Werkzeug 2.1.1"',
  require => Package['python3-pip'],
}

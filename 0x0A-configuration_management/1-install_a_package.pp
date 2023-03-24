# Install Flask via pip3
# Version: 2.1.0

# Set provider for package to pip3
Package { provider => 'pip3' }

# Install Flask package with version 2.1.0
package { 'Flask':
  ensure => '2.1.0',
}

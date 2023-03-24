# This Puppet manifest creates a file named "school" in the /tmp directory with the content "I love Puppet",
# file permission of 0744, owner www-data, and group www-data.

file { '/tmp/school':
    ensure  => file,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
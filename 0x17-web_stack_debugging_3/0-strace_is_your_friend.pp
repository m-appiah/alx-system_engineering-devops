# Fixes typographical error in the file extension phpp instead of php in
# the file location 'wp-settings.php'

$file = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${file}",
  path    => ['/bin','/usr/bin']
}

# creates a custom HTTP header response
exec { 'command':
  command  => 'apt -y update;
  apt -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell
}

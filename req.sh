#Install Django and MySql

#Note: during the installation of mysql-server, you will be prompted for a root password. Use this in the section below.

sudo apt-get install python-django
sudo apt-get install mysql-server
sudo apt-get install python-mysqldb

#Set up a MySql database and user

#Note, use the password you entered when installing MySql
echo "CREATE DATABASE @DATABASE_NAME;"|mysql -u root --password=@PASSWORD
echo "GRANT ALL ON @DATABASE_NAME.* TO '@USERNAME'@'localhost' IDENTIFIED BY '@PASSWORD';"|mysql -u root --password=@PASSWORD
echo "EXIT"|mysql -u root --password=@PASSWORD

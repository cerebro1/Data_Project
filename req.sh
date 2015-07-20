#Install Django and MySql

#Note: during the installation of mysql-server, you will be prompted for a root password. Use this in the section below.

sudo apt-get install python-django
sudo apt-get install mysql-server
sudo apt-get install python-mysqldb

#Set up a MySql database and user

#Note, use the password you entered when installing MySql
echo "CREATE DATABASE $DATABASE_NAME;"|mysql -u $Mysql_USER --password=$Mysql_PASS
echo "GRANT ALL ON $DATABASE_NAME.* TO '$USER_NAME'@'localhost' IDENTIFIED BY '$PASS';"|mysql -u $Mysql_USER --password=$Mysql_PASS
echo "EXIT"|mysql -u $Mysql_USER --password=$Mysql_PASS

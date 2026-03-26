#!/bin/bash

sudo apt update
sudo apt install default-jre -y
cd /opt
name="apache-tomcat-10.1.49"
if [ -d "$name" ]
then
        cd /opt/apache-tomcat-10.1.49/bin/
        ./startup.sh
        sudo su - ubuntu
        git clone https://github.com/vinayak432/hello-world-war.git
        cd hello-world-war
        mvn clean package
        sudo cp /home/ubuntu/hello-world-war/target/hello-world-war-1.0.0.war /opt/apache-tomcat-10.1.49/webapps/
        sudo su -
        cd /opt/apache-tomcat-10.1.49/bin
        ./shutdown.sh
        cd /opt/apache-tomcat-10.1.49/bin
        ./startup.sh

else
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.49/bin/apache-tomcat-10.1.49.tar.gz
tar -xvf apache-tomcat-10.1.49.tar.gz
cd /opt/apache-tomcat-10.1.49/bin/
./startup.sh
#check and edit the default port no
cd /opt/apache-tomcat-10.1.49/conf/
vi server.xml
cd /opt/apache-tomcat-10.1.49/conf/
#to add users edit the file 
vi tomcat-users.xml
#to give login access
cd /opt/apache-tomcat-10.1.49/webapps/manager/META-INF
vi context.xml
#cd /opt/apache-tomcat-10.1.49/webapps/host-manager/META-INF
cd /opt/apache-tomcat-10.1.49/webapps/host-manager/META-INF
vi context.xml
cd /opt/apache-tomcat-10.1.49/bin
./shutdown.sh
./startup.sh
su - ubuntu
git clone https://github.com/vinayak432/hello-world-war.git
cd hello-world-war
 mvn clean package
cp /home/ubuntu/hello-world-war/target/hello-world-war-1.0.0.war /opt/apache-tomcat-10.1.49/webapps/

sudo su - root
cd /opt/apache-tomcat-10.1.49/bin
./shutdown.sh
cd /opt/apache-tomcat-10.1.49/bin
./startup.sh
fi

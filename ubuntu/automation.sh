#!/bin/bash

sudo apt update
sudo apt install default-jre -y
cd /opt
sudo wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.49/bin/apache-tomcat-10.1.49.tar.gz
sudo tar -xvf apache-tomcat-10.1.49.tar.gz
cd apache-tomcat-10.1.49 
cd bin
./startup.sh
cd /opt
cd apache-tomcat-10.1.49 
cd conf/
#check the default port no
#vi server.xml
cd /opt
cd apache-tomcat-10.1.49 
cd conf/
#edit default port no
#vi server.xml
#to add users edit the file 
#vi tomcat-users.xml
#to give login access
cd ..
cd webapps/manager/META-INF# 
#vi context.xml
cd webapps/host-manager/META-INF# 
#vi context.xml
cd log
./shutdown.sh
./startup.sh
cd /home/ubuntu
git clone https://github.com/efsavage/hello-world-war
cd hello-world-war
mvn clean package
cd target
sudo cp /hello-world-war/target/hello-world-war-1.0.0.war /opt/apache-tomcat-10.1.49/webapps/
cd ../..
sudo su -
cd /opt
cd apache-tomcat-10.1.49
cd bin
./shutdown.sh
./startup.sh




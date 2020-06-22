# arca
1. On the Docker Host make sure docker is up and running
Docker can be installed on machine depending on your linux distro
if unbuntu the run 

$apt-get install docker-ce docker-cli

$service docker start
if centos/redhat/fedora

$yum install docker-ce docker-cli

$service docker start

clone this repository by running 

$git clone https://github.com/tocy1/arca.git

$cd arca

$chmod +x docker.sh

2. The python script can only be executed if you have the python runtime
After installing python on machine execute

$python  python-script.py  {start|stop}<instance-id>
 
Instance-id is the id of AWS instance you want to start or stop
N/B before using script make sure you configure your credentials by installing aws cli and running below

$aws configure
 


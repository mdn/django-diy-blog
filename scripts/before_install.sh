#!/bin/bash

sudo yum update -y

sudo yum install git -y
sudo yum install python3-pip python3-devel python3-setuptools -y

DIR="/home/ec2-user/app"
if [ -d "$DIR" ]; then
  echo "${DIR} exists"
else
  echo "Creating ${DIR} directory"
  mkdir ${DIR}
fi

sudo chmod -R 777 /home/ec2-user/app
cd /home/ec2-user/app

pip3 install -r requirements.txt
python3 manage.py migrate
#!/bin/bash

sudo yum update -y

sudo yum install git -y
sudo yum install python3-pip python3-devel python3-setuptools -y

DIR="/home/ubuntu/app"
if [ -d "$DIR" ]; then
  echo "${DIR} exists"
else
  echo "Creating ${DIR} directory"
  mkdir ${DIR}
fi

sudo chmod -R 777 /home/ubuntu/app
cd /home/ubuntu/app


pip3 install -r requirements.txt
python3 manage.py migrate
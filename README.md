# AWS-SQS-Demo

Overview
--------

AWS-SQS-Demo is an simple Python3 application for demonstration the use of AWS
Simple Queue Service.

This program runs a web service, on port 5000, to send messages to SQS and load
the queued messages.


Installation
------------

Main dependency is Python platform. On any GNU/Linux Distribution is installed
by default. On Windows and OSX platforms can be downloaded and installed from
official website: https://www.python.org/downloads/

Install Python package manager, Pip. 

For Debian GNU/Linux based system::

	apt-get install python3-pip

For Red hat based::

	yum install python3-pip
  
For Windows, open a command window (cmd):

	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	py get-pip.py


Download AWS-SQS-Demo:

Get latest release from https://github.com/fgclaramonte/AWS-SQS-Demo/releases/tag/v0.1
or clone the repository https://github.com/fgclaramonte/AWS-SQS-Demo.git
 
Uncompress and go to source dir::

	tar xvfz AWS-SQS-Demo-0.1.tar.gz
	(or unzip)
	
	cd AWS-SQS-Demo-0.1
	

Install AWS-SQS-Demo::

	pip3 install -r requirements.txt

	

Run AWS-SQS-Demo Web Service
----------------------------

First, AWS credential is needed to access to SQS.

For credential settings, the folder /aws must be copied to user home folder.

In Linux/OSX Systems::

	cp -r aws ~/.aws
	
In Windows:

	Copy to C:\Users\ username \. aws
	
Now, edit .aws/credentials file with Key id and secret key provided by the AWS
user account.::

	[profile1]
	aws_access_key_id=XXXXXXXXXXXX
	aws_secret_access_key=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

If you need a testing access, please contact me.


To run HTTP service::

	python3 server.py
	

Usage
-----

To load next message in the queue, with GET method:

http://localhost:5000/api/v1/messages

To send new messages to the queue, with POST method:

http://localhost:5000/api/v1/send 

with parameter message="<new message>"


Support
-------

Please if you need some help or support to install or run this service, request for help at:
francisco@garciac.es
Or at my telephone number.

Thank you, hope you agree with this implementation.

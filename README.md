# QAPython

# Introduction
This web application is intended to serve as a task management tool to manage your time and your daily tasks.

# Prerequisites
- Python 3.7 or higher

# Running app locally
In order to run the web application locally all you need to do is run the virtual environmnet by running the command:

if you are running on linux

    source env/bin/activate
    
 or if you are running on windows
 
    .\env\bin\activate.ps1

Once you have activated the virtual environment you can run the command 

    python app.py

If it states that some packages are missing you can install the predefine list as so

    pip install -r requirements.txt

# Extra info for running app on EC2
Currently the app is set to run on port 5000 but in order to run the app on EC2 and be visible through http (port 80) you need to reverse proxy the port 5000 to 80. You can do this by first installing nginx by running the command

    sudo yum install nginx -y

Then update nginx config file to reverse proxy port 5000 to 80. You should be able to find the file at `etc/nginx/conf.d/flask_app.conf` and then modify the config but running

    sudo nano flask_app.conf

If you can not see the find you can just create one.

Next, to check your config looks good you can run the following command

    sudo nginx -t

This should confirm your config has correct syntax.

Finally, execute the following command to reverse the proxy

    sudo systemctl restart nginx

Once this is complete you can follow the Running app locally instructions to run the app on AWS EC2

# Running Unit Test
In order to run the unit tests your can run the command 

    python -m unittest .\tests\test_app.py

# Troubleshooting
If you are having issues with running the project and you are encountering issues that state you do not have python, pip or any other tools installed you can remove the env folder by running

    rm -rf env

and then recreate your virtual environment by running the following command

     python -m venv env

Once you have recreated your environment then activate your virtual environmnet by running the following command:

if you are running on linux

    source env/bin/activate
    
 or if you are running on windows
 
    .\env\bin\activate.ps1

and then re install your packages by running the command

    pip install -r requirements.txt
# nsb-fsms
Application for Learning tasks and assignment/tracker

This is a web application developed and tested using:
- Ubuntu Server 18.04, Python 3.6, Django 3.0.6, PostgresSQL 12.5

Prequisites: 
1. An Ubuntu desktop or server (18.04 or 20.04)
2. The latest version of Python
 
Follow the following steps to set up the web application on your own machine. 

1. Go to user directory
2. Create a folder with your project name and cd into to that folder
3. Create python virtual environment using: ``python -m venv [your_env_name]``
4. Activate the new virtual environment using: ``source your_env_name/bin/activate``
5. Install Django using: ``pip install django``
6. Download the source code from this repo with: ``git clone <this repo>`` or download the zip file and extract it to the project folder created above
7. Run: ``pip install -r requirements.txt`` (make sure to inlcude path to the requirements.txt file, if needed)
8. Go to settings file and add the host ip in ALLOWED_HOSTS (eg: ALLOWED_HOSTS = ['127.0.0.1'] )  (settings file is located in the innermost project folder)
9. Create the following folder structure for static files:
	-- static_in_env under project folder
	--- static_root, media_root under static_in_env
	
10. Run: python manage.py collectstatic (to copy all the static files from project static folder to the above newly created environment static folders)
11. Run: python manage.py makemigrations (to see all the migrations that will happen)
12. Run: python manage.py migrate (to complete the migrations to DB)
13. Run: python manage.py createsuperuser to create a super user (follow the prompts to complete user creation)
14. run: python manage.py runserver host_ip:8000 (eg: python manage.py runserver 127.0.0.1:8000)
15. In a browser type: host_ip:8000 and login with the username and password (created in above step) (127.0.0.1:8000)
16. Create/Update Tasks and use the application as needed.


In Bash window:

create and activeate virtual environment:
$ python -m venv virt
$ source virt/Scripts/activate

to deactiveate virtural environment:
$ deactiveate

to intsall flask:
$ pip install flask

to see what is installed:
$ pip freeze

creat first python file:
touch hello.py

run flask app in development mode:
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
$ flask --app hello --debug run

----------- GitHub -----------------
" Create an ssh key for windows users "

$ cd ~/ 
$ pwd
$ mkdir .ssh
$ cd .ssh
$ clear
$ ssh-keygen.exe
(hit enter)
(hit enter)
(hit enter)
$ ls
$ cat id_rsa.pub
( copy and past key to GitHub account)

# Before pushing project to GitHub we need to exclude the virtual environment
$ touch .gitignore
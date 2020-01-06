#! /bin/bash
# mod : creating python 3 virtual environment
# cre : lwx 20190926
# upd : lwx 20190926
# ver : 1.0

CBLUE="\x1b[34;1m"
CRED="\x1b[31;1m"
CGREEN="\x1b[32;1m"
CYELLOW="\x1b[33;1m"
CRESET="\e[0m"
TMENU="\e[1;101;93m"
TERR="\e[1;40;97m"
THIDE="\e[8m"


CreaPyEnv() {
  virtualenv -p python3 env
  source env/bin/activate
  pip install gunicorn
  pip install bottle
  pip install pillow
  pip install pytz
  pip install python-dateutil
  pip install requests
  pip install requests-toolbelt
  pip install psycopg2-binary
  pip install XlsxWriter
  #pip install boto
  #pip install rethinkdb
  #pip install appdirs
  #pip install pyparsing
  pip install websockets
  pip install Cython
  pip install xmltodict
  pip install DateTime
  deactivate
}

CreaPyEnv
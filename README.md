# InstaAd for Waive

website is at preview.waivescreen.com for now

Current "public" site is at waivescreen.com

## Current API Endpoints

http://staging.waivescreen.com/api/campaign_history?id=[number_of_campaign_id]

http://staging.waivescreen.com/api/sensor_history

http://staging.waivescreen.com/api/campaigns

## What keeps the server going
Gunicorn (A python3 module that) keeps the python files in check and supervisor (apt install program) keeps gunicorn constantly running. 
#### Restart the server with 
```
sudo systemctl restart nginx
```
Restarting supervisor
```
sudo supervisorctl reload
```
This [link](https://stackoverflow.com/questions/18859063/supervisor-socket-error-issue) is helpful regarding configuring supervisor 

supervisor constantly runs the command 
```
gunicorn -w 3 run:app
```

## pip modules to install for web
__Recomennded to be done using a venv__
* flask
* flask_sqlalchemy
* flask_bcrypt
* flask_wtf

### Steps for setting up venv
Run these commands in the shell
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## "Updating the database" (only temp till we switch to a prod database)
Good to run this from the virtual env
run python3 at the root of the project
```
from website import create_app, db
from website.models import User, Campaign # not necessary but you will most likely want it
app = create_app()
ctx = app.app_context()
ctx.push()
#Database manipulations here
#...
ctx.pop()  # exit from the app
exit()
```

## Server directories
* django server code - /home/dango_code
* current wordpress server - /var/www (will be removed soon)
* functions - /var/www/html/wp-content/themes/Avada/functions.php
* database entry - /etc/pyfiles/etc/database_entry.py
* turn info to html - /etc/pyfiles/get_db_create_ad.py

## Production vs Development
In order to update the server or set up a develpment server these things should be done. _This is due to be changed so it wont be so tedious_.
* Get rid of the website/config_local.py if you're on production 
	* If you're on development then change config_local.py to config.py
Config file is in /etc/config.json

### Flow

The landing page is essentially:

```
  You can promote with your existing Instagram account Instantly on our Magical Screens
  Anybody can do it
  No Agency Required
  No Credit Card required
  No hidden fees

  And it's just 1 button.
  This button, right here!

  <button>
  Yes that one
```
The important part are:
  
  * It's magical. 
  * Most people think you mean "ad agency" - we need to eliminate that
  * It has to be automatic on top of a flow they are already doing
  * It can't look to be expensive.

After that you log in then.

```
  your promotion just played in Culver City
  Your instagram has XX free plays left

  Want more?
  Want to customize?

  Finish your account setup

    email / password / credit card
```

The important parts are:

  * A visceral response that the ad already happened
  * Something that can be visualized of what actually happened
  * An endorphine/dopamine loop that helps to hook people to the status
  * The actual convergence of getting payment info and email.
  * Not talking about unit economics or how affordable something is.

The last one is important: If you offer a decent product at a decent price you shouldn't
have to emphasize that fact ... "show not tell".


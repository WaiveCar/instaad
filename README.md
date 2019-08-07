# InstaAd for Waive

website is at preview.waivescreen.com for now

Current "public" site is at waivescreen.com

## Current API Endpoints

http://staging.waivescreen.com/api/campaign_history?id=[number_of_campaign_id]

http://staging.waivescreen.com/api/sensor_history

http://staging.waivescreen.com/api/campaigns

## pip modules to install for web
* virtualenv
* django
* flask
* sqlalchemy

## Server directories
* django server code - /home/dango_code
* current wordpress server - /var/www (will be removed soon)
* functions - /var/www/html/wp-content/themes/Avada/functions.php
* database entry - /etc/pyfiles/etc/database_entry.py
* turn info to html - /etc/pyfiles/get_db_create_ad.py

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
  Your promo has 25 free plays left

  Want more?
  Want to customize?

  Finish your account setup
```


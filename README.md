# money_exchange_bot_backend
## Description
This project was created in order to automate the work of an administrator at a currency exchange office in Sri Lanka for Russians.
- Dynamic rate based on data received via the Binance API.
- Realized referral system.
- The logic of the bot and data storage is divided into services. Synchronous realized by API. 
- Admin and user have different interface

This service stores data and logic of work. Interface for working with Telegram API on a separate service. You can find it on this link:
https://github.com/Todvaa/money_exchange_bot

## Launch  
1. Install requirements in the virtual environment.
<br><pre>pip install requirements.txt</pre><br>
2. Run the migrations.  
<br><pre>python manage.py migrate</pre><br> 
***Make sure that a user with the number 0 has been created in the database in the table "exchange_user".
3. Start server.
<br><pre>python manage.py runserver</pre><br>

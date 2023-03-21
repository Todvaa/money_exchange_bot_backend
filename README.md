# money_exchange_bot_backend
## Description
This project was created in order to automate the work of an administrator at a currency exchange office in Sri Lanka for Russians.
The logic of the bot and data storage is divided into services. Synchronous realized by API.
[Documentation](doc.json).  
This service stores data and logic of work. Interface for working with Telegram API on a separate service. You can find it on this link:
https://github.com/Todvaa/money_exchange_bot

## Launch  
1. Install requirements in the virtual environment.
<br><pre>pip install requirements.txt</pre><br>
2. Create and fill out a file ".env"
<br><pre>cp .env.dist .env</pre><br>
3. Run the migrations.  
<br><pre>python manage.py migrate</pre><br> 
4. Start server.
<br><pre>python manage.py runserver</pre><br>
 
 ## TODO
- Сontainerize in docker
- Using queues where it necessary

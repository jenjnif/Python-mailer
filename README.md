# Python-mailer
A quick set-up python mailer with example emails and schedule file, based on the [codeschool python weather forecast mailer](https://www.codeschool.com/screencasts/build-a-python-weather-forecast-mailer).

Contents:
- an example email list with first and last names
- an example schedule
- a Python file which pulls in the email list and schedule to send an email

To use this:
1. you will need to change all emails in the emails2.txt file and the from_email (currently from_email = 'youremail@mailer.com') in the emailer.py file
2. you will also need to add an API key within the emailer.py file. Details below:

To include the weather API in your email:
In the emailer.py file there is an API call to the [Open Weather Map](https://openweathermap.org/api). 

You will need to [create an API key](https://openweathermap.org/price) to use this and then add it onto the URL in the code after the = at the end
For example the URL for London weather in Celsius would be the following URL plus your own API key after the =: http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid= 

I used the current weather in London, in Celsius. You can change features such as the place, whether it is metric (Celsius) or imperial (Fahrenheit) etc. Help with this can be found here: https://openweathermap.org/current

Email example output will look something like this:


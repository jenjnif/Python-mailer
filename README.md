# Python-mailer
A quick set-up python mailer with example emails and schedule file - built to send a weather forecast and daily schedule in an email to listed recipients. It is based on the [codeschool python weather forecast mailer](https://www.codeschool.com/screencasts/build-a-python-weather-forecast-mailer).

Email example output will look something like this:

![Example email output](/example_output.png)

Contents:
- an example email list with first and last names
- an example schedule
- 3 Python files - the main Python mailer file (emailer.py) and two module files: weather.py and mailer.py

To use this:
1. you will need to change all emails in the emails2.txt file and the change the from_email in the mailer.py file (currently from_email = 'youremail@mailer.com') to whichever email address you would like to send the emails.
2. you will also need to add an API key within the weather.py file. Details below:

To include the weather API in your email:

In the weather.py file there is an API call to the [Open Weather Map](https://openweathermap.org/api). 

You will need to [create an API key](https://openweathermap.org/price) to use this and then add it onto the URL after the = at the end.
For example the URL for London weather in Celsius would be the following URL plus your own API key after the =: http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid= 

I used the current weather in London, in Celsius. You can change features such as the place, whether it is metric (Celsius) or imperial (Fahrenheit) etc. Help with this can be found here: https://openweathermap.org/current

import requests
import smtplib

def get_emails():
	# reads each email address into a dictionary
	emails = {}

	# try is good to catch an error when a file name is not found
	try:
		# opens the email list file
		email_file = open('emails2.txt', 'r')

		# reading the lines from the email list file
		for line in email_file:
			# creates a tuple of email and name by splitting at the comma
			(email, name) = line.split(',')
			# creates an entry in dictionary. Setting emails[key] equal to the value, which is name
			emails[email] = name.strip()

	except FileNotFoundError as err:
		print(err)

	return(emails)

def get_schedule():
	try:
		# read file as one string
		schedule_file = open('schedule.txt', 'r')

		# reads the entire contents of the file
		schedule = schedule_file.read()
	except FileNotFoundError as err:
		print(err)

	return(schedule)

def get_weather_forecast():
	# you need to get an api key from the weathermap and then add this after the = at the end
	url = 'http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid='
	weather_request = requests.get(url)
	weather_json = weather_request.json()

	print(weather_json)

	description = weather_json['weather'][0]['description']
	print(description)
	temp_min = weather_json['main']['temp_min']
	temp_max = weather_json['main']['temp_max']
	print(temp_min)
	print(temp_max)

	forecast = 'The London forecast for today is ' 
	forecast += description + ' with a high of ' + str(temp_max)
	forecast += ' celcius and a low of ' + str(temp_min) + " celcius."

	return(forecast)

def send_emails(emails, schedule, forecast):
	# connect to the smtp server
	server = smtplib.SMTP('smtp.gmail.com', '587')
	
	# start TLS encription
	server.starttls()

	# login
	password = input('What is your password?')
	from_email = 'youremail@mailer.com'
	server.login(from_email, password)

	# send to entire email list
	for to_email, name in emails.items():
		message = "Subject: Welcome to your day\n"
		message += "Hi " + name + ",\n\n"
		message += forecast + "\n\n"
		message += "Your schedule for today is:\n"
		message += schedule + "\n\n"
		message += "Hope you have a great day!"
		server.sendmail(from_email, to_email, message)
	
	server.quit()

def main():
	emails = get_emails()
	print(emails)
 
	schedule = get_schedule()
	print(schedule)

	forecast = get_weather_forecast()
	print(forecast)
	
	send_emails(emails, schedule, forecast)

main()



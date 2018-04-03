import weather
import mailer

def get_emails():
	# Reading emails from a file
	# Reads each email address and puts it into a dictionary
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
	# Reading the schedule from a file
	try:
		# read file as one string
		schedule_file = open('schedule.txt', 'r')

		# reads the entire contents of the file
		schedule = schedule_file.read()
	except FileNotFoundError as err:
		print(err)

	return(schedule)

def main():
	emails = get_emails()
 
	schedule = get_schedule()
	
	# need to add weather. to let it know to use the weather module
	# containing the weather function
	forecast = weather.get_weather_forecast()
	
	# need to add mailer. to let it know to use the mailer module
	# containing the mailer function
	mailer.send_emails(emails, schedule, forecast)

main()

	
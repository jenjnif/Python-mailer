import smtplib

def send_emails(emails, schedule, forecast):
	# Connect to the smtp server
	server = smtplib.SMTP('smtp.gmail.com', '587')
	
	# Start TLS encription
	server.starttls()

	# Login - remember not to add your password to a GitHub repo
	password = input('What is your password?')
	from_email = 'youremail@mailer.com'
	server.login(from_email, password)

	# Send to entire email list
	for to_email, name in emails.items():
		message = "Subject: Welcome to your day\n"
		message += "Hi " + name + ",\n\n"
		message += forecast + "\n\n"
		message += "Your schedule for today is:\n"
		message += schedule + "\n\n"
		message += "Hope you have a great day!"
		server.sendmail(from_email, to_email, message)
	
	server.quit()
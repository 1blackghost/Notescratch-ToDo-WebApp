def send_email(theusername,theemail):
	print('sending mail...')
	import smtplib, ssl
	link="https://notescratch.pythonanywhere.com/dash"
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "notescratchonline@gmail.com"  # Enter your address
	receiver_email = str(theemail)
	print('recall',str(theemail)) # Enter receiver address
	password = 'kaepkrryzjvbvwks'
	SUBJECT="Notescratch"
	TEXT='''Hi,{} Thank you for using Notescratch!.We are really eager to see you setup another note!.Come back to see your notes.And what we have held you so far!Come Back NOW!!Link Below..

		 \nThis is a system generated message don't reply!'''.format(str(theusername))+str('\n')+str(link)+str("\n\nTEAM NOTESCRATCH")
	message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

	context = ssl.create_default_context()
	try:
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		    server.login(sender_email, password)
		    server.sendmail(str(sender_email), str(receiver_email), str(message))
		print('mail sent')
	except Exception as e:
		print(str(e))

with open('reset.txt','w') as f:
    f.write('[]')
with open('user.txt','r') as f:
	d=eval(f.read())
for i in d:
	send_email(str(i[0]),str(i[1]))

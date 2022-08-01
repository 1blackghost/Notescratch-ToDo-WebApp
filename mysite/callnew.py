def call_new(theusername,theemail):
	print('sending mail...')
	import smtplib, ssl
	link="https://notescratch.pythonanywhere.com"
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "notescratchonline@gmail.com"  # Enter your address
	receiver_email = str(theemail)
	print('advert ',str(theemail)) # Enter receiver address
	password = 'xhlrdrtngmvckyyz'
	SUBJECT="NOTESCRATCH: ONLINE PRIVATE NOTES!"
	TEXT='''Hi,{} Create and save your plans!,Write diaries,Write Notes!Have you thought of writing notes and diaries...And Donot feel secure ! Trying to save it online and donot know where to? Here at notescracth we will save your notes and diaries secure and safe..Try NOW!.Link Below..

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
with open('/home/notescratch/justF.txt') as f:
    d=f.readlines()
for i in d:
    call_new('',str(i))
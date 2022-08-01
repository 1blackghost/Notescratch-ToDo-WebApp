from flask import Flask,render_template,request,redirect,url_for,session
import random
import flask
import hashlib
import datetime
from flask import send_file

app=Flask(__name__)
app.secret_key='823r5y834htiutsdbvuhbvidbvdfbvjdsfvbksadbvksbvhbvkfbvdfbvkdfbvkdfvbdfvbdfkhvbkdfjvbdfbvdfbvkhdfbvkdhfbvefbvdfbgviuerhfgi8uergiugkrtnvkjfbhghrtkjgnrtkjgnifhguhergkjfenkvjhdafivgeajtb refmoisdhcgvsdjfberjgiuf vshfnierfhufhvadsfjvoefhighevjnkfgnirehghrgkjgfgvty457y94okvjieurvhvkdfngiq45yt5hturv  4'

@app.route('/forget_password/<name>',methods=['GET','POST'])
def thereset(name):
	if request.method=="POST":
		newpassword=request.form.get('passw')
		confirm=request.form.get('password')

		if newpassword==confirm:
			if len(newpassword)>5:

				with open('user.txt','r') as f:
					d=eval(f.read())
				for i in d:
					if session['reset'] in i:
						i[3]=str(newpassword)
				with open('user.txt','w') as f:
					f.write(str(d))
				session['user']=str(session['reset'])
			elif len(newpassword)<5:
			    return render_template('donelink.html',err="Passwords Too Short!")
		else:
		    return render_template('donelink.html',err="Passwords Don't Match!")


		return redirect(url_for('dash'))
	else:
		with open('reset.txt','r') as f:

			r=eval(f.read())
		if name=="":
			return redirect(url_for('login'))
		else:
			found=False
			with open('reset.txt','r') as f:
				va=eval(f.read())
			for i in va:
				if str(name) in str(i):
					va.remove(i)
					session['reset']=str(i[0])
					found=True
			if found:
				with open('reset.txt','w') as f:
					f.write(str(va))
				for i in r:
					if str(name)==i[2]:
						return render_template('donelink.html')
			else:
				return redirect(url_for('login'))


def send_email1(theusername,theemail):
	print('sending mail...')
	import smtplib, ssl
	link="https://notescratch.pythonanywhere.com/dash"
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "notescratchonline@gmail.com"  # Enter your address
	receiver_email = str(theemail)
	print('recall',str(theemail)) # Enter receiver address
	password = 'bimaamlgvhnatwhr'
	SUBJECT="Notescratch"
	TEXT='''Hi,{} Welcome to NOTESCRATCH!,We are happy to see a new signup..Notescratch helps you to create new notes and save important dairy entries.Fast,Reliable and Secure!.Make sure you Read the terms and conditions in the link below! We are happy to see you come back again!. To comeback directly click the link below.Thank you for using NOTESCRATCH Links Below..

		 \nThis is a system generated message don't reply!'''.format(str(theusername))+str('\n')+str('TERMS: https://www.termsfeed.com/live/fc78c91c-0da9-4c29-a8e4-442a6d8efd41')+str('\n')+str('DASHBOARD: https://notescratch.pythonanywhere.com/dash')+str("\n\nTEAM NOTESCRATCH")
	message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

	context = ssl.create_default_context()
	try:
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(str(sender_email), str(receiver_email), str(message))
		print('mail sent')
		return True
	except Exception as e:
		print(str(e))
		return False
def send_email(theusername,theemail,hashed):
	print('sending mail...')
	import smtplib, ssl
	link="https://notescratch.pythonanywhere.com/forget_password/"+str(hashed)
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "notescratchonline@gmail.com"  # Enter your address
	receiver_email = str(theemail)
	print('RESET LINK SEND TO',str(theemail)) # Enter receiver address
	password = 'bimaamlgvhnatwhr'
	SUBJECT="Notescratch"
	TEXT='''Hi,{} Thank you for using Notescratch!.This email gives you access for the reset of your password at notescratch.Don't share this link.You Can only use the link only once!.Hope you enjoy our service! Any Trouble?Send us feedback! Reset Link Below....

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

@app.route('/forget_password',methods=['GET','POST'])
def forget_password():
	if request.method=="POST":
		useron=False
		theusername=""
		theemail=""
		thename=request.form.get('name')
		if thename=="":
			return render_template('forget_password.html',err="Null Entry!")
		else:
			with open('user.txt') as f:
				d=eval(f.read())
			for i in d:

				if (str(thename)==i[0]) or (str(thename)==i[1]):
					useron=True
					theusername=str(i[0])
					theemail=str(i[1])


			if not useron:
				return render_template('forget_password.html',err="User Doesn't Exists!")

			if useron:
				plist=[]
				with open('reset.txt','r') as f:
					values=eval(f.read())
				for i in values:
					if str(thename) in i:
						return render_template("forget_password.html",err="Link Already Sent! If It Doesn't Reach Please wait!")
				stringforhash="abcd365ef3333ghijklmnopqrs34333tuvwxyz1289798!@#$%^3455767777&*()_+*&*&^&*&^^3468768684734783758734658347583745687346587345687634875jhsbvijefvibvkjfvjfvije$#%*&&^(*&jvhvnuh ;;vc  efthryj"
				hashstring=""
				for i in range(1,30):
					hashstring=stringforhash[random.randint(1,40)]+hashstring
				hashed=str(hashlib.md5(str(hashstring).encode('utf-8')).hexdigest())
				plist.append(str(theusername))
				plist.append(str(theemail))
				plist.append(str(hashed))
				values.append(plist)
				with open('reset.txt','w') as f:

					f.write(str(values))
				send_email(theusername,theemail,hashed)
				return render_template('resetlink.html',err="Reset Link Has Been Sent To Your Email!")



	return render_template('forget_password.html',err="")
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/customize',methods=['GET','POST'])
def customize():
	if 'user' in session:
		if request.method=="POST":
			if request.form.get('submit'):
				color=request.form.get('color')
				family=request.form.get('family')
				fontsize=request.form.get('fontsize')
				background=request.form.get('background')
				with open('customize.txt','r') as f:
					dirt=eval(f.read())
				exists=False
				for i in dirt:
					if session['user'] in i:
						exists=True
						i[1]=fontsize
						i[2]=family
						i[3]=color
						i[4]=background

				with open('customize.txt','w') as f:
					f.write(str(dirt))
				return redirect(url_for('dash'))
			if request.form.get('back'):
				return redirect(url_for('dash'))
		return render_template('customize.html')
	else:
		return redirect(url_for('login'))
@app.route('/delete')
def delete():
	if 'user' in session:
		with open(session['user']+'.save','r') as f:
			the=eval(f.read())
		try:
			the.remove(session['opener'])
		except:
			return redirect(url_for('dash'))
		with open(session['user']+'.save','w') as f:
			f.write(str(the))
		session.pop('opener',None)

		return redirect(url_for('dash'))
	else:
		return render_template('login')
@app.route('/change')
def change():
	if 'user' in session:

		category = request.args.get('type')
		session['opener']=str(category)
		return redirect(url_for('dash'))
	else:
		return redirect(url_for('views'))
@app.route('/views')
def views():
	if 'user' in session:
		with open(session['user']+'.save','r') as f:
			red=eval(f.read())
		return render_template('views.html',docs=red)
	else:
		return redirect(url_for('login'))
@app.route('/')
def landintg():
	return render_template("index.html")
@app.route('/help')
def help():
	if 'user' in session:
		return render_template('help.html')
	else:
		return redirect(url_for('login'))
@app.route('/logout')
def logout():
	session.pop('opener',None)

	session.pop('user',None)
	return redirect(url_for('login'))
@app.route('/loginerror',methods=['GET','POST'])
def loginerror():
	if request.method=='POST':
		name=request.form.get('name')
		password=request.form.get('password')
		with open('user.txt','r') as f:
			cred=eval(f.read())
		authen=False
		for i in cred:
			if (i[0]==name or i[1]==name) and i[3]==password:
				session['user']=name
				authen=True
				print("LOGGED IN:",name)

				return redirect(url_for('dash'))

		if not authen:
			return redirect(url_for('loginerror'))


	else:
		return render_template('loginerror.html')
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		name=request.form.get('name')
		password=request.form.get('password')
		with open('user.txt','r') as f:
			cred=eval(f.read())
		authen=False
		for i in cred:
			if (i[0]==name or i[1]==name) and i[3]==password:
				session['user']=name
				authen=True
				print("LOGGED IN:",name)
				return redirect(url_for('dash'))

		if not authen:
			return redirect(url_for('loginerror'))


	else:
		return render_template('login.html')
def convert(filename):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    f = open('/home/notescratch/'+str(filename)+'.txt', "r")
    for x in f:
        pdf.cell(100,10, txt = x, ln = 1, align = 'C')
    pdf.output('/home/notescratch/'+str(filename)+'.pdf')
@app.route('/dash',methods=['POST','GET'])
def dash():
	if request.method=='POST':
		if request.form.get('log'):
			return redirect(url_for('logout'))
		if request.form.get('cus'):
			return redirect(url_for('customize'))
		if request.form.get('p'):
			text=request.form.get('t')
			if 'opener' in session:
				with open(session['opener']+'.txt','w') as f:
					f.write(str(text))

			else:
				with open(session['user']+'.txt','w') as f:
					f.write(str(text))
			convert(str(session['opener']))
			return send_file(str('/home/notescratch/')+str(session['opener'])+str('.pdf'),as_attachment=True)
		if request.form.get('d'):
			return redirect(url_for('delete'))
		if request.form.get('w'):
			return redirect(url_for('views'))
		if request.form.get('n'):
			text=request.form.get('t')
			if 'opener' in session:
				with open(session['opener']+'.txt','w') as f:
					f.write(str(text))

			else:
				with open(session['user']+'.txt','w') as f:
					f.write(str(text))
			try:
				open(str(session['user'])+'.save','r')
			except:
				with open(str(session['user']+'.save'),'w')as f:
					f.write(str('[]'))
			with open(session['user']+'.save','r') as f:
				readed=eval(f.read())
			datestr=str(datetime.datetime.now())
			readed.append(datestr)
			with open(session['user']+'.save','w') as f:
				f.write(str(readed))
			with open(datestr+'.txt','w') as f:
				f.write('')
			session['opener']=str(datestr)


		if request.form.get('s'):
			text=request.form.get('t')
			if 'opener' in session:
				with open(session['opener']+'.txt','w') as f:
					f.write(str(text))

			else:
				with open(session['user']+'.save','r') as f:
					redee=eval(f.read())
					vals=eval(f.read())
					valslen=len(vals)-1
					r=redee[varlslen]
				session['opener']=str(r)
				with open(session['opener']+'.txt','w') as f:
					f.write(str(text))
	if 'user' in session:
		try:
			with open(session['user']+'.save','r') as f:
				vals=eval(f.read())
				valslen=len(vals)-1
				default=vals[valslen]
		except:
			with open(session['user']+'.save','w') as f:
				vals=""
				f.write(str('[]'))

		if vals=="":
			datestr1=str(datetime.datetime.now())
			open(datestr1+'.txt','x')
			with open(datestr1+'.txt','w') as f:
				f.write('')
			with open(session['user']+'.save','r') as f:
				readed=eval(f.read())
			readed.append(datestr1)
			session['opener']=str(datestr1)
			with open(session['user']+'.save','w') as f:
				f.write(str(readed))

		try:
			with open(session['opener']+'.txt','r') as f:
				readvalue=f.read()
		except:
			with open(session['user']+'.save','r') as f:
				vals=eval(f.read())
				valslen=len(vals)-1
				default=vals[valslen]
				session['opener']=str(default)
			with open(session['opener']+'.txt','r') as f:
			    readvalue=f.read()
		greet='>'+session['user']+'>'+str(session['opener'])
		with open('customize.txt','r') as f:
			dirt=eval(f.read())
		exists=False
		for i in dirt:
			if session['user'] in i:
				exists=True
				fontsize=i[1]
				family=i[2]
				color=i[3]
				background=i[4]
		if not exists:
			this=[]
			fontsize=60
			family="cursive"
			color="black"
			background="white"
			for i in dirt:
				this.append(str(session['user']))
				this.append(str(fontsize))
				this.append(str(family))
				this.append(str(color))
				this.append(str(background))
			dirt.append(this)
		with open('customize.txt','w') as f:
			f.write(str(dirt))

		return render_template('dash.html',fontsize=fontsize,username=greet,r=readvalue,color=color,background=background,family=family)

	else:
		return redirect(url_for('login'))
@app.errorhandler(404)
def page_error(e):
	return render_template("error404.html")
@app.route('/signup',methods=['GET','POST'])
def signup():
	ip_address = flask.request.remote_addr
	try:
		error=session['temp']
	except:
	    error=""
	if request.method=='POST':
		name=request.form.get('name')
		email=request.form.get('email')
		mobile="NIL"
		password=request.form.get('password')
		confirm_password=request.form.get('c')
		state=False
		x=send_email1(str(name),str(email))
		if x:
		    state=True
		with open('user.txt','r') as f:
			users=eval(f.read())
		for i in users:
			for j in i:
				if j==name:
					session['temp']=" Name Already Exists.Try Another!"
					return redirect(url_for('signup'))
				if j==email:
					session['temp']=" Email Already Exists.Try Another!"
					return redirect(url_for('signup'))


		if name=='':
			session['temp']="Name Is Required!"
			return redirect(url_for('signup'))
		if state==False:
			session['temp']="Email Is Invalid"
			return redirect(url_for('signup'))
		if len(password)<6:
			session['temp']='Password Doesnt Support Required Security!6>chars'
			return redirect(url_for('signup'))
		if password=='' or confirm_password=='':
			session['temp']='Password Field Must Be Entered!'
			return redirect(url_for('signup'))
		if password!=confirm_password:
			session['temp']='Passwords Donot Match'
			return redirect(url_for('signup'))
		else:
			l=[]
			l.append(name)
			l.append(email)
			l.append(mobile)
			l.append(password)
			users.append(l)
			with open('user.txt','w') as f:
				f.write(str(users))
			session['temp']=""
			with open('temp'+str(ip_address),'w') as f:
				f.write('')
			session['user']=name

			return redirect(url_for('dash'))

	else:
		return render_template('signup.html',error=error)
if __name__=='__main__':
	app.run(debug=True)

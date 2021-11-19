#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys , subprocess , os ,requests,string,random,datetime
from faker import Faker

# from browser_ import *
# import smtplib
import re
gmail_user = 'binhunt3r@gmail.com'  
gmail_password = 'agoon007'
sent_from = gmail_user  
to = ['binhunt3r@gmail.com']  


###########################################################
proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050',}
domains=["@artiganovitch.com","@cicada3301.de","@tarfacha.com"]
reasonableCharacters = (string.digits + string.ascii_letters )

def password0(minimum=10, maximum=14):
    return ''.join(
        random.choice(reasonableCharacters) for x in range(
            random.randint(minimum, maximum)
        )
    )




###########################################################
def gmail(msg):
  
  subject0 = 'COOL'
  ooof=re.sub(r':.+?:', '', msg)
  body = ooof+"\n"

  email_text = """\
  From: %s  
  To: %s  
  Subject: %s
  %s
  """ % (sent_from, ", ".join(to), subject0, body)
  try:  
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(gmail_user, gmail_password)
      server.sendmail(sent_from, to, email_text)
      server.close()

      print ('Email sent!')
  except:  
      print ('Something went wrong...')
###########################################################
###########################################################
def call_ip0():
	s = requests.Session()
	s.proxies = proxies
	r = s.get('https://api.ipify.org')
	#print(r.text)
	m_ip=r.text
	return m_ip
###########################################################
###########################################################
def url_open_start():
	driver=(start_driver ())
	return driver
	#rotatator(driver)
###########################################################
def generate_name_add():
	geo_info=[]

	while True:

		fake_a = Faker('en_US')
		adrees_com=fake_a.address()
		street_add=	adrees_com.split("\n")
		street0=street_add[0]
		date_if_birth=fake_a.date_time_between(start_date="-40y",end_date="-20y")
		date_if_birth=date_if_birth.date()
		date_if_birth=date_if_birth.strftime('%d-%m-%Y')

		if "," in street_add[1]:
			city_a=street_add[1].split(",")
			city_=city_a[0]
			zop=city_a[1].split()
			country=zop[0]
			zip00=zop[1]
			break
	while True:
  		fake = Faker('en_US')
  		name_j=fake.name().lower()
  		name2_j=name_j.replace(" ","")
  		timestamp = datetime.datetime.now()
  		vary=password0(2,2)
  		#vva2=random.choice(reasonableCharacters) 
  		t =  str(timestamp.second)+vary
  		email_ja=name_j.replace(" ",t)
  		if len(email_ja) <= 16:
  			#print(t)
  			dom=random.randint(1,len(domains))
  			user_do=email_ja
  			password_do=password0(8,12)
  			real_name=name_j.lower()
  			email_do=email_ja+domains[dom-1]
  			geo_info.append(password_do)
  			geo_info.append(real_name)
  			geo_info.append(date_if_birth)
  			geo_info.append(zip00)
  			geo_info.append(email_do)
  			geo_info.append(user_do)
  			geo_info.append(street0)
  			geo_info.append(city_)
  			geo_info.append(country)
  			#geo_info.append(city_)
  			#geo_info.append(country)
  			#geo_info.append(zip00)
  			#print(geo_info)
  			# print(geo_info)
  			#return user_do,password_do,email_do,real_name,street0,city_,country,zip00  			
  			return geo_info
  			break

  		else :
  			continue
###########################################################

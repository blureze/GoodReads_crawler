# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup

def login(login_url, session_requests):
	initial(login_url, session_requests)
	logindata = read_secret()

	formdata = {
		'user[email]': logindata['email'], 
		'user[password]': logindata['password'],
		'authenticity_token': authenticity_token,
		'n': hidden_n
	}

	result = send_form(formdata, login_url)

	return result	

def initial(login_url, session_requests):
	result = session_requests.get(login_url)
	content = result.text
	soup = BeautifulSoup(content, "html.parser")
	authenticity_token = soup.find('input', {'name': 'authenticity_token'}).get('value')
	hidden_n = soup.find('input', {'name': 'n'}).get('value')

def read_secret():
	with open('config/secret.json', 'r', encoding='utf-8') as data_file:
	    data = json.load(data_file)

	print data
	logindata = {'email': data['email'], 
				'password': data['password']}

	return logindata

def send_form(formdata, login_url):
	result = session_requests.post(
		login_url,
		data = formdata
	)

	if result.status_code == 200:
		print 'successfully login'
	else:
		print "Logging failed"

	return result
# -*- coding: utf-8 -*-
import requests

from login import login

website_url = 'https://www.goodreads.com'
login_url = 'https://www.goodreads.com/user/sign_in'
session_requests = requests.Session()
result = login(login_url, session_requests)


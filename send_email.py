import smtplib, ssl  # this is going to produce a module that helps us define an smtp client session so that we actually send an email/ ssl provides the security for us)
import os
port = 465
smtp_server = "smtp.gmail.com"

USERNAME = os.environ.get('USER_EMAIL')   # we're utilizing env varibale to secure the creds
PASSWORD = os.environ.get('USER_PASSWORD')
message = """\
Subject: Github Email report
This is your email notification"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
  server.login(USERNAME,PASSWORD) # logging into smtp server
  server.sendmail(USERNAME,USERNAME, message) # sending it to ourself

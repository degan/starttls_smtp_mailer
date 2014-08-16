#! /usr/bin/python

import smtplib,sys,argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Parse args
parser = argparse.ArgumentParser(description='STARTTLS sender test')
parser.add_argument('to', help='Email to send test')
parser.add_argument('account', help='Email to send email from, usually account specific')
parser.add_argument('server', help='Mail Server Address')
parser.add_argument('port', help='Mail Server Port')
parser.add_argument('username', help='Account username credentials')
parser.add_argument('password', help='Account password credentials')
parser.add_argument('starttls', help='yes or no to force starttls')
args = parser.parse_args()

print "Starting STARTTLS sender test..."

#Message Container
msg = MIMEMultipart('alternative')
msg['Subject'] = "Email Test" 
msg['From'] = args.account
msg['To'] = args.to 

#Text and HTML messages
text = "Hi!"
html = "<html><head></head><body><p>Hi!</p></body></html>"

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

#Connect
s = smtplib.SMTP(args.server, args.port)
s.set_debuglevel(1)

#STARTTLS
if 'yes' in args.starttls:
    s.starttls()
    s.ehlo() #smtplib documentation recommends an ehlo after starttls

#Authenticate
s.login(args.username, args.password)

#send
s.sendmail(msg['From'], msg['To'], msg.as_string())

s.quit()

print "End STARTTLS sender test"

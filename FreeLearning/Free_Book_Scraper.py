# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
try:
    import urllib.request as request
    import urllib.parse as parse
except ImportError:
    import urllib2 as request
    import urlparse as parse
import re
from keys import sender, email_list, key_gmail_user, key_gmail_pwd

url = 'https://www.packtpub.com/packt/offers/free-learning'
subject = 'Packt Free Learning Daily Offer - '

def send_email(subject, message):
    msg = MIMEText(message, 'html')
    _from = sender
    _to = email_list
    msg['Subject'] = '{}'.format(subject)
    msg['From'] = _from
    msg['To'] = _to[0]

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    gmail_user = key_gmail_user
    gmail_pwd = key_gmail_pwd 
    smtpserver = smtplib.SMTP_SSL("smtp.gmail.com",465)
    smtpserver.ehlo()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    smtpserver.sendmail(_from, _to, msg.as_string())
    smtpserver.quit()
    return'Email sent!'


req = request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
page = request.urlopen(url)

soupysoupsoup = BeautifulSoup(page)
book_title = soupysoupsoup.find('div', class_='dotd-title').h2.text.encode('utf-8')
#direct_link = soupysoupsoup.findAll('div', class_={'float-left','free-ebook'})[-1].form.attrs['action'] #CAPTCHA prevents this being useful
description = [x for x in soupysoupsoup.find('div', class_ = {'dotd-main-book-summary'}).children][-4].get_text().strip().encode('utf-8')
img = soupysoupsoup.find('img', class_='bookimage imagecache imagecache-dotd_main_image')

book_title = re.sub(r'[\n\t]','', book_title)
# PlainText Version
# message = '{}\n\n{}\n\n\nVisit Page: {}\n\n\n'.format(book_title,description, url)
subject += book_title

message = '''
<html>
    <head><title>{}</title></head>
    <body>
        <div>
            <div style='text-align:center; float: left; width: 350px'>
                <a href="{}" target="_blank" >
                    <img src="http:{}" alt="Oops! Image Missing!" width=150px />
                </a>
            </div>

            <div style='text-align:center;'>
               <h1>{}</h1>

            <div style='text-align:left; font-size:12pt'>
                {}
            </div>
            <br >
            <div>
                <a href="{}" target="_blank"
                style="font-size:x-large; background-color: #2e3191; color: white; padding: 10px 20px;
                        text-align: center; text-decoration: none; display: inline-block;">
                    Download Here
                </a>
            </div>

        </div>


  </body>
</html>
'''.format(subject, url, img['src'], book_title, description,url)

send_email(subject, message)

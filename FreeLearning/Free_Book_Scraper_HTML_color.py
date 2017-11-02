import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
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

page = request.urlopen(req)

soupysoupsoup = BeautifulSoup(page, 'lxml')
book_title = soupysoupsoup.find('div', class_='dotd-title').h2.text
img = soupysoupsoup.find('img', class_='bookimage imagecache imagecache-dotd_main_image')
description = [x for x in soupysoupsoup.find('div', class_ = {'dotd-main-book-summary'}).children][-4].get_text().strip()

im = Image.open(request.urlopen('http:'+img['src']))

# Finds Two most common colors in image to color the button in the email.
NUM_CLUSTERS = 5

im = im.resize((150, 150))      # optional, to reduce time
ar = scipy.misc.fromimage(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2])

codes, dist = scipy.cluster.vq.kmeans(ar.astype('double'), NUM_CLUSTERS)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max].astype('int')
second_peak = codes[scipy.argsort(counts)[-2]].astype('int') # find second most frequent
max_colour = ''.join(format(c, '02x') for c in peak)
second_colour = ''.join(format(c, '02x') for c in second_peak)

book_title = re.sub(r'[\n\t]','', book_title)
subject += book_title

message = '''
<html>
    <head><title>{}</title></head>
    <body>
        <div style="display:none;font-size:1px;color:#333333;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;">
          Today's Free Learning E-Book is {}. Download directly at {}.
        </div>
        <div>
            <div style='text-align:center; float: left; width: 350px'>
                <a href='{}' target='_blank'>
                   <img src="http:{}" alt="Oops! Image Missing!" width=150px />
                </a>
            </div>

            <div style='text-align:center'>
               <h1>{}</h1>

            <div style='text-align:left; font-size:13pt'>
                {}
            </div>
            <br >
            <div>
                <a href="{}" target="_blank" style="font-size:x-large; background-color: #{}; color: #{}; font-weight: bold; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block;">
                    Download Here
                </a>
            </div>

        </div>


  </body>
</html>
'''.format(subject, book_title, url, url, img['src'], book_title, description,url,max_colour,second_colour)

#message = '{}\nDirect Link: {}\n\nVisit Page: {}'.format(book_title, parse.urljoin(url, direct_link), url)


send_email(subject, message)

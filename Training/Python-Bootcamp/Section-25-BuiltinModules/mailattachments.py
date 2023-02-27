import smtplib
from email.message import EmailMessage
from pathlib import Path

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

html_content = Path('test_email.html').read_text()

# email = EmailMessage()
email = MIMEMultipart()

email['from'] = 'a <a.bc@gmail.com>'  # enable less secure apps from the account
email['to'] = 'shay.m@gmail.com'
email['subject'] = 'Good job Python!'

# email.set_content('Wow! Congratulations!')
# email.set_content(html_content, 'html')
email.attach(MIMEText(html_content, 'html'))

filename = 'python.pdf'
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment;filename={filename}')
    email.attach(part)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('a.bc@gmail.com', 'srghswuoiehd23')  # username & password
    smtp.send_message(email)
    print('The mail was sent!')

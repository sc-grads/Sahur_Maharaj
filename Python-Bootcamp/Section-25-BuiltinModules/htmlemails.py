import smtplib
from email.message import EmailMessage
from pathlib import Path

html_content = Path('test_email.html').read_text()  # <-- path to html file in local path

email = EmailMessage()
email['from'] = 'a <a.bc@gmail.com>'  # enable less secure apps from the account
email['to'] = 'shay.m@gmail.com'
email['subject'] = 'Good job Python!'


# email.set_content('Wow! Congratulations!')
email.set_content(html_content, 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('a.bc@gmail.com', 'srghswuoiehd23')  # username & password
    smtp.send_message(email)
    print('The mail was sent!')


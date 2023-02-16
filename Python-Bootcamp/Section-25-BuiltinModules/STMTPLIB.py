import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'a <a.bc@gmail.com>'  # enable less secure apps from the account
email['to'] = 'shay.m@gmail.com'
email['subject'] = 'Good job Python!'

email.set_content('Wow! Congratulations! \n This email is send with Python.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # says hi to the server
    smtp.starttls()  # encrypt connection
    smtp.ehlo()  # close server

    smtp.login('a.bc@gmail.com', 'srghswuoiehd23')  # username & password
    smtp.send_message(email)
    print('The mail was sent!')

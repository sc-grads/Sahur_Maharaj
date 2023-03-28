import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Sahur <Sahur.M@outlook.com>'  # enable less secure apps from the account
email['to'] = 'sahur.maharaj@gmail.com'
email['subject'] = 'Good job Python!'

email.set_content('Wow! Congratulations! \n This email is send with Python.')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()  # says hi to the server
    smtp.starttls()  # encrypt connection
    smtp.ehlo()  # close server

    smtp.login('Sahur.M@outlook.com', 'AZERTY1!')  # username & password
    smtp.send_message(email)
    print('The mail was sent!')

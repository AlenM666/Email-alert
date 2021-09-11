import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    #email to send from 
    user = "Enter here -- gmail.com"
    msg['from'] = user
    password = "your password"

    #google mail 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    #The entered mail will recive the message
    email_alert("hey", "hello world", "Enter email here")


import smtplib
from email.message import EmailMessage


def send_email(mail, subject, mssg):
    email = EmailMessage()
    email['from'] = 'PORTFOLIO.Tazribine'
    email['to'] = 'tazribinehassan1998@gmail.com'
    email['subject'] = subject
    content = f"from: {mail} \n {mssg}"
    email.set_content(content)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('tazribine98@gmail.com', 'hassan@1998')
        smtp.send_message(email)

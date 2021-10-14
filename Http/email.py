from smtplib import SMTP, SMTPException
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'weishaodaren@gmail.com'
    receivers = ['zhaojiawei@keyush.info']
    message = MIMEText('This is fuckin read', 'plain', 'utf-8')
    message['From'] = Header('from WEISHAODAREN', 'utf-8')
    message['TO'] = Header('to zjw', 'utf-8')
    message['Subject'] = Header('EMAIL', 'utf-8')
    try:
        smtper = SMTP('localhost')
        smtper.login(sender, 'haha')
        smtper.sendmail(sender, receivers, message.as_string())
        print('Done')
    except SMTPException:
        print('Error')


if __name__ == '__main__':
    main()
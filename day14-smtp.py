from email import message
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'ancdefg@outlook.com'
    receivers = ['uvwxyz@qq.com', 'ucsad@qq.com']
    message = MIMEText('内容', 'plain', 'utf8')
    message['From'] = Header('大佬', 'utf8')
    message['To'] = Header('采购', 'utf8')
    message['Subject'] = Header('Title', 'utf8')
    smtper = SMTP('smtp.126.com')

    smtper.login(sender, 'password')
    smtper.sendmail(sender, receivers, message.as_string())
    print('comp')


if __name__ == '__main__':
    main()

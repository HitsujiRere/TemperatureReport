
import os
from datetime import datetime
from dotenv import load_dotenv

from email.utils import formatdate
from email.mime.text import MIMEText
import smtplib

from TemperatureReport import report


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


def create_message(from_addr: str, to_addr: str, subject: str, body: str):
    """
    メッセージを作成する
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg


def send_mail(from_addr: str, my_password: str, to_addr: str, body_msg):
    """
    メールを送る
    """
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    # smtpobj.set_debuglevel(True)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(from_addr, my_password)
    smtpobj.sendmail(from_addr, to_addr, body_msg.as_string())
    smtpobj.close()


if __name__ == '__main__':
    userid = os.environ.get('USER_ID')
    password = os.environ.get('PASSWORD')

    result = report(userid, password)

    if not result[0]:
        print(result[1])

        mail_to = os.environ.get('MAIL_TO')
        mail_address = os.environ.get('MAIL_ADDRESS')
        mail_password = os.environ.get('MAIL_PASSWORD')
        body_msg = '本日の検温報告を失敗しました．\n{}'.format(result[1])
        msg = create_message(mail_address, mail_to, '検温報告失敗', body_msg)
        send_mail(mail_address, mail_password, mail_to, msg)

from celery import *
from celery import Celery
import smtplib
from decouple import config
import logging

app = Celery('myapp', broker='redis://localhost:6379/0')

logger = logging.getLogger('tasks_logger')
logging.basicConfig(
    level=logging.INFO,
    filename="tasks-log_file.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt='%H:%M:%S',
)
@app.task
def send_mail_celery(email_ad, text):
    user = config("USER_SMTP_EMAIL")
    passwd = config("USER_SMTP_PASS")
    logger.info(f'Отправлен email на адрес: {email_ad} с текстом: {text}')
    server = "smtp.yandex.ru"
    port = 587
    subject = "Тестовое письмо."
    to = "sirotkin.nikola@mail.ru"
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'
    text = text

    body = "\r\n".join((f"From: {user}", f"To: {to}",
                        f"Subject: {subject}", mime, charset, "", text))

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user, passwd)
        smtp.sendmail(user, to, body.encode('utf-8'))
    except smtplib.SMTPException as err:
        logger.error(err)
        raise err
    except Exception as error:
        logger.error(error)
    finally:
        smtp.quit()

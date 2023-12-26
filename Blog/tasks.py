from celery import *
from celery import Celery
import smtplib

app = Celery('myapp', broker='redis://localhost:6379/0')


@app.task
def send_mail_celery(email_ad, text):
    print(f'Отправлен email на адрес: {email_ad} с текстом: {text}')

    user = "sirotos@yandex.ru"
    passwd = "*****************"
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
        print(err)
        raise err
    finally:
        smtp.quit()

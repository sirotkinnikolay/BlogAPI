# Create your tasks here
from celery import *
from celery import Celery
import smtplib

app = Celery('myapp', broker='redis://localhost:6379/0')


@app.task
def test_celery(email_ad, text):
    print(f'Отправлен email на адрес: {email_ad} с текстом: {text}')

    # Скрипт для отправки сообщения на почту пользователя, подписанного на автора
    # email = 'my_email@mail.ru'
    # password = 'my_password'
    #
    # server = smtplib.SMTP('smtp.yandex.ru', 587)
    # server.ehlo()
    # server.starttls()
    # server.login(email, password)
    #
    # dest_email = email_ad
    # subject = 'Subscription message'
    # email_text = text
    # message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (email, dest_email, subject, email_text)
    #
    # server.set_debuglevel(1)
    # server.sendmail(email, dest_email, message)
    # server.quit()

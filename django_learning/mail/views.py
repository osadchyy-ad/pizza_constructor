from email.mime.text import MIMEText
from django.http import HttpResponse
import smtplib


def mail(request):
    if request.method == 'POST':
        detail = dict(request.POST.lists())
        fullname = detail['name'][0]
        email = detail['email'][0]
        total = detail['total'][0]
        phone = detail['phone'][0]
        send_email(email, fullname, total, phone)
        return HttpResponse('<h2>Заказ отправлен в обработку!</h2>')


def send_email(email, fullname, total, phone):
    email_msg = MIMEText('Подтверждение Вашего заказа, {0}!\n'
                         'Итоговая сумма заказа: {1}\n'
                         'Указанный контактный номер телефона: {2}\n'
                         .format(fullname, total, phone).encode('utf-8'), _charset='utf-8')
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    smtp_obj.login('osadchyy.ad@gmail.com', 'IPS1300536feranos')
    smtp_obj.sendmail("osadchyy.ad@gmail.com", email, str(email_msg))

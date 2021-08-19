from string import Template  # p/ subs os placeholders do html
from datetime import datetime

from email.mime.multipart import MIMEMultipart  # padrão p/ o email
from email.mime.text import MIMEText    # corpo da msg
from email.mime.image import MIMEImage  # anexos de img

import smtplib

# dds dos email de origem e destino
FROM_EMAIL = ''
EMAIL_PASSWORD = r''
TO_EMAIL = ''

# le o template da msg
with open('template.html', 'r', encoding='utf-8') as file:
    template = Template(file.read())
    date = datetime.now().strftime('%d/%m/%Y')
    msg_template = template.substitute(name='Nina', date=date)

# config a msg
msg = MIMEMultipart()
msg['from'] = 'Nome'
msg['to'] = TO_EMAIL
msg['subject'] = 'Email automático Python.'

text = MIMEText(msg_template, 'html')
msg.attach(text)    # anexa o texto da msg

# le as imgs e anexa na mgs
with open('imgs/road.jpg', 'rb') as img, open('imgs/jaguar.jpg', 'rb') as img2, \
        open('imgs/eagle.jpg', 'rb') as img3:     # rb - readBytes
    img_to_send_1 = MIMEImage(img.read())
    msg.attach(img_to_send_1)
    img_to_send_2 = MIMEImage(img2.read())
    msg.attach(img_to_send_2)
    img_to_send_3 = MIMEImage(img3.read())
    msg.attach(img_to_send_3)

# envia o email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(FROM_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f'Email enviado com sucesso para: {TO_EMAIL}')
    except Exception as error:
        print(f'Email não enviado para {TO_EMAIL}')

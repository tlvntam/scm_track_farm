import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import numpy as np

from sqlalchemy import create_engine
from twilio.rest import Client

import random
import smtplib
from email.message import EmailMessage
import mimetypes
import datetime as dt

my_email = "tlvntamc2.pbchau@gmail.com"
my_password = "nhantam47"

with open("test.png", 'rb') as f:
    img_data = f.read()

msg = EmailMessage()
msg["Subject"] = "Demo"
msg["From"] = "tlvntamc2.pbchau@gmail.com"
msg["To"] = "nhatquang187@gmail.com"
msg.set_content("Test email")

mime_type, _ = mimetypes.guess_type('test.png')
mime_type, mime_subtype = mime_type.split('/')
with open('test.png', 'rb') as file:
    msg.add_attachment(file.read(),
                       maintype=mime_type,
                       subtype=mime_subtype,
                       filename='test.png')
print(msg)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(my_email, my_password)
server.send_message(msg)

FARM_1 = "+84344861145"
FARM_2 = "+84365021598"
FARM_3 = "+84562361344"

account_sid = "AC142fe016328a50048f4b45234c8bbca9"
auth_token = "789e98fb6815395c9ac0a52427802c02"

temperature = 10
humidity = 65
rain = 1300
light = 11000
ec = 0.5

# if temperature not in range(24, 30):
#     temp_mess = f"1.Farm_1's current temperature is: {temperature}°C ❌"
# else:
#     temp_mess = f"1.Farm_1's current temperature is: {temperature}°C ✔️"
#
# if humidity not in range(60, 70):
#     humid_mess = f"2.Farm_1's current humidity is: {humidity}% ❌"
# else:
#     humid_mess = f"2.Farm_1's current humidity is: {humidity}% ✔️"
#
# if temperature not in range(24, 30) or humidity not in range(60, 70):
#     full_mess = f"{temp_mess} \n{humid_mess}"
#     print(full_mess)
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body=f"{full_mess}",
#         from_="+12283386869",
#         to=FARM_2
#     )
#     print(message.status)

sqlEngine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/scmdemo', pool_recycle=3600)
farm1_data = pd.read_sql_table("farm1", sqlEngine)
farm2_data = pd.read_sql_table("farm2", sqlEngine)

temp1_value = 0
humid1_value = 0
rain1_value = 0
light1_value = 0
ec1_value = 0

for index, row in farm1_data.iterrows():
    temperature1 = farm1_data.loc[index, "temperature"]
    humidity1 = farm1_data.loc[index, "humidity"]
    rain1 = farm1_data.loc[index, "rain"]
    light1 = farm1_data.loc[index, "light"]
    ec1 = farm1_data.loc[index, "ec"]
    date1 = farm1_data.loc[index, "date"]

    if temperature1 not in range(24, 30):
        temp1_value += 1
    if humidity1 not in range(60, 70):
        humid1_value += 1
    if rain1 not in range(1250, 1850):
        rain1_value += 1
    if light1 not in range(10000, 15000):
        light1_value += 1
    if ec1 not in np.arange(0.2, 1.2, 0.1):
        ec1_value += 1

df = pd.DataFrame({'lab': ['Temperature', 'Humidity', 'Rain', 'Light', 'EC'],
                   'val': [temp1_value, humid1_value, rain1_value, light1_value, ec1_value]})
ax = df.plot.bar(x='lab', y='val', rot=0)

# plt.savefig('test.png')
# plt.show()

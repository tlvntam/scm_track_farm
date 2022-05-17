import pandas as pd
import sqlalchemy
import numpy as np
from twilio.rest import Client
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
import mimetypes


FARM_1 = "+84365021598"
FARM_2 = "+84344861145"
FARM_3 = "+84562361344"

account_sid = "ACabedf0a9d15114f8c70b7664915166c4"
auth_token = "ff3a659df73608b84f910ecc2f5f19f8"
twilio_num = "++19804002319"

sqlEngine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/scmdemo', pool_recycle=3600)
farm1_data = pd.read_sql_table("farm1", sqlEngine)
farm2_data = pd.read_sql_table("farm2", sqlEngine)
# print(farm1_data)

"""Sending SMS to Farm 1"""
for index, row in farm1_data.iterrows():
    temperature1 = farm1_data.loc[index, "temperature"]
    humidity1 = farm1_data.loc[index, "humidity"]
    rain1 = farm1_data.loc[index, "rain"]
    light1 = farm1_data.loc[index, "light"]
    ec1 = farm1_data.loc[index, "ec"]
    date1 = farm1_data.loc[index, "date"]
    if temperature1 not in range(24, 30):
        temp1_mess = f"1.Farm_1's current temperature is: {temperature1}°C ❌"
    else:
        temp1_mess = f"1.Farm_1's current temperature is: {temperature1}°C ✔️"

    if humidity1 not in range(60, 70):
        humid1_mess = f"2.Farm_1's current humidity is: {humidity1}% ❌"
    else:
        humid1_mess = f"2.Farm_1's current humidity is: {humidity1}% ✔️"

    if rain1 not in range(1250, 1850):
        rain1_mess = f"3.Farm_1's current rain is: {rain1}mm ❌"
    else:
        rain1_mess = f"3.Farm_1's current rain is: {rain1}mm ✔️"

    if light1 not in range(10000, 15000):
        light1_mess = f"4.Farm_1's current light is: {light1}Lux ❌"
    else:
        light1_mess = f"4.Farm_1's current light is: {light1}Lux ✔️"

    if ec1 not in range(0, 2):
        ec1_mess = f"5.Farm_1's current ec is: {ec1}mS/cm ❌"
    else:
        ec1_mess = f"5.Farm_1's current ec is: {ec1}mS/cm ✔️"

    if temperature1 not in range(24, 30) or humidity1 not in range(60, 70) or rain1 not in range(1250, 1850) or light1 not in range(10000, 15000) or ec1 not in range(0, 2):
        full1_mess = f"WARING AT {date1}\n{temp1_mess}\n{humid1_mess}\n{rain1_mess}\n{light1_mess}\n{ec1_mess}"
        print(full1_mess)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{full1_mess}",
            from_=twilio_num,
            to=FARM_3
        )
        print(message.status)

"""Sending SMS to Farm 2"""
for index, row in farm2_data.iterrows():
    temperature2 = farm2_data.loc[index, "temperature"]
    humidity2 = farm2_data.loc[index, "humidity"]
    rain2 = farm2_data.loc[index, "rain"]
    light2 = farm2_data.loc[index, "light"]
    ec2 = farm2_data.loc[index, "ec"]
    date2 = farm2_data.loc[index, "date"]
    if temperature2 not in range(24, 30):
        temp2_mess = f"1.Farm_2's current temperature is: {temperature2}°C ❌"
    else:
        temp2_mess = f"1.Farm_2's current temperature is: {temperature2}°C ✔️"

    if humidity2 not in range(60, 70):
        humid2_mess = f"2.Farm_2's current humidity is: {humidity2}% ❌"
    else:
        humid2_mess = f"2.Farm_2's current humidity is: {humidity2}% ✔️"

    if rain2 not in range(1250, 1850):
        rain2_mess = f"3.Farm_2's current rain is: {rain2}mm ❌"
    else:
        rain2_mess = f"3.Farm_2's current rain is: {rain2}mm ✔️"

    if light2 not in range(10000, 15000):
        light2_mess = f"4.Farm_2's current light is: {light2}Lux ❌"
    else:
        light2_mess = f"4.Farm_2's current light is: {light2}Lux ✔️"

    if ec2 not in range(0, 2):
        ec2_mess = f"5.Farm_2's current ec is: {ec2}mS/cm ❌"
    else:
        ec2_mess = f"5.Farm_2's current ec is: {ec2}mS/cm ✔️"

    # if temperature2 not in range(24, 30) or humidity2 not in range(60, 70) or rain2 not in range(1250, 1850) or light2 not in range(10000, 15000) or ec2 not in range(0, 2):
    #     full2_mess = f"WARING AT {date2}\n{temp2_mess}\n{humid2_mess}\n{rain2_mess}\n{light2_mess}\n{ec2_mess}"
    #     print(full2_mess)
    #     client = Client(account_sid, auth_token)
    #     message = client.messages.create(
    #         body=f"{full2_mess}",
    #         from_=twilio_num,
    #         to=FARM_2
    #     )
    #     print(message.status)

"""Create BAR Chart"""
temp1_value = 0
humid1_value = 0
rain1_value = 0
light1_value = 0
ec1_value = 0

temp2_value = 0
humid2_value = 0
rain2_value = 0
light2_value = 0
ec2_value = 0

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
    if ec1 not in range(0, 2):
        ec1_value += 1

    temperature2 = farm2_data.loc[index, "temperature"]
    humidity2 = farm2_data.loc[index, "humidity"]
    rain2 = farm2_data.loc[index, "rain"]
    light2 = farm2_data.loc[index, "light"]
    ec2 = farm2_data.loc[index, "ec"]
    date2 = farm2_data.loc[index, "date"]

    if temperature2 not in range(24, 30):
        temp2_value += 1
    if humidity2 not in range(60, 70):
        humid2_value += 1
    if rain2 not in range(1250, 1850):
        rain2_value += 1
    if light2 not in range(10000, 15000):
        light2_value += 1
    if ec2 not in range(0, 2):
        ec2_value += 1

df = pd.DataFrame({'lab': ['Temperature', 'Humidity', 'Rain', 'Light', 'EC'],
                   'val1': [temp1_value, humid1_value, rain1_value, light1_value, ec1_value],
                   'val2': [temp2_value, humid2_value, rain2_value, light2_value, ec2_value]
                   })
ax1 = df.plot.bar(x='lab', y='val1', rot=0)
plt.savefig('farm1.png')
ax2 = df.plot.bar(x='lab', y='val2', rot=0)
plt.savefig('farm2.png')
# plt.show()

"""Create Report"""
my_email = "tlvntamc2.pbchau@gmail.com"
my_password = "nhantam47"

report_content = ""
farm1_report = "Farm 1 Report"
for index, row in farm1_data.iterrows():
    temperature1 = farm1_data.loc[index, "temperature"]
    humidity1 = farm1_data.loc[index, "humidity"]
    rain1 = farm1_data.loc[index, "rain"]
    light1 = farm1_data.loc[index, "light"]
    ec1 = farm1_data.loc[index, "ec"]
    date1 = farm1_data.loc[index, "date"]
    if temperature1 not in range(24, 30):
        farm1_report += f"\nAt {date1} Farm_1's temperature is: {temperature1}°C ❌ "
    if humidity1 not in range(60, 70):
        farm1_report += f"\nAt {date1} Farm_1's humidity is: {humidity1}% ❌ "
    if rain1 not in range(1250, 1850):
        farm1_report += f"\nAt {date1} Farm_1's rain is: {rain1}mm ❌ "
    if light1 not in range(10000, 15000):
        farm1_report += f"\nAt {date1} Farm_1's light is: {light1}Lux ❌ "
    if ec1 not in range(0, 2):
        farm1_report += f"\nAt {date1} Farm_1's ec is: {ec1}mS/cm ❌ "
# print(farm1_report)

farm2_report = "Farm 2 Report"
for index, row in farm2_data.iterrows():
    temperature2 = farm2_data.loc[index, "temperature"]
    humidity2 = farm2_data.loc[index, "humidity"]
    rain2 = farm2_data.loc[index, "rain"]
    light2 = farm2_data.loc[index, "light"]
    ec2 = farm2_data.loc[index, "ec"]
    date2 = farm2_data.loc[index, "date"]
    if temperature2 not in range(24, 30):
        farm2_report += f"\nAt {date2} Farm_2's temperature is: {temperature2}°C ❌ "
    if humidity2 not in range(60, 70):
        farm2_report += f"\nAt {date2} Farm_2's humidity is: {humidity2}% ❌ "
    if rain2 not in range(1250, 1850):
        farm2_report += f"\nAt {date2} Farm_2's rain is: {rain2}mm ❌ "
    if light2 not in range(10000, 15000):
        farm2_report += f"\nAt {date2} Farm_2's light is: {light2}Lux ❌ "
    if ec2 not in range(0, 2):
        farm2_report += f"\nAt {date2} Farm_2's ec is: {ec2}mS/cm ❌ "

report_content = farm1_report + "\n" + farm2_report
# print(report_content)
report_content_1 = "Farm 1 Report" \
                   "\nAt 2022-05-13 14:49:40 Farm_1's humidity is: 72.0% ❌ " \
                   "\nAt 2022-05-13 14:49:52 Farm_1's temperature is: 22.0°C ❌ " \
                   "\nAt 2022-05-13 14:49:52 Farm_1's rain is: 1967.0mm ❌ " \
                   "\nAt 2022-05-13 14:50:19 Farm_1's temperature is: 31.0°C ❌ " \
                   "\nAt 2022-05-13 14:50:19 Farm_1's light is: 15370.0Lux ❌ " \
                   "\nAt 2022-05-13 14:50:45 Farm_1's humidity is: 75.0% ❌ " \
                   "\nAt 2022-05-13 14:50:45 Farm_1's ec is: 2.0mS/cm ❌ " \
                   "\nFarm 2 Report" \
                   "\nAt 2022-05-13 14:49:23 Farm_2's rain is: 1933.0mm ❌ " \
                   "\nAt 2022-05-13 14:49:23 Farm_2's light is: 8986.0Lux ❌ " \
                   "\nAt 2022-05-13 14:49:23 Farm_2's ec is: 2.0mS/cm ❌ " \
                   "\nAt 2022-05-13 14:50:01 Farm_2's temperature is: 31.0°C ❌ " \
                   "\nAt 2022-05-13 14:50:01 Farm_2's rain is: 1124.0mm ❌ " \
                   "\nAt 2022-05-13 14:50:01 Farm_2's ec is: 2.0mS/cm ❌ " \
                   "\nAt 2022-05-13 14:50:11 Farm_2's humidity is: 73.0% ❌ " \
                   "\nAt 2022-05-13 14:50:11 Farm_2's rain is: 1945.0mm ❌ " \
                   "\nAt 2022-05-13 14:50:11 Farm_2's ec is: 2.0mS/cm ❌ " \
                   "\nAt 2022-05-13 14:50:45 Farm_2's rain is: 1196.0mm ❌ " \
                   "\nAt 2022-05-13 14:50:45 Farm_2's ec is: 2.0mS/cm ❌ "

# with open("farm1.png", 'rb') as f1:
#     img_data_1 = f1.read()
# with open("farm2.png", 'rb') as f2:
#     img_data_2 = f2.read()
# """Sending EMAIL REPORT"""
# msg = EmailMessage()
# msg["Subject"] = "Report from Farm"
# msg["From"] = "tlvntamc2.pbchau@gmail.com"
# msg["To"] = "chuoicungungdemo@gmail.com"
# msg.set_content(report_content_1)
#
# mime_type, _ = mimetypes.guess_type('test.png')
# mime_type, mime_subtype = mime_type.split('/')
# with open('farm1.png', 'rb') as file_1:
#     msg.add_attachment(file_1.read(),
#                        maintype=mime_type,
#                        subtype=mime_subtype,
#                        filename='farm1.png')
# with open('farm2.png', 'rb') as file_2:
#     msg.add_attachment(file_2.read(),
#                        maintype=mime_type,
#                        subtype=mime_subtype,
#                        filename='farm2.png')
# print(msg)
#
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login(my_email, my_password)
# server.send_message(msg)





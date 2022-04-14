import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

message = """
This is your OTP for COVBOT App s%s
""" % OTP

msg = message
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
smtp_email = 'sangchustark@gmail.com'
smtp_pass = '7984248787.Tyj'
s.login(smtp_email, smtp_pass)
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")

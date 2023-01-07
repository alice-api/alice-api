import alice_api
from alice_api import sms

#คำเตือน: เบอร์ต่างประเทศบางตัวอาจจะไม่สามารถใช้ได้กับ API ได้ดังนั้นควรใส่เบอร์โทรศัพท์ไทยดีกว่า
#Warning: Some foreign countries may not be compatible with the API, so it's better to include a Thai phone number.
phone = "191" #เบอร์โทรศัพท์/Phone Number

#คำเตือน: อย่าใส่จำนวนมากกว่า 20 มันจะทำให้เซิฟเวอร์มีปัญหา
#Warning: Do not put the number more than 20, it will cause the server problems.
amount = "1" #จำนวนที่ต้องการยิง/Amount to send

#คำเตือน: อย่าลบสิ่งนี้ไม่งั้นอาจจะทำให้ยิงไม่ได้
#Warning: Don't delete this, otherwise it might make a sms spammer.
sms.send(phone, amount)
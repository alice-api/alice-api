import alice_api
from alice_api import truewallet

#คำเตือน: ต้องไทยเบอร์ประเทศไทยเท่านั้น!
#Warning: Thai number only required!
phone = "085596918" #เบอร์โทรศัพท์/Phone Number

#คำเตือน: ไม่มี
#Warning: ไม่มี
link = "https://gift.truemoney.com/campaign/?v=asfasf" #ลิงค์ซองของขวัญ

#คำเตือน: อย่าลบสิ่งนี้ไม่งั้นอาจจะทำให้รับซองของขวัญไม่ได้
#Warning: Don't delete this, otherwise it might make a truewallet gift.
response = truewallet.send(phone, link)

if response['status']['code'] == "PHONEN_INCORRECT":
    print(f"เบอร์โทรศัพท์ไม่ถูกต้อง! / {response['status']['message']}")
elif response['status']['code'] == "VOUCHER_GIFT_INCORRECT":
    print(f"ซองของขวัญไม่ถูกต้อง! / {response['status']['message']}")
elif response['status']['code'] == "VOUCHER_NOT_FOUND":
    print(f"ซองของขวัญไม่ถูกต้อง! / {response['status']['message']}")
elif response['status']['code'] == "VOUCHER_OUT_OF_STOCK":
    print(f"ซองของขวัญมีคนรับไปแล้ว! / {response['status']['message']}")
elif response['status']['code'] == "VOUCHER_EXPIRED":
    print(f"ซองของขวัญไม่ถูกต้อง! / {response['status']['message']}")
elif response['status']['code'] == "SUCCESS":
    balance = response['data']['voucher']
    owner_profile = response['data']['owner_profile']
    if balance['amount_baht'] == balance['redeemed_amount_baht']:
        print(f"สำเร็จ รับเงินแล้ว {balance['redeemed_amount_baht']} และรับเงินจาก {owner_profile['full_name']} / Success Received {balance['redeemed_amount_baht']} and received money from {owner_profile['full_name']}")
    else:
        print(f"ซองของขวัญต้องรับได้แค่คนเดียวเท่านั้น / Gift can only be accepted by one person.")
else:
    print(f"ไม่สามารถรับซองของขวัญได้ / Can't accept gift")
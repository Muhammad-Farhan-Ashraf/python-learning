import string
import random
def ranstring(length):
    letters=string.ascii_letters + string.digits +string.punctuation
    result_let="".join(random.choice(letters) for i in range (length))
    print("Random string length", length ,"is" , result_let)
ranstring(12)
import qrcode
data = "GeeksforGeeks"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=qrcode.constants.ERROR_CORRECT_M
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='green', back_color='white')
img.save('MyQRCode2.png')
"""Guess number game"""
print(" Guess game, Lets start")
rnum=random.randint(0,100)
attempts=0
while True:
    guess=int(input("Write the number: "))
    attempts+=1
    if guess>rnum:
        print("Your number is greater")
    elif guess<rnum:
        print("Number is less")
    else:
        print("Finally you guessed the number in ", attempts, "attempts")
        break

from scipy import constants
a=constants.kilo
print(a)

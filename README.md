# Password-Generator
import random
import string

password_len=7
Charvalues=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(password_len):
   
   password=password+(random.choice(Charvalues))

print("your random pssword",password)


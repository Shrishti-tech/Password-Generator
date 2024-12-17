import random
import string

password_len=7
Charvalues=string.ascii_letters+string.digits+string.punctuation
# print(string.digits)
# print(string.punctuation)
#print(Charvalues)
password=""
for i in range(password_len):
   
   password=password+(random.choice(Charvalues))

print("your random pssword",password)

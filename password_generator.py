import random
n = int(input("enter lenght of password:"))
arr = []
for i in range(n):
    a = random.randint(33,126)
    arr.append(chr(a))

str = ''.join(arr)
print ("Machine generated password:\n",str)
str2 = input("Now enter the password:\n")
if str2 == str:
    print("password matched\nstrenghth of password:")
    if(len(str2)<=8):
        print("weak")
    elif(len(str2)==16):
        print("strong")
    elif(len(str2)>16):
        print("very strong")
else:
    print("password not matched")

import time
timestamp = time.strftime('%H,%M,%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
if(4<=timestamp<12):
    print('Good Morning')
elif(12>=timestamp<3):
    print('Good evening')
else:
    print('Good night ')

def isnumber():
    phone=input('Prvide your phone number:  ')
    if len(phone) != 10 or not phone.isdigit():
        print('Invalid phone number, make sure you enter 10 digit number')
    else:
        print('Phone number accepted')

message: ''' It was a quiet morning in the village of Willowbrook when Maya received a mysterious letter. The envelope was unmarked, but inside was a note that read, "The answers lie where the sun meets the sea, and the code is buried in plain sight: 8745297866." Confused but intrigued, she tucked the note into her journal and set off toward the coast. Along the way, she passed the old lighthouse, where she remembered her grandfather once told her stories of hidden treasures and secret messages. The wind whispered through the trees, almost as if it were guiding her toward something long forgotten.
As she reached the cliffs, the waves crashed below with a rhythm that seemed almost intentional. She sat on a rock, letting the breeze carry her thoughts, when she noticed a carving etched into the stone: "Trust the path, even when it’s unclear. 9813532025 will light the way." Her heart raced. Two numbers, two clues, and a growing sense that this was more than just a coincidence. Maya smiled, knowing that the adventure had only just begun. '''

for i in range (len(message)):
    chunk = message[i:i+12]
    if isnumber(chunk):
        print(f'Found number: {chunk}')
    else:
        print('Number not found')  
 
# -------------RegEx-------------

import re
phonenum=re.compile(r'\d\d\d\d\d\d\d\d\d')
message=phonenum.findall('''It was a quiet morning in the village of Willowbrook when Maya received a mysterious letter. The envelope was unmarked, but inside was a note that read, The answers lie where the sun meets the sea, and the code is buried in plain sight: 8745297866. Confused but intrigued, she tucked the note into her journal and set off toward the coast. Along the way, she passed the old lighthouse, where she remembered her grandfather once told her stories of hidden treasures and secret messages. The wind whispered through the trees, almost as if it were guiding her toward something long forgotten. As she reached the cliffs, the waves crashed below with a rhythm that seemed almost intentional. She sat on a rock, letting the breeze carry her thoughts, when she noticed a carving etched into the stone: Trust the path, even when it’s unclear. 9813532025 will light the way. Her heart raced. Two numbers, two clues, and a growing sense that this was more than just a coincidence. Maya smiled, knowing that the adventure had only just begun.''')
print(message)

batRE= re.compile(r'\bBat(?:man|cat|Mobile|rat|mat)\b')
mo=batRE.findall('My name is Batman and I have a BatMobile')
print(mo)


batad=re.compile('Bat(?:women|girl|lady)')
mo=batad.findall("Batwomen in the adventure of the worlds, they have Batgirl and Batlady from parallel universe as well")
print(mo)

ipadd=re.compile(r'\b(?:\d{1,3})\.(?:\d{1,3})\.(?:\d{1,3})\.(?:\d{1,3})')
mo=ipadd.findall("These are in standard IPv4 format 192.168.43.27 within private IP ranges 0.245.67.89 while others are public 172.16.254.1 or 203.0.113.76")

print(mo)

ipadd= re.compile(r'\b(?:\d{1,3}\.)(?:\d{1,3}\.)(?:\d{1,3}\.)(?:\d{1,3})')
mo=ipadd.findall("These are in standard IPv4 format 192.168.43.27 within private IP ranges 0.245.67.89 while others are public 172.16.254.1 or 203.0.113.76")

print(mo)

/d ---- digits 0-9
/w ---- words 
/s ---- Space 

?  --- group matches 0 or 1 times
*  --- group matches 0 or more times
+  --- group matches 1 or more times.
findall() --- find all matchs
^ --- matching anything other than. eg: re.compile(r'[^aeouwAEOUW]') --- will match everything except vowels
# -----open & read-----------
var=open('/path')
var.read()
var.close()
------open & write-------
var=open('/path', 'w')
write(Hello!!!)
var.close()
------open & append-------
var=open('/path', 'a')
write(Hello!!!)
var.close()

eg:
import re
song='''12 drummers drumming 11 pipers piping 10 lords a-leaping 9 ladies dancing 8 maids a-milking 7 swans a-swimming 6 geese a-laying 5 golden rings 4 calling birds 3 French hens 2 turtle doves'''

songreg=re.compile(r'\d+\s\w+')
xmas=songreg.findall(song)
print(xmas)

# ---------------------------OS----------------------------

import os

os.path.join('folder1','folder2','folder3')
os.path.abspath('py1.py')
os.path.dirname('c:/folder1/folder2/test.txt')
os.path.basename('c:/folder1/folder2/test.txt')
os.path.getsize('abspath of file')
os.getcwd()
os.chdir()
os.listdir('c:\\dir_name')
os.path.isfile()   ----to check if file exists (not dir)
os.makedirs()
os.rmdir() --to delete directory
os.remove() &  os.unlink()  --to delete file

-----------------copy&move----------------

import shutil

shutil.copy('c:\\USERS\\yenaik\\Desktop\test.txt', 'c:\\USERS\\yenaik\\Desktop\Study')
shutil.copytree('c:\\USERS\\yenaik\\Desktop\\Study', 'c:\\USERS\\yenaik\\Desktop\\My\ Data')  ---to copy entire directory
shutil.move()   ---to move and rename
shutil.rmtree('c:\\Folder')

--------------raise exception--------------
eg:
    if len(argument) != 1:
        raise Exception('argument should be a single character')

-----------random----------

import random
random.randint(0,15)

-------sys-------
import sys
sys.exit()           -- will break n exit program from here

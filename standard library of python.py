import array
arry= array.array('i', [1,2,3,4,5,6,7,8,9])
print(arry)



import math
print(math.sqrt(16))
print(math.pi)


import random
my_numb= random.randint(5,15)
print(my_numb)
name=['nini', 'vini','kiwi']
my_alpha= random.choice(name)
print(my_alpha)



##os
'''
Optimized tool selection or os
The os module is a core part of Python's standard library that provides a portable way to interact with the operating system. 
It allows you to perform tasks like:
Working with files and directories (e.g., creating, deleting, renaming files; listing directory contents)
Managing environment variables
Running system commands
Getting information about the current process or system (e.g., current working directory, platform details)
'''
import os
print(os.getcwd())#here cwd means current working directory

os.mkdir('test_directory')



##shutil
'''
The shutil module is another key part of Python's standard library, 
focused on high-level file and directory operations.
 It's short for "shell utilities" and provides functions for copying, moving,
   and removing files/directories in a cross-platform way.'''
import shutil
shutil.copyfile('source.txt', 'destination.txt')



##data serialization
'''
JSON stands for JavaScript Object Notation.
It is a format used to store and exchange data between programs, websites, APIs, apps, etc.
Think of it like a Python dictionary, but written in a universal format.'''
import json
data={'name':'nini',
      'age':18}
json_str=json.dumps(data)#means here the data type is getting dumped and new data type will be form
print(type(json_str))



##csv
import csv
with open('example.csv', mode='w',newline='')as file: #there is one more mode called w+ mode in which we can write and append
    writer= csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['nini',18])



##datetime
from datetime import datetime, timedelta
now=datetime.now()
print(now)
yesterday=now-timedelta(day=1)
print(yesterday)



## regular expression
'''
A Regular Expression (Regex) is a special pattern used to search, match, or replace text.
It helps you find specific text patterns inside strings.
In Python, regex is used with the built-in re module.
Here:
\d = digit (0-9)
+ = one or more times
So \d+ means:
👉 “find one or more digits”'''
import re
text = "My number is 9876543210"
result = re.search(r"\d+", text)
print(result.group())
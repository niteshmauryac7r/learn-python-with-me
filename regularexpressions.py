import re

pattern = r"[A-Z]ython"
text = '''To set a reminder notification in Python, 
you can use libraries like plyer or notify2 to display desktop notifications, 
and schedule or time to control Wython when the notification is triggered. 
The basic process involves importing necessary libraries, Zython
defining a notification function, setting up a schedule, and then running the scheduler'''

matches = re.search(pattern,text)

#print(matches)

a = re.finditer(pattern,text)

for i in a:
    print(i)
    print(type(i.span()))
    print(i.span()[0],i.span()[1])
    print(text[i.span()[0]:i.span()[1]])
import sys
import re

if len (sys.argv)<2:
    print('start as:python3 RE_test.py BVI1')
    sys.exit()
t=sys.argv[1]
f=open('./1.txt','rt')
for x in f:
    reg=re.findall(r'^[A-Za-z]+\d+/?\d?/?\d?/?\d?',x)
    if reg==[]:
        continue
    elif reg[0]==t:
        for x in f:
            ip=re.findall(r'[0-9a-f]{4}(\.[0-9a-f]{4}){2}',x)
            if ip !=[]:
                print(ip)
                break
            elif x=='\n':
                print('no IP')
                break
        break
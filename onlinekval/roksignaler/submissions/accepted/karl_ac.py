morseToLetter = {}

for i in range(26):
    letter, morse = raw_input().split()
    morseToLetter[morse] = letter

s, p = map(int, raw_input().split())
t, b, m = map(int, raw_input().split())

nString, code = raw_input().split()
n = int(nString)

out = ''
cur = code[0]
count = 0
morse = ''

def doPrev():
    global out, cur, count, morse
    if cur == '1':
        if count == s:
            morse += '-'
        else:
            morse += '.'
    else:
        if count == b or count == m: 
            out += morseToLetter[morse]
            morse = ''                            
        if count == m:
            out += ' '

for c in code:
    if c != cur:
        doPrev()
        cur = c
        count = 0
    
    count += 1

doPrev()
cur = '0'
count = b
doPrev()

print(out)

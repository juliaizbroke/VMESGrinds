def myAtoi(s: str) -> int:
    num = '0'
    neg = False
    check = {' ':True,'-':False,'+':False,'digit':False}
    
    for i in range(len(s)):
        if s[i].isdigit():
            num += s[i]
            if check[' ']:
                check[' '] = False
            if not check['digit']:
                check['digit'] = True
            if not check['-']:
                check['+'] = True
        elif check['digit']:
            break
        else:
            if (s[i] == '+' or s[i] == '-') and not check['+'] and not check['-']:
                check[s[i]] = True
                check[' '] = False
                if s[i] == '-':
                    neg = True
            elif (s[i].isspace() and not check[' ']) or (not s[i] in check) or ((s[i] == '+' or s[i] == '-') and (check['+'] or check['-'])):
                break
        
    num = int(num)
    if neg:
        num = -num
    if num < -2**31:
        return -2**31
    elif num > (2**31)-1:
        return (2**31)-1
    return num

print(myAtoi('42'))
print(myAtoi(' -042'))
print(myAtoi('1337c0d3'))
print(myAtoi('0-1'))
print(myAtoi('words and 987'))

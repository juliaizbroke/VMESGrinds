def myAtoi(self, s: str) -> int:
    num = '0'
    sign = ""
    space = True
    digit = False
    
    for i in s:
        if i.isdigit():
            num += i
            if not digit:
                space = False
                digit = True
        elif digit:
            break
        else:
            if sign == "" and (i == '-' or i == '+'):
                sign = i
                space = False
            elif (i.isspace() and not space) or (sign != "" and (i == '-' or i == '+')) or (not i.isspace() and i != '-' and i != '+'):
                break
        
    num = int(num)
    if sign == "-":
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

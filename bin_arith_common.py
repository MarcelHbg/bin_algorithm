import math

def list2Num(list:list):
    num = 0
    if list[0] == 1 : num = -1
    for bit in list:
        if bit < 0 or bit > 1:
            raise ValueError("list is no bitarray", list, bit)
        num = num << 1
        num |= bit
    return num

def num2List(num:int):
    list = []
    bitcnt = round(math.log2(abs(num)))
    for i in range(bitcnt + 2):
        bit = (num >> i) & 1
        list.append(bit)
    list.reverse()
    return list

def list2Str(list:list):
    result = "[ "
    for bit in list:
        result += str(bit)
        result += ' '
    result += "]"
    return result

def list2StrDiv(list:list):
    result = "[ "
    length = len(list)
    for i in range(length):
        result += str(list[i])
        if ((length - i) % 4) == 1: result += ' '
    result += "]"
    return result

def printDevider(len:int):
    devider = ""
    for i in range(len):
        devider += '='
    print(devider)

def printBinDec(info:str, list:list):
    line = str(f"{info}: {list2StrDiv(list)}2, [{list2Num(list)}]10")
    print(line)
    return len(line)

def adjustLength(s1:list, s2:list, fillLeft = True):
    s1_len = len(s1)
    s2_len = len(s2)
    neutral = 0
    if s1_len < s2_len:
        if fillLeft :
            neutral = s1[0]
            s1.reverse()
        while(len(s1) < s2_len):
            s1.append(neutral)
        if fillLeft : s1.reverse()
        return s2_len
    else:
        if fillLeft :
            neutral = s2[0]
            s2.reverse()
        while(len(s2) < s1_len):
            s2.append(neutral)
        if fillLeft : s2.reverse()
        return s1_len

def add(s1:list, s2:list, fillLeft = True, enaPrint = False):
    _s1 = s1.copy()
    _s2 = s2.copy()

    length = adjustLength(_s1, _s2, fillLeft)

    if enaPrint:
        line = str(f"   {list2Str(_s1)}")
        printDevider(len(line))
        print(line)
        print(f" + {list2Str(_s2)}")

    _s1.reverse()
    _s2.reverse()

    result = [0] * length
    carry = [0] * length
    for i in range(length):
        try:
            sum = _s1[i] + _s2[i] + carry[i]
            if sum == 2:
                result[i] = 0
                carry[i+1] = 1
            elif sum == 3:
                result[i] = 1
                carry[i+1] = 1
            else:
                result[i] = sum
        except IndexError:
            pass

    result.reverse()

    if enaPrint:
        carry.reverse()
        line = str(f" c {list2Str(carry)}")
        print(line)
        print(f" = {list2Str(result)}")
        printDevider(len(line))

    return result

def komplement1(list:list):
    result = []
    for bit in list:
        if bit:
            result.append(0)
        else:
            result.append(1)
    return result

def komplement2(list:list):
    k1 = komplement1(list)
    return add(k1, [0,1])

def shiftRight(list:list, keepLen=1):
    result = [list[0]]
    for i in range(len(list) - keepLen):
        result.append(list[i])
    return result

def boothRadix2(m1:list, m2:list):
    line = str("Booth-Algorithmus-Radix-2")
    printDevider(len(line))
    print(line)
    printDevider(len(line))

    m22 = komplement2(m2)
    printBinDec("Multiplikator", m1)
    printBinDec("Multiplikand ", m2)
    printBinDec("Multiplikand\"", m22)

    operation = "MULT"

    m1.append(0) # append 0 
    result = [0] * (len(m2)) # create result with 0
    line = str(f"{list2Str(m1)} : {operation} : {list2Str(m2)}") # print first line 
    printDevider(len(line))
    print(line)
    printDevider(len(line))
    
    m1_cnt = len(m1)
    dualcode = ['-'] * m1_cnt

    for i in range(m1_cnt-1):
        r2 = m1[m1_cnt-i-1]
        r1 = m1[m1_cnt-i-2]
        dualcode[m1_cnt-i-1] = r2
        dualcode[m1_cnt-i-2] = r1
        
        if (r1 == 1) and (r2 == 0):
            print(f"{list2Str(dualcode)} : ADD\" : {list2Str(m22)}")
            result = add(result, m22, False)
        elif (r1 == 0) and (r2 == 1):
            print(f"{list2Str(dualcode)} : ADD  : {list2Str(m2)}")
            result = add(result, m2, False)

        print(f"{list2Str(dualcode)} : SHR  : {list2Str(result)}") 
        result = shiftRight(result, 0)

        dualcode[m1_cnt-i-1] = '-'
        dualcode[m1_cnt-i-2] = '-'

        line = str(f"{list2Str(dualcode)} :      : {list2Str(result)}")
        print(line)

    printDevider(len(line))
    printBinDec("Produkt", result)
    printDevider(len(line))
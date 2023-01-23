import bin_arith_common as bin

def _convertInputType(any):
    t = type(any)
    if t is list:
        return any
    elif t is int:
        return bin.num2List(any)
    else:
        raise TypeError("Invalid type", any, t)

def komp2(z):
    _z = _convertInputType(z)
    line = str("2er Komplement")
    bin.printDevider(len(line))
    print(line)
    bin.printDevider(len(line))
    bin.printBinDec("Input ", _z)
    _z1 = bin.komplement1(_z)
    bin.printBinDec("Input\'", _z1)
    _z2 = bin.komplement2(_z)
    bin.printDevider(bin.printBinDec("Input\"", _z2))

def add(s1, s2):
    _s1 = _convertInputType(s1)
    _s2 = _convertInputType(s2)
    line = str("Addition")
    bin.printDevider(len(line))
    print(line)
    bin.printDevider(len(line))
    bin.printBinDec("Summand ", _s1)
    bin.printBinDec("Summand ", _s2)
    _sum = bin.add(_s1, _s2, enaPrint=True)
    bin.printDevider(bin.printBinDec("Summe ", _sum))

def sub(minuend, subtrahend):
    _m = _convertInputType(minuend)
    _s = _convertInputType(subtrahend)
    line = str("Subtraction")
    bin.printDevider(len(line))
    print(line)
    bin.printDevider(len(line))
    bin.printBinDec("Minuend     ", _m)
    bin.printBinDec("Subtrahend  ", _s)
    _s2 = bin.komplement2(_s)
    bin.printBinDec("Subtrahend\" ", _s2)
    _diff = bin.add(_m, _s2, enaPrint=True)
    bin.printDevider(bin.printBinDec("Difference ", _diff))

def boothRadix2(m1, m2):
    _m1 = _convertInputType(m1)
    _m2 = _convertInputType(m2)
    bin.boothRadix2(_m1, _m2)


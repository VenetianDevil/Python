import fractions
def add_frac(frac1, frac2):        # frac1 + frac2
    if(frac1[1] == frac2[1]):
        return [frac1[0]+frac2[0], frac1[1]]
    else:
        NWD = fractions.gcd(frac1[1], frac2[1])
        mianownik = frac1[1] * (frac2[1]/NWD)
        licznik = (frac1[0] * (frac2[1]/NWD)) + (frac2[0] * (frac1[1]/NWD))
        NWD_skroc = fractions.gcd(licznik, mianownik)
        return [licznik/NWD_skroc, mianownik/NWD_skroc]

def sub_frac(frac1, frac2):        # frac1 - frac2
    if(frac1[1] == frac2[1]):
        licznik = frac1[0] - frac2[0]
        NWD_skroc = fractions.gcd(licznik, frac1[1])
        return [licznik/NWD_skroc, frac1[1]/NWD_skroc]
    else:
        NWD = fractions.gcd(frac1[1], frac2[1])
        mianownik = frac1[1] * (frac2[1]/NWD)
        licznik = (frac1[0] * (frac2[1]/NWD)) - (frac2[0] * (frac1[1]/NWD))
        NWD_skroc = fractions.gcd(licznik, mianownik)
        return [licznik/NWD_skroc, mianownik/NWD_skroc]

def mul_frac(frac1, frac2):        # frac1 * frac2
    if(frac1[0] == 0 | frac2[0] == 0):
        return 0
    else:
        licznik = frac1[0] * frac2[0]
        mianownik = frac1[1] * frac2[1]
        NWD_skroc = fractions.gcd(licznik, mianownik)
        return [licznik/NWD_skroc, mianownik/NWD_skroc]

def div_frac(frac1, frac2):        # frac1 / frac2
    if(frac1[0] == 0):
        return 0
    else:
        licznik = frac1[0] * frac2[1]
        mianownik = frac1[1] * frac2[0]
        NWD_skroc = fractions.gcd(licznik, mianownik)
        return [licznik/NWD_skroc, mianownik/NWD_skroc]

def is_positive(frac):             # bool, czy dodatni
    if frac[0] > 0:
        return True
    elif frac[0] < 0:
        return False

def is_zero(frac):                 # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    f1 = float(frac1[0])/float(frac1[1])
    f2 = float(frac2[0])/float(frac2[1])
    if f1 < f2:
        return -1
    elif f1 == f2:
        return 0
    else:
        return 1

def frac2float(frac):              # konwersja do float
    return float(frac[0])/float(frac[1])
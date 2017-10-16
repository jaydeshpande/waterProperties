def calcVisc(T_in):
    return round(-2E-13 * T_in ** 5 + 9E-11 * T_in ** 4 - 1E-08 * T_in ** 3 + 1E-06 * T_in ** 2 - 6E-05 * T_in + 0.0018, 6)

def calcRho(T_in):
    return round(-1E-07 * T_in ** 4 + 4E-05 * T_in ** 3 - 0.0071 * T_in ** 2 + 0.0385 * T_in + 999.99, 2)

def calcSpecHt(T_in):
    return 1000 * round(-3E-11 * T_in ** 5 + 9E-09 * T_in ** 4 - 1E-06 * T_in ** 3 + 9E-05 * T_in ** 2 - 0.0029 * T_in + 4.2134, 2)

def calcKappa(T_in):
    return round(5E-10 * T_in ** 4 - 1E-07 * T_in ** 3 - 3E-06 * T_in ** 2 + 0.002 * T_in + 0.5603 , 4)
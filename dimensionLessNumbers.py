from fluidProperties import *
def calcRe(T_in, U_inf, D):
    return round(calcRho(T_in) * U_inf * D / calcVisc(T_in), 2)

def calcPr(T_in):
    return round(calcVisc(T_in) * calcSpecHt(T_in) / calcKappa(T_in), 2)

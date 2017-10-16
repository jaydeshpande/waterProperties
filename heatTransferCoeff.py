from fluidProperties import *
from math import log, sqrt

def calcHeatTransferCoeffLaminar(Re, Pr, D, L, T):
    nu_numerator = 0.065 * Re * Pr * D / L
    nu_denominator = 1 + (0.04 * (Re * Pr * D / L) ** (2 / 3))
    nu_ = 3.66 + (nu_numerator / nu_denominator)
    return round(nu_ * calcKappa(T) / D, 2)


def calcHeatTransferCoeffTurbulent(Re, Pr, T, D):
    sjfrictionFact_ = (1 / (-2 * log(5.74 / Re ** (0.9)))) ** 2
    nu_numerator = (sjfrictionFact_ / 2) * (Re - 1000) * Pr
    nu_denominator = 1 + (12.7 * (Pr ** (2 / 3) - 1) * sqrt(sjfrictionFact_ / 2))
    nu_ = nu_numerator / nu_denominator
    return round(nu_ * calcKappa(T) / D, 2)
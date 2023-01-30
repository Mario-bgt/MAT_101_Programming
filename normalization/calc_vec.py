import mpmath
import math
import decimal
import numpy as np
from sympy import *

t = symbols('t')
e = symbols('e')
toft = [3 * sqrt(2) * t, Pow(e, 3 * t), Pow(e, -3 * t)]
tprimet = [diff(toft[0], t), diff(toft[1], t), diff(toft[2], t)]
print('Our vector function is:' + str(toft))
print("T'(t) is then given by: " + str(tprimet))
noft = [tprimet[0] / sqrt(Pow(tprimet[0], 2) + Pow(tprimet[1], 2) + Pow(tprimet[2], 2)),tprimet[1] / sqrt(Pow(tprimet[0], 2) + Pow(tprimet[1], 2) + Pow(tprimet[2], 2)), tprimet[2] / sqrt(Pow(tprimet[0], 2) + Pow(tprimet[1], 2) + Pow(tprimet[2], 2))]
print("Our N(t) is then given by: " + str(noft))

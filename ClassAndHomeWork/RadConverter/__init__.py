import sys
import os

sys.path.append(os.path.dirname(__file__))

from python.ClassAndHomeWork.RadConverter.deg_to_gms import *
from python.ClassAndHomeWork.RadConverter.deg_to_rad import *
from python.ClassAndHomeWork.RadConverter.gms_to_deg import *
from python.ClassAndHomeWork.RadConverter.rad_to_deg import *

print(deg_to_gms(39.97))
print(gms_to_deg("39°", "58`", '12"'))
print(deg_to_rad(39.97))
print(rad_to_deg(deg_to_rad(39.97)))

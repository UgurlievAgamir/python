from deg_to_gms import *


def RC_MultiInput(*args, **kwargs):
    OutputData = {}

    for i in range(0, len(args)):
        OutputData['Point_' + str(i)] = deg_to_gms(args[i])

    for name, value in kwargs.items():
        value = deg_to_gms(value)
        OutputData[name] = value

    return OutputData


print(RC_MultiInput(12.34, 123.34, 123.3, k=22.2, l=34.23))

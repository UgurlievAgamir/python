from math import pi


def deg_to_gms(deg):
    '''

    :param deg: decimal degrees
    :return: degrees, minutes, seconds
    '''

    grad = int(deg)
    minutes_ost = (deg - grad) * 60
    minutes = int(minutes_ost)
    seconds = round((minutes_ost - minutes) * 60, 5)

    return f'{grad}° {minutes}` {seconds}"'


def gms_to_deg(degrees, minutes, seconds):
    '''

    :param degrees: str degrees with special symbol
    :param minutes: str minutes with special symbol
    :param seconds: str seconds with special symbol
    :return: decimal degrees
    '''

    ans = int(degrees[:2]) + (int(minutes[:2]) / 60) + (int(seconds[:2]) / 3600)

    return ans


def deg_to_rad(deg):
    '''

    :param deg: decimal degrees
    :return: radians
    '''
    return (pi / 180) * deg


def rad_to_deg(rad):
    '''

    :param rad: radians
    :return: decimal decrees
    '''
    return (180 / pi) * rad


def main():
    print(deg_to_gms(39.97))
    print(gms_to_deg("39°", "58`", '12"'))
    print(deg_to_rad(39.97))
    print(rad_to_deg(deg_to_rad(39.97)))

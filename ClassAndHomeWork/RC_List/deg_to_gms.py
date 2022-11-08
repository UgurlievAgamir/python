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

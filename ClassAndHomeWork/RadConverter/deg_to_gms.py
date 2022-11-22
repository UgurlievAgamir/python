def deg_to_gms(deg: int) -> str:
    """
    deg to gms
    :param deg: decimal degrees
    :return: degrees, minutes, seconds
    """

    grad: int = int(deg)
    minutes_ost: int = (deg - grad) * 60
    minutes: int = int(minutes_ost)
    seconds: int = round((minutes_ost - minutes) * 60, 5)

    return f'{grad}° {minutes}` {seconds}"'

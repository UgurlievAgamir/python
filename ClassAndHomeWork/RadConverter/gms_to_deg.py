def gms_to_deg(degrees: int, minutes: int, seconds: int) -> float:
    """
    gms to deg
    :param degrees: str degrees with special symbol
    :param minutes: str minutes with special symbol
    :param seconds: str seconds with special symbol
    :return: decimal degrees
    """

    ans = int(degrees[:2]) + (int(minutes[:2]) / 60) + (int(seconds[:2]) / 3600)

    return ans

def contains_duplicates(numbers_list: list) -> bool:
    """

    :param numbers_list:
    :return:
    """
    for number in numbers_list:
        if numbers_list.count(number) > 1:
            return True

    return False

#
# print(contains_duplicates([0, 1, 2, 3, 4, 5, 6, 7, 6]))
# print(contains_duplicates([0, 1, 2, 3, 4, 5, 6, 7]))
# print(contains_duplicates([]))

help(contains_duplicates([12, 12]))
#dfjdsjkf

'''
dasdas
asda
sd
ass
'''
print(__doc__)
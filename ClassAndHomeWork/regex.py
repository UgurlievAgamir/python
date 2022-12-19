import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

tel_nums = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()

pattern2 = '(?:header__title-link\">)([^<]*)(?:[^.]*location\">\n*\s*)([^\n]*)'

pattern: str = r'(?:class=\"org-widget\-header__title-link\">[^\w]*|<span class=\"org-widget\-header__meta ' \
               r'org-widget\-header__meta\--location\">[^\w]*|<dt class=\"spec__index\"><span ' \
               r'class=\"spec__index-inner\">Телефон</span></dt>\n*\s*<dd class=\"spec__value\">[^\w]*|<dt ' \
               r'class=\"spec__index\"><span class=\"spec__index-inner\">Часы работы</span></dt>\n*\s*<dd ' \
               r'class=\"spec__value\"[^\w]*>|<p>[^\w]*)([^<]*\b) '
match = re.findall(pattern, tel_nums)
match2 = re.findall(pattern2, tel_nums)
print(match)
print(match2)

towns_db = []
towns_search = []

db_input_count = int(input())

for i in range(0, db_input_count):
    towns_db.append(input().split())

search_input_count = int(input())

for j in range(0, search_input_count):
    towns_search.append(input())

for town in towns_search:
    for data in towns_db:
        for db_town in data:
            if town == db_town:
                print(data[0])

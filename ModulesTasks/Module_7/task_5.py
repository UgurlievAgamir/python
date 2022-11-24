files_list = []
operations_list = []

input_files_count = int(input())

for i in range(0, input_files_count):
    files_list.append(input())

input_operation_count = int(input())

for j in range(0, input_operation_count):
    inp = input()

    inp_cache = ''
    for k in inp:
        inp_cache += k.replace('R', 'read').replace('W', 'write').replace('X', 'execute')

    print(inp_cache)

    inp = inp_cache

    operations_list.append(inp.split())

for operation in operations_list:
    for file in files_list:
        print(file)
        if operation.split()[1] in file:
            if operation.split()[0] in file:
                print('OK')
            else:
                print('Denied')

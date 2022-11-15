import file_handler

print(file_handler.read_file('read_file.txt'))
file_handler.write_file('save_file.txt', file_handler.read_file('read_file.txt'))

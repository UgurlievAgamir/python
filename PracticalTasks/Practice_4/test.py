import file_handler

print(file_handler.read_file('read_file'))
file_handler.write_file('save_file', file_handler.read_file('read_file'))

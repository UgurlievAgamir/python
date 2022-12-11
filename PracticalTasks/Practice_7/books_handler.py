import csv


def get_books(with_name: str) -> list:
    output: list = []
    with open('books.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            if with_name.lower() in row[1].lower():
                output.append(row)

    return output


def get_totals(books: list) -> list:
    output: list = []

    for book_values in books:
        try:
            qp = float(book_values[3]) * float(book_values[4])

            if qp < 500:
                qp += 100

            output.append((book_values[0], str(qp)))
        except ValueError:
            print(f'Incorrect values in book ({book_values})')

    return output


print(get_books('python'))
print(get_totals(get_books('python')))

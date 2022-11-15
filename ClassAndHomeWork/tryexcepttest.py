def f():
    try:
        a = int(input())
        b = int(input())
        x = a / b
    except:
        return
    else:
        return x
    finally:
        print('Обработка')


print(f())

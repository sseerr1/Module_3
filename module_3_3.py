# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров:
values_list = [777, 'какой-то текст', False]
values_dict = {'c': 10, 'a': 'тра-ля-ля', 'b': False}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:
values_list_2 = [777, 'Боинг']
print_params(*values_list_2, 42)

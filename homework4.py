calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    return (len(string)), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    low_string = string.lower()
    low_list_to_search = [i.lower() for i in list_to_search]
    if low_string in low_list_to_search:
        return True
    else:
        return False


print(string_info("Клоунада"))
print(string_info('Третий модуль сложный'))
print(is_contains('Кошка', ['Пряжка', 'кошкА', 'кишка']))
print(is_contains("Кит", ['Кот', 'крОТ', 'СЛОн']))
print(calls)

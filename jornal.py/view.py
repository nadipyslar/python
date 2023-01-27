import model
def input_class():
    return input('С каким классом работаем? ').upper()

def input_subject():
    return input('Какой предмет? ').lower()

def who_answer():
    return input('Кто будет отвечать? ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_child(journal:dict):
    for i, child in enumerate(journal,1):
        print(f'{i}. {child:20} {journal.get(child)}')

def mark_check(mark):
    if mark in range(1,6):
        print('Оценка принята')
    else:
        print('Введите оценку от 1 до 5 ')

def student_check(str):
    if str in model.journal:
        print(f'Отвечает ученик{str}')
    else:
        print('Проверьте написание фамилии и имени ученика')
        student = input('Кто будет отвечать? ')
        return student         

    
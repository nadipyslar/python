
def main_menu():
    сommands = ['Показать все контакты', 'Открыть файл',
    'Сохранить файл','Новый контакт','Изменить контакт',
    'Удалить контакт','Найти контакт','Выйти из программы']

    print ('\nВыберете пункт меню: ')
    for i in range(len(сommands)):
            print (f'\t{i+1}. {сommands[i]}')

    user_input = int(input('\nВведите пункт меню: '))
    return user_input

def show_contacts(phone_book:list):
    if len(phone_book)>0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пуста или не загружена')

def save_success():
    print('Телефонная книга сохранена успешно')

def load_success():
    print('Телефонная книга загружена успешно')

def new_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search


def delete_contactd():
    name = input('Введите имя и фамилию контакта: ')
    return name

def delete_success():
    print('Контакт удален')

def change_contact_old():
    name = input('Введите имя и фамилию контакта, которое надо изменить: ')
    return name
def change_contact_new():    
    new_name = input('Введите новое имя: ')
    new_phone = input('Введите новый телефон: ')
    new_comment = input('Введите новый комментарий: ')
    return new_name, new_phone, new_comment
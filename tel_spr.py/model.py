phone_book=[]
path = '/Users/franz/Desktop/python/tel_spr.py/phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact:list):
    global phone_book
    phone_book.append(contact)

def open_phone_book():
    global phone_book
    global path
    with open (path,'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open (path,'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))
        for line in data:
            phone_book.append(line.strip().split(';'))

def search_contact(search:str):
    global phone_book
    search_results =[]
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results

def delete_phone_book(name:str):
    global phone_book
    for line in phone_book:
         if name in line:
            phone_book.remove(line)

def change_phone_book_from_old (contact:str):
    global phone_book
    for line in phone_book:
         if contact in line:
            phone_book.remove(line)

def change_phone_book_add_new (contact:list):
    global phone_book
    phone_book.append(contact)
  
            
    
        
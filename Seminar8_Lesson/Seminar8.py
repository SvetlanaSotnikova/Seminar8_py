# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# HomeWork
# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

import os

def load_from_file(filename): # пришлось и себя помучать этой штукой и нейронку тоже :\
    phonebook = []
    try:
        with open(filename, 'r') as file:
            contact = {}
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        key, value = parts
                    elif len(parts) == 1:
                        key = parts[0]
                        value = None
                    else:
                        key = None
                        value = None
                    if key is not None:
                        contact[key] = value
                elif contact:
                    phonebook.append(contact)
                    contact = {}
            if contact:
                phonebook.append(contact)
        return phonebook
    except FileNotFoundError:
        return []

def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
        contact = {
            'Lastname': last_name,
            'Firstname': first_name,
            'Middlename': middle_name,
            'Phone number': phone_number
        }
        phonebook.append(contact)

def display_contacts(phonebook):
    for contact in phonebook:
        print('\n---- contact ----')
        for key, value in contact.items():
            print(f'{key}:{value}')

def search_contact(phonebook, key, value):
    found_contacts = []
    for contact in phonebook:
        if contact.get(key) == value:
            found_contacts.append(contact)
    return found_contacts

def save_to_file(phonebook, filename):
    with open(filename, 'a') as f:
        for contact in phonebook:
            for key, value in contact.items():
               f.write(f'{key}: {value}\n')
            f.write('\n')

def list_files():
    files_txt = [filename for filename in os.listdir() if filename.endswith('.txt')]
    return files_txt

def display_contacts_from_list(filename):
    phonebook = load_from_file(filename)
    if not phonebook:
        print('This file is empty :/')
    else:
        display_contacts(phonebook)

# чтобы скопировать определенные строки
def copy_file(number_line, another_filename, source_def_file): # хомеворк
    phonebook = load_from_file(source_def_file)

    if not phonebook:
        print('Source file is empty. Nothing to copy.')
        return
    
    with open(another_filename, 'a') as f:
        for line_number in number_line:
            if 1 <= line_number <= len(phonebook):
                contact_copy = phonebook[line_number - 1]

                for key, value in contact_copy.items():
                    if key in ['Lastname', 'Firstname', 'Middlename', 'Phone number']:
                        f.write(f'{key}: {value}\n')
                f.write('\n')
        else:
            print(f'Invalid line number {line_number}. Skipped :(')

# а это чтобы скопировать весь контакт по найденной строчке
# def copy_file(number_line, another_filename, source_def_file): # хомеворк
#     phonebook = load_from_file(source_def_file)

#     if not phonebook:
#         print('Source file is empty. Nothing to copy.')
#         return

#     for line_number in number_line:
#         if line_number <= len(phonebook):
#             contact_copy = phonebook[line_number - 1]

#             with open(another_filename, 'a') as f:
#                 for key, value in contact_copy.items():
#                     f.write(f'{key}: {value}\n')
#                 f.write('\n')
#         else:
#             print(f'Invalid line number {line_number}. Skipped :(')

phonebook = load_from_file('Phonebook.txt')

while True:

    print('\nMenu')
    print('1. Add contact')
    print('2. Display all contacts')
    print('3. Save to file')
    print('4. Search contact by characteristic')
    print('5. Сopy data to another file') # homework
    print('6. Exit')

    choice = input('Your choice: ')

    if choice == '1':
        last_name = input('Input lastname: ')
        first_name = input('Input firstname: ')
        middle_name = input('Input middlename: ')
        phone_number = input('Input phone number: ')
        add_contact(phonebook, last_name, first_name, middle_name, phone_number)
   
    elif choice == '2':
        files_txt = list_files()
        if not files_txt:
            print(f'No {files_txt} files found in the directory :(')
        else:
            print('\nAvailable files:')
            for idf, file in enumerate(files_txt, start=1):
                print(f'{idf}. {file}')

            selection = None
            while selection is None:
                try:
                    file_choice = int(input('the number of the file to display contacts: '))

                    selection = files_txt[file_choice - 1] if 1 <= file_choice <= len(files_txt) else None

                    display_contacts_from_list(selection) if selection else print('Invalid value :(')

                except ValueError:
                    print('Invalid input :/ Try again input number !')
   
    elif choice == '3':
        print('You can save information in default file or in your own file :D')
        print('1. Default file "Phonebook.txt')
        print('2. Your file')
        print('3. Cancel')

        while True:
            file_choice = input('Your choice: ')
            if file_choice == '1':
                save_to_file(phonebook, 'Phonebook.txt')
                print('\nData was saving in file Phonebook.txt :D')
                break
            elif file_choice == '2':
                file_name = input('Input file name with extension: ')
                save_to_file(phonebook, file_name)
                save_to_file(phonebook, 'Phonebook.txt')
                print(f'\nData was saving in file {file_name} :D')
                break
            elif file_choice == '3':
                continue
            else:
                print('Incorrect choice :( Try again !')  
   
    elif choice == '4': 
        search_key = input('\nInput a search characteristic (for example, Lastname): ')
        search_value = input('Input a search value: ')
        found_contacts = search_contact(phonebook, search_key, search_value)
        if search_value:
            print('\nFound contacts:')
            display_contacts(found_contacts)
        else:
            print('\nNo contacts with the specified characteristics were found :(')

    elif choice == '5': # homework
        source_file = input('\nInput the name of the file from which you want to copy contacts: ')
        another_file = input('Input file name to copy information: ')
        while True:
            line_numbers_input = input('Input the line numbers to copy (separated by spaces): ')

            if not all(num.isdigit() for num in line_numbers_input.split()):
                print('Invalid value, please input digit !')
            else:
                line_numbers = [int(number) for number in line_numbers_input.split()]
                if os.path.exists(source_file):
                    copy_file(line_numbers, another_file, source_file)
                    print('\nData was copied :D')
                    break
                else:
                    print('\nError, check your file')

    elif choice == '6':
        break
    
    else: 
        print('Wrong choice, try again !')

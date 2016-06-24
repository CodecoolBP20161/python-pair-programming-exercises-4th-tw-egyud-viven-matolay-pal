import csv
import sys
from person import Person


def open_csv(file_name):
    with open(file_name) as csvfile:
        filereader = csv.reader(csvfile)
        person_list = []
        for row in filereader:
            person_list.append(Person(row[0], row[1]))
        return person_list


def get_csv_file_name(argv_list):
    try:
        return argv_list[1]
    except:
        return None


def format_output(person):
    if not person:
        return "No match found."
    return "This number belongs to: {}".format(person.get_name())


def get_person_by_phone_number(person_list, user_input_phone_number):
    phone_number = Person.normalize_phone_number(user_input_phone_number)
    for element in person_list:
        if element.is_phone_number_matching(phone_number):
            return element
    return None


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()

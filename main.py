from requests import get
from csv import DictWriter
from json import load
def option():
    """Params that the user wants."""
    results = int(input('How many users do you want? ='))

    gender_if = input('Do you want any specific genre? [Y/n]')
    gender = None if gender_if.lower() == 'n' else 'y' 
    if gender:
        gender = input('Male or Female? [M/F]')
        gender = 'male' if gender.lower() == 'm' or gender.lower() == 'male' else 'female'
    context = {
        'results': results,
        'gender': gender
    }
    request(**context)


def request(results, gender):
    """Request and params from users."""
    print(results, gender)
    URL = 'https://randomuser.me/api/'
    params = {'results': results, 'gender': gender}
    response = get(URL, params=params)
    value = load(response.json)
    if_values(value)
    
def if_values(value):
    print(type(value))
    print(value)


def writer_csv(users):
    """Write new users."""
    with open('users.csv', 'w') as csv_file:
        fieldnames = ['name complete', 'email', 'country', 'date', 'cell']
        user_writer = DictWriter(csvfile, fieldnames=fieldnames)

        user_writer.writerheader()
        user_writer.writerow(user)


def main():
    option()

if __name__ == '__main__':
    main()

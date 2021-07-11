from requests import get
import csv
import json
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
    value = json.loads(response.text) 
    csv_writer(value)
    
def csv_writer(dictionary):
    """Define values."""
    users = list(dictionary['results'])
    with open('users.csv', 'w', encoding='utf-8') as csvfile:
        fieldnames = ['name complete', 'email', 'country', 'date', 'cellphone']
        user_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        user_writer.writeheader()
        for user in users:
            name = user.get('name')
            name = f"{name['first']} {name['last']}"
            country = user.get('location')
            country = country.get('country')
            email = user.get('email')
            date = user.get('dob')
            date = date.get('date')
            cell = user.get('cell')

            user_writer.writerow({
                'name complete': name, 
                'country': country, 
                'email': email, 
                'date': date, 
                'cellphone':cell})

if __name__ == '__main__':
    option()

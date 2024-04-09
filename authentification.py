import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi_sentiments'
# port de l'API
api_port = 8000
 
users=[{'username':'alice','password':'wonderland'},
         {'username':'bob','password':'builder'},
         {'username':'clementine','password':'mandarine'}]

for i in range(len(users)):  

    # requête
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params= {
            'username': users[i]['username'],
            'password': users[i]['password']
        }
    )

    output = '''
============================
     Authentication test
============================

request done at "/permissions"
| username= {username}
| password= {password}

expected result = 200
actual restult = {status_code}

==>  {test_status}

    '''


    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    print(output.format(username= users[i]['username'], password= users[i]['password'], status_code=status_code, test_status=test_status))

    # impression dans un fichier
    if os.environ.get('LOG') == 1:

        with open('/home/my_folder/api_test.log', 'a') as file:
            file.write(output)

import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi_sentiments'
# port de l'API
api_port = 8000

versions=['v1','v2']
 
users=[{'username':'alice','password':'wonderland'},
         {'username':'bob','password':'builder'}]

for version in versions:
    for i in range(len(users)):
            
	# requête
        r = requests.get(
            url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
            params= {
                'username': users[i]['username'],
                'password': users[i]['password'],
                'sentence': 'life is beautiful'
            }
        )

        output = '''
============================
     Authorization test
============================

request done at "/{version}/sentiment"
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

        print(output.format(version= version, username= users[i]['username'], password= users[i]['password'], status_code=status_code, test_status=test_status))

        # impression dans un fichier
        if os.environ.get('LOG') == 1:

            with open('/home/my_folder/api_test.log', 'a') as file:
                file.write(output)

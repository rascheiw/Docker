import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi_sentiments'
# port de l'API
api_port = 8000
 
contents=['life is beautiful','that sucks']

versions=['v1','v2']

for content in contents:
    for version in versions:

        # requête
        r = requests.get(
            url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
            params= {
                'username': 'alice',
                'password': 'wonderland',
                'sentence': content
            }
        )

        output = '''
============================
      Content test
============================

request done at "/{version}/sentiment"
| username= "alice"
| password= "wonderland"
| sentence= {content}

expected result = {expected}
actual restult = {score}

==>  {test_status}

        '''


        # statut de la requête
        status_code = r.status_code

        # affichage des résultats
        if content == 'life is beautiful':
            expected = 'POSITIF SCORE'
            if (r.json()['score'] > 0):
                test_status = 'SUCCESS'
            else:
                test_status = 'FAILURE'

        if content == 'that sucks':
            expected = 'NEGATIF SCORE'
            if (r.json()['score'] < 0):
                test_status = 'SUCCESS'
            else:
                test_status = 'FAILURE'

        print(output.format(version= version, content=content, expected=expected, score=r.json()['score'], test_status=test_status))


        # impression dans un fichier
        if os.environ.get('LOG') == 1:

            with open('/home/my_folder/api_test.log', 'a') as file:
                file.write(output)

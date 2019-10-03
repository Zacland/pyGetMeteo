import matplotlib.pyplot as plt
import requests
from requests.exceptions import HTTPError

# API utilisée : https://www.infoclimat.fr/api-previsions-meteo.html?id=2988507&cntry=FR
#
# Cette API est limitée à un usage raisonnable et non commercial.
# Est considéré comme raisonnable un usage de moins de 5.000 requêtes en 24 heures
# et de moins d'une requête par seconde, pour l'ensemble des API de prévisions.
# Vous devrez faire en sorte vous-même de ne pas dépasser cette limite,
# ou votre accès sera automatiquement verrouillé
# (dans ce cas vous recevrez un message d'erreur HTTP 509 Bandwidth Limit Exceeded).
# Merci de respecter notre service qui vous est offert gratuitement, sans publicité, par une association de bénévoles.
# Si vos besoins sont plus élevés (au niveau du nombre de requêtes ou des paramètres disponibles),
# merci de nous contacter préalablement.
# Si la clé d'authentification est erronée, le message 400 Bad Request sera retourné. ' \
# Si le run est en cours de sortie et les données non disponibles, le code sera 409 Conflict.
# Nous vous conseillons de toujours vérifier le paramètre "request_state" avant de traiter les données,
# cela évitera le plantage de vos applications en cas de problème.

url = "http://www.infoclimat.fr/public-api/gfs/json?_ll=43.610269,3.876715&_auth=UkgEEw9xAyEEKQA3VyELIlI6U2YBdwUiVytXNAhtBHkIY1c2B2dRN1A%2BWicFKgI0VntUN15lCDhWPQF5AXNQMVI4BGgPZANkBGsAZVd4CyBSfFMyASEFIlc3VzcIewRgCGpXLQdmUTBQNlomBTICPlZ6VCteYAg1VjIBZgFtUDJSMQRlD2kDZwR0AH1XYgtrUmhTNgFoBW5XMVdkCGUEZghpVzUHY1EzUCFaOAU2Aj5WY1Q3XmQIMVY3AXkBc1BKUkIEfQ8sAyMEPgAkV3oLalI%2FU2c%3D&_c=50707ccbef008a5791ad181bbc9c58c7"

try:
    response = requests.get(url)

    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success!')

retour = response.json()

print(retour)

x_date = []
y_temp = []

for elem in retour:
    if elem[:4].isnumeric():
        # print(elem, float(retour[elem]['temperature']['sol']) - 273.15)
        x_date.append(elem[5:16])
        y_temp.append(float(retour[elem]['temperature']['sol']) - 273.15)

plt.plot(x_date, y_temp, marker='o')
plt.grid()

plt.xticks(x_date, x_date, rotation='vertical', fontsize=6)

plt.show()

response.close()


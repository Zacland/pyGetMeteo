# pyGetMeteo

Attention à l'utilisation :

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

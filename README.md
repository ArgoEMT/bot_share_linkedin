# Bot de repartage de post sur LinkedIn

## Principe

Le but de ce bot est de repartager automatiquement un post récent d'une des compagnies suivies par l'utilisateur. 

## Comment l'utiliser 

En premier lieu, il faut vous créer un compte sur https://developer.linkedin.com/. Il faut ensuite activer tous les services. Le service Marketing peut prendre un certain temps à s'activer. 


Une fois cela fait, il faut ensuite compléter le `credentials_template.json` avec vos informations personnelles et le renommer en `credentials.json`. 
- Le `client_id` et le `client_secret` se trouvent dans l'onglet auth.
- le `redirect_uri` correspond à l'rul de redirection qui permet de récupérer certains tokens de connexion : le `access_token` et le `grant_token`
- le `orga_id` correspond à l'id de votre organisation. 

## Comment récupérer le `access_token` et le `grant_token`
1. Démarrer un serveur local à l'aide par exemple de la commande suivante : `python -m http.server 5501` (ouvre un serveur local sur le port 5501) et autoriser cet URL de redirection sur LinkedIn Developer.
2. Executer la fonction `get_authorization_code` de `auth_api`. Celle ci ouvrira une page web sur le serveur local et donnera accès au `access_token`.
3. Executer la fonction `get_grant_token` de `auth_api`. Celle ci éditera directement le `credentials.json`.

## Auteurs
- ArgoEMT (Victor Daumas)
- Thoom1999 (Thomas Pouget)
- ochaff (Owen Chaffard)

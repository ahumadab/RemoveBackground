# RemoveBackground

Webserver qui a pour but de supprimer le background des images envoyé

## Fonctionnalités

- Suppression automatique de l'arrière-plan des images.
- API RESTful pour l'intégration facile avec d'autres services ou applications.
- Interface utilisateur Swagger pour une interaction facile et un test de l'API.

## Technologies Utilisées

- FastAPI
- Python 3.10
- Docker
- Uvicorn pour le serveur ASGI

## Prérequis

- Python 3.10
- Docker

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

Lancez l'application avec cette commande:

```bash
uvicorn main:app --reload
```

Faites une requête POST avec l'image en payload

```bash
curl -X POST -F 'file=@path/to/your/image.jpg' http://localhost:8000/remove-bg --output processed_image.png
```

Visitez http://localhost:8000/docs pour accéder à la documentation Swagger de l'API et tester les endpoints.

## Déploiement avec Docker

Instructions pour construire et exécuter le conteneur Docker :

```bash
docker build -t remove_bg .
docker run -p 8000:8000 remove_bg
```
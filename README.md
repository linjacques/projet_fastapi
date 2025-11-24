# projet_fastapi

## Comment lancer le projet ? 

1. Construire l'image Docker de Fastapi et uvicorn
   ```bash
      docker build -t exemple_fastapi .
   ```
   
2. Construire **et** lancer le Container
   ```bash
     docker run -d -p 8000:8000 fastapi-app
   ```
   
   Explications :

  -  **-d** -> mode détaché (en arrière-plan)

  -  **-p 8000:8000** -> mappe le port externe 8000 vers le port interne 8000 où tourne FastAPI

  -  **exemple_fastapi** -> nom de l’image qu'on vient de construire

3. Lancer/relancer le container (déjà construit!)
   ```bash
     docker start SHA256 du container
   ```

4. Stoper le container
   ```bash
      docker stop SHA256 du container
   ```

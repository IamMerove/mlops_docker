FROM python:3.10-slim

WORKDIR /app

# 3. Copie des fichiers de dépendances
# On utilise uv pour l'installation rapide si tu veux, 
# mais ici on va faire classique avec pip pour Docker

COPY pyproject.toml .

#Copie du code source

COPY . .

RUN pip install --default-timeout=1000 --no-cache-dir .



#Exposition du port 8000 <--- UVICORN
EXPOSE 8000

# Commande de lancement

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
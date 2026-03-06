FROM python:3.10-slim

WORKDIR /app

# 3. Copie des fichiers de dépendances et du code source
# On installe ensuite le package via pip (qui a besoin du code source présent)

COPY pyproject.toml README.md ./
COPY . .

RUN pip install --default-timeout=1000 --no-cache-dir .


#Exposition du port 8000 <--- UVICORN
EXPOSE 8000

# Commande de lancement

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
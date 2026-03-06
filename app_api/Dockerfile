FROM python:3.10-slim

WORKDIR /app

# On copie TOUT le contenu du dossier app_api dans /app
COPY . .

# On installe (maintenant que maths est forcément là)
RUN pip install --no-cache-dir .

# On expose le port
EXPOSE 8000

# On lance
CMD ["uvicorn", "maths.main:app", "--host", "0.0.0.0", "--port", "8000"]
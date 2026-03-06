FROM python:3.10-slim

WORKDIR /app

# On copie TOUT le contenu du dossier app_api dans /app
COPY . .

# Debug : on vérifie que maths existe vraiment dans le contexte Docker
RUN echo "=== Debug: contenu de /app ==="
RUN ls -la
RUN echo "=== Debug: détails du dossier maths ==="
RUN ls -la maths || echo "ERREUR : dossier maths INEXISTANT ou inaccessible"
RUN test -d maths && echo "OK : maths est un dossier" || echo "KO : maths n'est PAS un dossier"
RUN find . -type d -name maths -ls || echo "find ne trouve pas maths nulle part"
RUN echo "=== Fin debug ===".

RUN pip install --no-cache-dir .
# On expose le port
EXPOSE 8000

# On lance
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
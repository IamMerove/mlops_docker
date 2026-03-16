FROM python:3.10-slim

WORKDIR /app

# On copie TOUT le contenu du dossier app_api dès le début
# (c'est la clé pour que maths existe quand on fait pip install .)
COPY . .

# ────────────────────────────────────────────────────────────────
# Debug : on vérifie que le contexte est bien chargé
# ────────────────────────────────────────────────────────────────
RUN echo "=== Debug: liste complète du répertoire courant (/app) ==="
RUN ls -la

RUN echo ""
RUN echo "=== Debug: contenu du dossier maths (s'il existe) ==="
RUN ls -la maths || echo "!!! ERREUR : dossier maths INEXISTANT ou inaccessible !!!"

RUN echo ""
RUN echo "=== Debug: maths est-il un dossier ? ==="
RUN test -d maths && echo "OK : maths est un dossier" || echo "KO : maths n'est PAS un dossier"

RUN echo ""
RUN echo "=== Debug: recherche complète du dossier maths ==="
RUN find . -type d -name maths -ls || echo "find ne trouve pas maths nulle part"

RUN echo ""
RUN echo "=== Fin des debug ==="
RUN echo ""

# On installe le package (maintenant que tout est copié)
RUN pip install --no-cache-dir .

# Exposition du port
EXPOSE 8000

# Commande de lancement
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# MLOps Docker – Orchestration Backend / Frontend

Projet d'orchestration d'une API FastAPI (calculs et historique) et d'un dashboard Streamlit, conteneurisé avec Docker et déployé via CI/CD GitHub Actions.

[![CI](https://github.com/lamMerove/mlops_docker/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/lamMerove/mlops_docker/actions/workflows/ci.yml)
[![CD](https://github.com/lamMerove/mlops_docker/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/lamMerove/mlops_docker/actions/workflows/cd.yml)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen.svg)](https://github.com/lamMerove/mlops_docker/actions)

## Architecture

- **Backend** : FastAPI (port 8000) – `app_api/`
  - Calculs (add, sub, square) + historique en base de données
  - Endpoints : `/compute/{operation}`, `/data`
- **Frontend** : Streamlit (port 8501) – `app_front/`
  - Calculateur + historique via appels API
- **Infrastructure** : Docker + docker-compose (multi-services)

## Documentation automatique

Documentation du code générée automatiquement avec Sphinx et hébergée sur Read the Docs :

→ **[Documentation complète (Sphinx)](https://mlops-docker.readthedocs.io/en/latest/)**  
→ [Source du code sur GitHub](https://github.com/lamMerove/mlops_docker/tree/main/app_api)

## Prérequis

- Python 3.10+
- uv[](https://docs.astral.sh/uv/getting-started/installation/)
- Docker & Docker Compose

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/lamMerove/mlops_docker.git
cd mlops_docker

# Installer les dépendances (backend + frontend + dev tools)
uv sync --dev

# Lancer les services (API + Dashboard)
docker compose up --build
Accès :

API : http://localhost:8000 (docs Swagger : http://localhost:8000/docs)
Dashboard Streamlit : http://localhost:8501

Développement local
Bash# Lancer l'API seule (FastAPI + uvicorn)
uv run uvicorn app_api.main:app --reload --port 8000

# Lancer le dashboard seul (Streamlit)
uv run streamlit run app_front/main.py --server.port 8501
Qualité & Sécurité

Linting : ruff (zéro erreur)
Sécurité : gitleaks (aucune clé/mot de passe en clair)
Tests : pytest + pytest-cov → couverture > 80 %
CI/CD : GitHub Actions (lint, security, tests, build Docker multi-stage)

CI/CD

CI : déclenchée sur push main / develop et PR vers main
ruff lint
gitleaks
pytest + coverage

CD : déclenchée sur push main (après CI success)
Build image multi-stage
Push sur Docker Hub : lammerove/mon-api:latest & lammerove/mon-front:latest


Fichiers concernés :

.github/workflows/ci.yml
.github/workflows/cd.yml

Déploiement
Bashdocker compose -f docker-compose.prod.yml up -d
Auteur
Sébastien – Projet MLOps – Mars 2026
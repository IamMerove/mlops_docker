FROM python:3.10-slim


WORKDIR /app

COPY pyproject.toml .

RUN pip install --default-timeout=1000 --no-cache-dir .

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
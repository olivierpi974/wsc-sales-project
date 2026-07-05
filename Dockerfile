FROM python:3.12-slim

WORKDIR  /usr/src/app 

#installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["sh", "-c", "python src/main.py && python src/analysis.py"]
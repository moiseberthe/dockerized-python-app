FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
COPY models/decision-tree.pkl /app/decision-tree.pkl
COPY models/penguins-decision-tree.pkl /app/penguins-decision-tree.pkl

WORKDIR /app
RUN pip install -r requirements.txt

COPY app.py app.py

CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]
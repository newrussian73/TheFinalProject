FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
COPY . .
CMD python -m pytest -s -- /app/tests/
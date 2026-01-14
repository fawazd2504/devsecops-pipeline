FROM python:3.11-slim

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && pip uninstall -y jaraco.context \
 && pip install --no-cache-dir jaraco.context==6.1.0 \
 && rm -rf /root/.cache/pip

COPY app/ .
EXPOSE 5000
CMD ["python", "app.py"]

FROM python:3.9-slim

WORKDIR /app

COPY grafana_metrics_docker.py /app/grafana_metrics_docker.py

RUN pip install --no-cache-dir requests

CMD ["python3", "grafana_metrics_docker.py"]

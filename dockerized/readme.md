The command


```bashrc
docker build -t grafana-metrics-parser .
```

```bashrc
docker run -it -v /path/on/host/:/app \
-e GRAFANA_URL=https://your-grafana-url.com/ \
-e GRAFANA_API_KEY=your-api-key \
grafana-metrics-parser
```

Output:
* promql_metric_names.json
* promql_unique_metric.json

## About

The `grafana_metrics_used.py` is an extension of `grafana_query_scrapper.py` (https://github.com/danielstankw/Grafana-metrics/tree/main/query_scraper).   
It allows to connect to the Grafana API, scrapes all the dashboards looking for two things: variables and PromQL queries, with goal of collecting all the metrics that are being used by the dashboards.  
Once all the queries and variables are collected they are then preprocessed to extract **just** the metrics and further any repeated metrics are deleted and they are sorted in alphabethical order.  

We go from this:

```json
    {
        "dashboard": "MyDashboard / K8s / Cluster / Ephemeral Storage",
        "metric_names": [
            "node_filesystem_avail_bytes",
            "node_filesystem_size_bytes",
            "up"
        ]
    },
    {
        "dashboard": "MyDashboard / K8s / Cluster View",
        "metric_names": [
            "kube_namespace_created",
            "container_cpu_usage_seconds_total",
            "kube_ingress_info",

```

To the final product

```json
    "cluster:namespace:pod_cpu:active:kube_pod_container_resource_limits",
    "cluster:namespace:pod_cpu:active:kube_pod_container_resource_requests",
    "cluster:namespace:pod_memory:active:kube_pod_container_resource_limits",
    "cluster:namespace:pod_memory:active:kube_pod_container_resource_requests",
    "container_cpu_usage_seconds_total",
    "container_memory_cache",
    "container_memory_rss",
    "container_memory_swap",
    "container_memory_working_set_bytes",
    "container_network_receive_bytes_total",
    "container_network_receive_packets_total",
    "container_network_transmit_bytes_total",
    "container_network_transmit_packets_total",
    "kube_configmap_info",
```

By obtaining this list of metrics, user knows exactly what metrics are needed for the existing dashboards to run correctly. Any other metrics can be restricted or fully deleted, thus reducing the amount of metrics being scraped by Prometheus resulting in faster query time, saved memory and more robust monitoring solution. 


### How to run the script? 

To run you will need to modify the following in the `grafana_query_scraper.py`  

```py
if __name__ == "__main__":

    # Your grafana url 
    grafana_url = "<YOUR-GRAFANA-URL>"  
    # API key - read the readme for instructions.
    api_key = "<YOUR-GRAFANA-API-KEY>"
    # File name where the result of scrape will be saved
    file_name = 'grafana_queries.json'
```

Install the relevant dependancies and execute the script:
```bashrc
python3 grafana_query_scrapper.py
```

## Getting Grafana API key

To connect with Grafana API an API key is required. Below I present guide on how to get it.
<div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/db1b3108-3fdc-436b-8b8c-0afcc665b665" alt="Image 1" width="900">
    <img src="https://github.com/user-attachments/assets/67794c8a-255f-46c4-abd5-0049f0a8a4b2" alt="Image 2" width="900">
    <img src="https://github.com/user-attachments/assets/c0dab608-8c0d-42d3-b341-490a6a3926f8" alt="Image 3" width="900">
    <img src="https://github.com/user-attachments/assets/6955109f-155e-4023-aa44-7556458f3faf" alt="Image 4" width="900">
    <img src="https://github.com/user-attachments/assets/a5a7c9be-49b4-427d-a3d2-238fab6b07b2" alt="Image 5" width="900">
    <img src="https://github.com/user-attachments/assets/bf5522aa-d772-4f6d-98a7-2cc9c2fe6bde" alt="Image 6" width="900">
</div>




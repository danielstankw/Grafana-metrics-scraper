## About

The `grafana_metrics_used.py` script extends the functionality of my [Query Scraper](https://github.com/danielstankw/Grafana-metrics/tree/main/query_scraper).   

It connects to the Grafana API and scrapes all the dashboards for two key items: **variables** and **PromQL queries**.   

The goal is to gather all the metrics used in the dashboards.
After collecting the queries and variables, the script preprocesses them to extract only the metrics. It then removes any duplicates and sorts the metrics in alphabetical order.

#### Step 1: We go from this
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
#### Step 2: ... to this - clean :) 
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

By obtaining this list of metrics, users can identify the exact metrics required for the existing dashboards to function correctly. Any unnecessary metrics can be restricted or deleted, reducing the number of metrics scraped by Prometheus. This results in faster query times, saved memory, and a more robust monitoring solution.

## How to run the script? 
>Note: If there will be demand I can dockerize the application and make it more *fancy*. The script is so simple that I kept it in its bare form.

To run you will need to modify the following in the `grafana_query_scraper.py`, and provide your grafana URL as well as Grafana API key (*read further to see how to get it*). 

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
pip install requests
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




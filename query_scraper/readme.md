## About

The purpose of the `grafana_query_scrapper.py` is to connect to the grafana dashboard and scrape PromQL expressions and dashboard variables.  
By doing that user obtains all the relevant metrics needed to run the dashboard successfuly. 

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

## Output

The output has the following form:

```json
        "dashboard": "MyDashboard / K8s / Cluster / Ephemeral Storage",
        "expressions": [
            "max by (instance, mountpoint) (node_filesystem_size_bytes{job='node-exporter', cluster='$cluster', mountpoint=\"/\"})",
            "max by (instance, mountpoint) (node_filesystem_avail_bytes{job='node-exporter', cluster='$cluster', mountpoint=\"/\"})"
        ],
        "variables": [
            "label_values(up{job=\"kube-state-metrics\"},cluster)"
        ]
```

where:
- `dashboard`: dashboard title
- `expressions`: collection of promql quries used in the dashboard
- `variables`: variables used in the dashboard

## What Now?   
For cardinality reduction we will require **just** the metrics name, not the full PromQL queries:

Instead of getting:
```bashrc
max by (instance, mountpoint) (node_filesystem_size_bytes{job='node-exporter', cluster='$cluster', mountpoint=\"/\"})",
```
we wish to get
```bashrc
node_filesystem_size_bytes
```

So that we can use the metrics name in relabeling process to keep those metrics and drop all of the rest.
This can be achieved by running ?????


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




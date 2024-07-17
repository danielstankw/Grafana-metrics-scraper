### About

This scrippt connect to the grafana dashboard and scrapes the PromQL expressions as well as variables. 
By doing that user obtains all the relevant metrics needed for use of the given dashboard.

The example output has the following form:

```json
        "dashboard": "Baxi / K8s / Cluster / Ephemeral Storage",
        "expressions": [
            "max by (instance, mountpoint) (node_filesystem_size_bytes{job='node-exporter', cluster='$cluster', mountpoint=\"/\"})",
            "max by (instance, mountpoint) (node_filesystem_avail_bytes{job='node-exporter', cluster='$cluster', mountpoint=\"/\"})"
        ],
        "variables": [
            "label_values(up{job=\"kube-state-metrics\"},cluster)"
        ]
    },
```

where:
- `dashboard` is dashboard title
- `expressions`: collection of promql quries used in the dashboard
- `variables`: variables used in the dashboard

### What Now?   
To obtain a list of JUST metrics without functions and filters ex.
Instead of getting:
```bashrc
max by (instance, mountpoint) (node_filesystem_size_bytes{job='node-exporter', cluster='$cluster', mountpoint=\"/\"})",
```
we wish to get
```bashrc
node_filesystem_size_bytes
```

So that we can use the metrics name in relabeling process to keep those metrics and drop all of the rest.
This will be done in the following LINK


### Getting Grafana API key

![image](https://github.com/user-attachments/assets/db1b3108-3fdc-436b-8b8c-0afcc665b665)

![image](https://github.com/user-attachments/assets/67794c8a-255f-46c4-abd5-0049f0a8a4b2)
![image](https://github.com/user-attachments/assets/c0dab608-8c0d-42d3-b341-490a6a3926f8)


![image](https://github.com/user-attachments/assets/6955109f-155e-4023-aa44-7556458f3faf)
![image](https://github.com/user-attachments/assets/a5a7c9be-49b4-427d-a3d2-238fab6b07b2)
![image](https://github.com/user-attachments/assets/bf5522aa-d772-4f6d-98a7-2cc9c2fe6bde)




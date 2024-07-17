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



import requests
import json
import re
import os

class GrafanaMetricsParser:
    def __init__(self, grafana_url, api_key):
        self.grafana_url = grafana_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_dashboards(self):
        """Fetch all dashboards from Grafana."""
        response = requests.get(f"{self.grafana_url}/api/search", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_dashboard_json(self, uid):
        """Fetch the JSON model of a dashboard using its UID."""
        response = requests.get(f"{self.grafana_url}/api/dashboards/uid/{uid}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def extract_promql_expressions(self, dashboard_json):
        """Extract PromQL expressions from the dashboard JSON."""
        expressions = []
        for panel in dashboard_json.get('dashboard', {}).get('panels', []):
            if 'targets' in panel:
                for target in panel['targets']:
                    if 'expr' in target:  # Assuming PromQL expressions are in 'expr' field
                        expressions.append(target['expr'])

        templating_list = dashboard_json.get('dashboard', {}).get('templating', {}).get('list', [])
        for item in templating_list:
            definition = item.get('definition', None)
            if definition:
                expressions.append(definition)

        return expressions

    def extract_metric_names(self, promql_expressions):
        """Extract metric names from PromQL expressions."""
        metric_names = set()
        # Pattern to match valid Prometheus metric names
        pattern = re.compile(r'([a-zA-Z_:][a-zA-Z0-9_:]*)\s*[{(]')

        fn_words = ['abs', 'absent', 'absent_over_time', 'ceil', 'changes', 'clamp', 'clamp_max', 'clamp_min', 
        'day_of_month', 'day_of_week', 'day_of_year', 'days_in_month', 'delta', 'deriv', 'exp', 
        'floor', 'histogram_avg', 'histogram_count and histogram_sum', 'histogram_fraction', 
        'histogram_quantile', 'histogram_stddev and histogram_stdvar', 'holt_winters', 'hour', 
        'idelta', 'increase', 'irate', 'label_join', 'label_replace', 'ln', 'log2', 'log10', 
        'minute', 'month', 'predict_linear', 'rate', 'resets', 'round', 'scalar', 'sgn', 'sort', 
        'sort_desc', 'sort_by_label', 'sort_by_label_desc', 'sqrt', 'time', 'timestamp', 'vector', 
        'year', 'by', 'without', 'sum', 'avg', 'rate', 'max', 'min', 'count', 'count_values', 'stddev', 
        'stdvar', 'topk', 'bottomk', 'sort', 'ignoring', 'vector', 'label_values']

        for expr in promql_expressions:
            matches = pattern.findall(expr)
            for match in matches:
                # Check if match is not in fn_words
                if match not in fn_words:
                    metric_names.add(match)
            
        return list(metric_names)

    def save_expressions_to_json(self, data, filename):
        """Save the extracted PromQL expressions to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def save_unique_metric_names_to_json(self, dashboards_data, filename):
        """Extract unique metric names from all dashboards and save to a JSON file."""
        unique_metric_names = set()
        for dashboard_data in dashboards_data:
            unique_metric_names.update(dashboard_data['metric_names'])
        
        sorted_metric_names = sorted(list(unique_metric_names))  # Sort metric names alphabetically

        with open(filename, 'w') as file:
            json.dump(sorted_metric_names, file, indent=4)


    def parse_final_json(self):

        dashboards = self.get_dashboards()
        output = []

        for dashboard in dashboards:
            uid = dashboard['uid']
            dashboard_json = self.get_dashboard_json(uid)
            title = dashboard_json['dashboard']['title']
            expressions = self.extract_promql_expressions(dashboard_json)
            metric_names = self.extract_metric_names(expressions)
            output.append({
            "dashboard": title,
            "metric_names": metric_names
        })
        
        return output
            
    
if __name__ == "__main__":
    
    grafana_url = os.getenv("GRAFANA_URL")
    api_key = os.getenv("GRAFANA_API_KEY")
    
    file_name_metrics = 'promql_metric_names.json'
    file_name_unique_metrics = 'promql_unique_metric.json'

    grafana_metrics_scrapper = GrafanaMetricsParser(grafana_url, api_key)
    output = grafana_metrics_scrapper.parse_final_json()

    grafana_metrics_scrapper.save_expressions_to_json(output, file_name_metrics)
    print(f"Saved PromQL metric names to {file_name_metrics}")

    grafana_metrics_scrapper.save_unique_metric_names_to_json(output, file_name_unique_metrics)
    print(f"Saved unique metric names to {file_name_unique_metrics}")

import requests
import json


class GrafanaScraper:
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
                    if 'expr' in target:  
                        expressions.append(target['expr'])
        return expressions

    def extract_variables_expressions(self, dashboard_json):
        """Extract definition expressions from the dashboard JSON."""
        expressions = []
        templating_list = dashboard_json.get('dashboard', {}).get('templating', {}).get('list', [])
        for item in templating_list:
            definition = item.get('definition', None)
            if definition:
                expressions.append(definition)
        
        return expressions

    def save_expressions_to_json(self, data, filename):
        """Save the extracted PromQL expressions to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def parse_final_json(self):
        """Perform final cleaning and concatination of the scraped queries"""
        dashboards = self.get_dashboards()
        output = []

        for dashboard in dashboards:
            uid = dashboard['uid']
            dashboard_json = self.get_dashboard_json(uid)
            title = dashboard_json['dashboard']['title']
            expressions = self.extract_promql_expressions(dashboard_json)
            variables = self.extract_variables_expressions(dashboard_json)
            output.append({
                "dashboard": title,
                "expressions": expressions,
                "variables": variables
            })
        
        return output



if __name__ == "__main__":

    # Your grafana url 
    grafana_url = "<YOUR-GRAFANA-URL>"  
    # API key - see readme.md for instruction
    api_key = "<YOUR-GRAFANA-API-KEY>"
    # File name where the result of scrape will be saved
    file_name = 'grafana_queries.json'

    # Headers for authentication
    grafana_scrapper = GrafanaScraper(grafana_url, api_key)

    output = grafana_scrapper.parse_final_json()
    grafana_scrapper.save_expressions_to_json(output, file_name)
    print(f"Saved PromQL expressions to {file_name}")

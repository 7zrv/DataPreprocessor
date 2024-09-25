import requests
import json

class DataChecker:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def check_data(self, keys_to_check=None):
        data = self.fetch_data()
        if data is None:
            return None

        # 특정 필드만 확인하려는 경우
        filtered_data = []
        if keys_to_check:
            for item in data.get('data', []):
                filtered_item = {key: item.get(key) for key in keys_to_check}
                filtered_data.append(filtered_item)
        else:
            print(json.dumps(data, indent=2, ensure_ascii=False))

        return filtered_data

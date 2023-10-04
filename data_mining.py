import requests
import json

class DataMining:
    def gather_data_from_sources(self, url):
        response = requests.get(url)
        data = json.loads(response.text)
        return data

if __name__ == '__main__':
    data_mining = DataMining()
    print(data_mining.gather_data_from_sources('https://jsonplaceholder.typicode.com/posts'))
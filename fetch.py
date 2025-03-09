import requests
import pandas as pd

def fetch_pubmed():
    response = requests.get("https://api.github.com")
    
    if response.status_code == 200:
        print("Connected to GitHub API successfully!")
        
        # Create a small DataFrame
        data = {"Message": ["API connection successful!"], "Status Code": [response.status_code]}
        df = pd.DataFrame(data)
        print(df)
    else:
        print("Failed to connect. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_pubmed()
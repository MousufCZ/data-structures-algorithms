import requests

# URL to access all datasets
url = "https://api.ons.gov.uk/datasets/DE3BC0B6-D6C4-4E20-917E-95D7EA8C91DC"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    datasets = response.json()
    
    # Print out dataset names and IDs
    for dataset in datasets['items']:
        print(f"Title: {dataset['title']}, ID: {dataset['id']}")
except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)
except requests.exceptions.RequestException as err:
    print("Error occurred:", err)
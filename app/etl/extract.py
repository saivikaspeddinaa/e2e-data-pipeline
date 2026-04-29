import requests

def extract_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    
    data = response.json()
    
    print("Data extracted successfully!")
    print("Number of records:", len(data))
    
    return data

if __name__ == "__main__":
    extract_data()
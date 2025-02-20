import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    print(f"Response: {response.json()}")
else:
    print(f"Error: {response.status_code}")

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
    }
post_response = requests.post(url,json=data)
if post_response.status_code == 201:
    print(f"Post Response: {post_response.json()}")
else:
    print(f"Error: {post_response.status_code}")

url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {
    "id": 1,
    "title": "updated title",
    "body": "updated body content",
    "userId": 1
    }
put_response = requests.put(url,json=data)
if put_response.status_code == 200:
    print(f"Put Response: {put_response.json()}")
else:
    print(f"Error: {put_response.status_code}")

url = 'https://jsonplaceholder.typicode.com/posts/1'
params = {'userId': 1}
response = requests.get(url, params=params)
if response.status_code == 200:
    print(f"Response: {response.json()}")
else:
    print(f"Error: {response.status_code}")

url = 'https://jsonplaceholder.typicode.com/nonexistent'
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")

except Exception as err:
    print(f"An Error occurred: {err}")
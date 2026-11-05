import requests

url = "https://jsonplaceholder.typicode.com/posts"

# post_data = {
#     "title": "Learning AI Engineering",
#     "body": "Practising POST requests using Python",
#     "userId": 1
# }

ticket_data = {
    "title": "Login Issue",
    "body": "Unable to log into my account",
    "userId": 5
}

response = requests.post(
    url,
    json=ticket_data,
    timeout=10
)

response.raise_for_status()

data = response.json()

print("Status Code:", response.status_code)
print("Response:", data)
print("Title:", data["title"])
print("Created ID:", data["id"])
import requests

url= "https://jsonplaceholder.typicode.com/posts"
try:
    params={
        "userId":1
    }
    response=requests.get(url,params=params,timeout=10)
    response.raise_for_status()
    posts=response.json()

    # print("Total posts:", len(posts))
    # print("First post:", posts[0]["title"])

    import json
    if posts:
        print("First post title:", posts[0]["title"])
        
        # Saves only the posts for the specified userId into the JSON file
        with open("user_posts.json", "w", encoding="utf-8") as file:
            json.dump(posts, file, indent=4)
        print("Successfully saved to user_posts.json")
    else:
        print("No posts found for this user.")
except requests.exceptions.Timeout:
    print("Requests time out")
except requests.exceptions.ConnectionError:
    print("Network connection Failed")
except requests.exceptions.HTTPError as error:
    print("HTTP error occurred:", error)

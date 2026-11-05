import requests

url="https://jsonplaceholder.tcode.com/users"

try:
    response = requests.get(url, timeout=10)

    

    data = response.json()

    print("Request successful!")
    print("Name:", data[0]["name"])
    print("Email:", data[0]["email"])
    print(response.status_code)

    # params={
    #     "userId":1
    # }

    # response=requests.get(url,params=params,timeout=10)



    # print(response.url)
    # print(response.status_code)

    # data=response.json()

    # print(data[0]["id"])
    # print(data[0]["title"])
    # print(data[0]["userId"])

except requests.exceptions.RequestException as Error:
    print("Something went wrong", Error)

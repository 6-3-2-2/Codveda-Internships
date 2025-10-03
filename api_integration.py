import requests  # import the library that helps us talk to the internet

print("😂 RANDOM JOKE GENERATOR")
print("---------------------------------------------------")

# 1. Define the API endpoint (URL where data lives)
url = "https://official-joke-api.appspot.com/random_joke"

try:
    # 2. Send a GET request to the API
    response = requests.get(url, timeout=5)

    # 3. Check if the response is OK (200 means success)
    response.raise_for_status()

    # 4. Convert the response from text → Python dictionary
    data = response.json()

    # 5. Extract the joke setup and punchline
    setup = data["setup"]
    punchline = data["punchline"]

    # 6. Print the joke in a friendly way
    print("Here’s a random joke for you:")
    print("😂 " + setup)
    print("👉 " + punchline)

except requests.exceptions.RequestException as e:
    # 7. If something goes wrong (internet down, bad URL, etc.)
    print("Error fetching data:", e)

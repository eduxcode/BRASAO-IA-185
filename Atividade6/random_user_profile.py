import requests

def get_random_user_profile():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    data = response.json()
    
    user = data["results"][0]
    name = f"{user["name"]["first"]} {user["name"]["last"]}"
    email = user["email"]
    country = user["location"]["country"]
    
    return name, email, country

if __name__ == "__main__":
    name, email, country = get_random_user_profile()
    print("Nome:", name)
    print("Email:", email)
    print("País:", country)

import requests

def find_email(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == 'email':
                print("Email found:", value)
            elif isinstance(value, (dict, list)):
                find_email(value)
    elif isinstance(json_data, list):
        for item in json_data:
            find_email(item)

if __name__ == '__main__':
    print(r'''
    
    .___  ___________                      .___ _____.___.             
    |   | \_   _____/___  __ __  ____    __| _/ \__  |   | ____  __ __ 
    |   |  |    __)/  _ \|  |  \/    \  / __ |   /   |   |/  _ \|  |  \
    |   |  |     \(  <_> )  |  /   |  \/ /_/ |   \____   (  <_> )  |  /
    |___|  \___  / \____/|____/|___|  /\____ |   / ______|\____/|____/ 
               \/                   \/      \/   \/                    
                 
                   姐妹看看内搭～～～ author: b3nguang
    ''')

    username = input("Please input your github username: ")
    api_url = f"https://api.github.com/users/{username}/events"
    response = requests.get(api_url)
    data = response.json()
    find_email(data)

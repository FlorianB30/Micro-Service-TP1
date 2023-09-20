# 1
import requests

# 2
def get_posts(): 
    url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
    response = requests.get(url)
    posts = response.json()
    for post in posts :
        print(post["title"])

# 3 
def get_users(): 
    url = "https://jsonplaceholder.typicode.com/users?_limit=5"
    response = requests.get(url)
    users = response.json()
    for user in users :
        print(user["name"])

# 4
def create_post():
    # title / corps
    title = input("Quel est le titre de votre nouvel article ?")
    body = input("Quel est le corps de votre article ?")

    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        "title": title,
        "body": body
    }

    article = requests.post(url, data).json()
    
    # return ID article
    print(article["id"])

# 5
def main():
    choice = input("Que souhaitez vous faire ? : \n - p : afficher les 5 premiers posts \n - u : afficher les 5 premiers utilisateurs \n - a : créer un nouvel article \n >")

    match(choice):
        case "p":
            get_posts()
        case "u":
            get_users()
        case "a":
            create_post()

main()
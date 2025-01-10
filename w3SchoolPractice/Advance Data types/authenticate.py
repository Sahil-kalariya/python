def user_authentication(username, password):
    predefined_users = {
        "empdb1": "Jue@3$juy0",
        "empdb2": "juRe34@$",
        "admin": "koiUaq$&@ki"
    }
    if username in predefined_users and predefined_users[username] == password:
        return True
    else:
        return False

def main():
    try:
        username = input("Input your userid: ")
        password = input("Input your password: ")
        
        if user_authentication(username, password):
            print("Authentication has been successful. Welcome!", username)
        else:
            print("Authentication failed. Invalid username or password.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
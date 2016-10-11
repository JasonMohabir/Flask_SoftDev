import hashlib

def read_usernames():
    f = open("data/username.csv", "r")
    raw = f.read().strip().split("\n")
    f.close()
    return raw

def read_passwords():
    f = open("data/password.csv", "r")
    raw = f.read().strip().split("\n")
    f.close()
    return raw

def write_data(username, password):
    u = open("data/username.csv", "r")
    p = open("data/password.csv", "r")
    uraw = u.read().strip()
    praw = p.read().strip()
    u.close()
    p.close()
    uraw += "\n" + username
    praw += "\n" + encrypt(password)
    u = open("data/username.csv", "w")
    p = open("data/password.csv", "w")
    u.write(uraw)
    p.write(praw)
    u.close()
    p.close()

def clear_data():
    u = open("../data/username.csv", "w")
    p = open("../data/password.csv", "w")
    u.write("")
    p.write("")
    u.close()
    p.close()

def encrypt(password):
    return hashlib.sha384(password).hexdigest()

def verify(username,password):
    usernames = read_usernames()
    passwords = read_passwords()
    try:
        row = usernames.index(username)
    except:
        return -2 
    if (encrypt(password) == passwords[row]):
        return 1
    return -1

def register(username,password):
    usernames = read_usernames()
    plen = len(password)
    ulen = len(username)

    if username in usernames:
        return -1
    write_data(username,password)
    return 1

if __name__ == "__main__":
    print "Clearing database..."
    clear_data()

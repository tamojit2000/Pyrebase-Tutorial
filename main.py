import sys
import pyrebase


sys.stdout = open('output.txt', 'w')

firebase_config = {
    'apiKey': "AIzaSyBSLIXszBhe_gJ1jyLNp-Be9fWyC-65DeA",
    'authDomain': "pyrebasemine.firebaseapp.com",
    'databaseURL': "https://pyrebasemine-default-rtdb.firebaseio.com/",
    'projectId': "pyrebasemine",
    'storageBucket': "pyrebasemine.appspot.com",
    'messagingSenderId': "330567043508",
    'appId': "1:330567043508:web:2f9cf623502beaadd90ae1",
    'measurementId': "G-TQYLWVH34R"
}

firebase = pyrebase.initialize_app(firebase_config)

auth = firebase.auth()

# LOGIN
'''
email = 'test@gmail.com'
password = 'test123'

try:
    auth.sign_in_with_email_and_password(email, password)
    print('OK')
except Exception as e:
    print(e)
'''
# SIGN UP
'''
email = 'admin@gmail.com'
password = 'admin123'

try:
    x = auth.create_user_with_email_and_password(email, password)
    print('OK', x)
except Exception as e:
    print(e)
'''

# STORAGE
'''
storage = firebase.storage()

try:
    storage.child('Billi.txt').put('Hello.txt')
    storage.child('Shop/Books.txt').put('Hello.txt')

    a = storage.child('Billi.txt').get_url(None)
    b = storage.child('Shop/Books.txt').get_url(None)

    print(a)
    print(b)

    storage.child('Billi.txt').download('', 'download1.txt')

    url = b
    content = urllib.request.urlopen(url).read()
    print(content)

    storage.child('Billi.txt').delete('Billi.txt', None)

except Exception as e:
    print(e)
'''

# DATABASE


db = firebase.database()

'''
try:
    data = {'age': 34, 'marks': 78}
    db.child('first').push(data)
    db.child('first').child('MyId').set(data)
    db.push(data)

except Exception as e:
    print(e)


All = db.get()
for node in All.each():
    print(node.key())
    print(node.val())
    print()

print('K')

All = db.child('first').get()
for node in All.each():
    print(node.key())
    print(node.val())
    print()

db.child('first').child('MyId').update({'marks': 100, 'roll': 56})

print(db.child('first/MyId/roll').get().val())

db.child('first/MyId/roll').remove()
'''

sys.stdout.close()

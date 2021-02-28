username = input('Username: ')
password = input('Password: ')

while username == password:
    print ('Username and password must be different.')
    username = input('Username: ')
    password = input('Password: ')
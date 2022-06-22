with open('users.csv', 'r') as u:
    with open('hobby.csv', 'r') as h:
        users = u.read()
        users = users.split('\n')
        hobby = h.read()
        hobby = hobby.split('\n')
        print(users)
        print(hobby)

users_hobby = {}
i = 0

if len(users) == len(hobby):
  while i < len(users):
    users_hobby[users[i]] = hobby[i]
    i += 1
elif len(users) > len(hobby):
  while i < len(hobby):
    users_hobby[users[i]] = hobby[i]
    i += 1
  while i < len(users):
    users_hobby[users[i]] = None
    i += 1
else:
  print('1')

print(users_hobby)
  
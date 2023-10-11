from collections import Counter

import requests

response = requests.get('https://parsinger.ru/3.4/3/dialog.json').json()

list_usernames = []


def count_users(resp):

    list_usernames.append(resp['username'])

    if resp['comments']:
        for i in resp['comments']:
            count_users(i)
    return list_usernames


not_sorted_names = Counter(count_users(response))
sorted_names = dict(sorted(not_sorted_names.items(), key=lambda x: (-x[1], x[0])))
print(sorted_names)







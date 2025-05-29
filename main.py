import json

# Caricare i dati dai file JSON
with open('./followers_1.json', 'r', encoding='utf-8') as f:
    followers_data = json.load(f)

with open('./following.json', 'r', encoding='utf-8') as f:
    following_data = json.load(f)

# Estrarre i nomi utente dai follower
followers = set()
for entry in followers_data:
    if 'string_list_data' in entry and entry['string_list_data']:
        followers.add(entry['string_list_data'][0]['value'])

# Estrarre i nomi utente dai seguiti
following = set()
for entry in following_data.get("relationships_following", []):
    if 'string_list_data' in entry and entry['string_list_data']:
        following.add(entry['string_list_data'][0]['value'])

# Identificare chi non ricambia il follow
non_followers = following - followers

# Stampare i risultati
print("Persone che segui ma che non ti seguono:")
for user in non_followers:
    print(user)

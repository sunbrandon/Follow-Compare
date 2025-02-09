import json

with open('followers.json', 'r') as f:
    followers_data = json.load(f)

with open('following.json', 'r') as f:
    following_data = json.load(f)

if isinstance(following_data, dict) and "relationships_following" in following_data:
    following_list_raw = following_data["relationships_following"]
else:
    following_list_raw = following_data

if isinstance(followers_data, dict) and "relationships_followers" in followers_data:
    followers_list_raw = followers_data["relationships_followers"]
else:
    followers_list_raw = followers_data

following_list = []
for entry in following_list_raw:
    if isinstance(entry, dict):
        if "string_list_data" in entry and entry["string_list_data"]:
            username = entry["string_list_data"][0]["value"]
            following_list.append(username)
    elif isinstance(entry, str):
        following_list.append(entry)
    else:
        print("Unexpected data type in following:", type(entry))

followers_list = []
for entry in followers_list_raw:
    if isinstance(entry, dict):
        if "string_list_data" in entry and entry["string_list_data"]:
            username = entry["string_list_data"][0]["value"]
            followers_list.append(username)
    elif isinstance(entry, str):
        followers_list.append(entry)
    else:
        print("Unexpected data type in followers:", type(entry))

non_followers = [user for user in following_list if user not in followers_list]

for user in non_followers:
    print(user)

import requests


'''
user_input = input("Enter id: ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"

#GET

get_response = requests.get(get_url)
print(get_response.json())

#POST

todo_item = {"userID" : 2, "title" : "my to do", "completed" : False}
post_url = "https://jsonplaceholder.typicode.com/todos"
#optional header
headers = {"Content-Type" : "application/json"}
post_response = requests.post(post_url, json = todo_item, headers= headers)
print(post_response.json())
'''

get_url = f"https://jsonplaceholder.typicode.com/todos/15"


#PUT
to_do_item_15 = {"userId": 2, "title": "put title", "completed": False}
#put_response = requests.put(get_url, json=to_do_item_15)
#print(put_response.json())

#PATCH
to_do_item_patch_15 = {"title": "Patch Test"}
#patch_response = requests.patch(get_url,json=to_do_item_patch_15)
#print(patch_response.json())

#DELETE
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)
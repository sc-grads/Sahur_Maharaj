import json, requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

print(todos)

for t in todos:
    if t['completed']:
        print(t)

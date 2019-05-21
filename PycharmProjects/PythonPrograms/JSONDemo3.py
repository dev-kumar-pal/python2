import json
import requests

todos_by_user = {}
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos	 = json.loads(response.text)

#todos == response.json()

print(json.dumps(todos,indent=2))

import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        #print(response.content)
        response.encoding = "utf-8"
        #print(response.text)
        #print(response.json())
        #print(response.headers)
        print(response.headers['Content-Type'])
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print('Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
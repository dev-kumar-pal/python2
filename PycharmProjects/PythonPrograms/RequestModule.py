import requests

'''r = requests.get('https://www.python.org/')
print(r.text)'''


#r = requests.get('https://customer-stories-feed.github.com/customer_stories/mgm-resorts/hero.jpg')
#print(r.content)

'''with open('image.png','wb') as f:
    f.write(r.content)'''

#payload = {'page':2,'count':25}
#payload = {'username':'Edris','Password':1234567890}
'''r = requests.post('https://httpbin.org/post',data=payload)
#print(r.url)
#print(r.text)
print(r.json())
print(r.ok)'''

r = requests.get('https://httpbin.org/basic-auth/edris/123456',auth=('edris','123456'))
print(r)
print(r.text)
import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '0618732987',
  'message': 'Hello world',
  'key': 'textbelt',
})
# print(resp.json())
print("sent")
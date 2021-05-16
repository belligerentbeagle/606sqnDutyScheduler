import base64

data = open("/Users/weiyushit/OneDrive/Github stuff/teststreamlit/test.xlsx", 'rb').read()
base64_encoded = base64.b64encode(data).decode('UTF-8')

print(base64_encoded)


# %%
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context

# %%
#3.8
#获取AP名字，位置等等
import http.client

conn = http.client.HTTPSConnection("117.78.31.209:26335")

headers = { 'x-auth-token': "budDCq6r1SC/t5BlOdsANs86r84bRztFIGJ2QI9eEDk=" }

conn.request("GET", "/rest/campuswlantopowebsite/v1/wlantopo/topoinfo?param=%7B%22id%22%3A%22540d8574-a743-4cda-a47e-3718b6a4f722%22%2C%22level%22%3A3%2C%22type%22%3A%22floor%22%7D&=&=", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


# %%
#3.9
#获取用户终端名字，位置等等
import http.client

conn = http.client.HTTPSConnection("117.78.31.209:26335")

headers = { 'x-auth-token': "budDCq6r1SC/t5BlOdsANs86r84bRztFIGJ2QI9eEDk=" }

conn.request("POST", "/rest/campusrtlswebsite/v1/clientlocation/lastlocation?param=%7B%22id%22%3A%22540d8574-a743-4cda-a47e-3718b6a4f722%22%2C%22level%22%3A3%2C%22type%22%3A%22floor%22%7D&=&=", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



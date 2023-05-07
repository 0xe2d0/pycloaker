# 💥 PyCloaker - A Cloaking Module

**Cloaking Module For Python**

# 🤖 Installation
```bash
pip install pycloaker
```

# ✨ What It Does ?

You can cloak your python based website with this module.<br/>
There is what does the module do :

* Checks User-Agent
* Checks ASN Company
* Blocks Cities You Determined
* Blocks Countries You Determined
* Blocks Ip Addresses You Determined


There is what you can do with this module :

* Block Ip Addresses
* Block Cities
* Block Countries


# ♣ Usage

```python
from pycloaker import *

url_is_humans_redirect = "https://x.com"
url_is_bots_redirect = "https://a.com"

clients_ip = "85.233.55.78"
clients_user_agent = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_2_9) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/47.0.2873.193 Safari/537"

cloaker = PyCloaker(
    url_is_humans_redirect,
    url_is_bots_redirect
)

cloaker.blockedCities(["paris","london"])
cloaker.blockedCountries(["us","ru"])
cloaker.blockedIpAddresses(["85.233.97.58"])

url = cloaker.cloak(clients_ip,clients_user_agent)

print(url)
```
It's gonna print *https://x.com*. Because there isn't any match with determined rules.

Trying another example:
```python
from pycloaker import *

url_is_humans_redirect = "https://x.com"
url_is_bots_redirect = "https://a.com"

clients_ip = "85.233.55.78"
clients_user_agent = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_2_9) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/47.0.2873.193 Safari/537"

cloaker = PyCloaker(
    url_is_humans_redirect,
    url_is_bots_redirect
)

cloaker.blockedIpAddresses(["1.1.1.1","85.233.55.78"])

url = cloaker.cloak(clients_ip,clients_user_agent)

print(url)
```
It's gonna print *https://a.com*. Because client's ip address is matches with determined ip address.

You can see its very easy and user friendly. 


# 🕶 Usage in Flask

```python
from flask import Flask,url_for,redirect,request
from pycloaker import PyCloaker

app = Flask(__name__)

cloaker = PyCloaker("/human-url","/bot-url")
cloaker.blockedCountries(["rus","us"])

@app.route("/")
def index():
    #ip = request.headers['X-Forwarded-For'] # If its a real website you can use that
    ip = "85.214.122.50" # We determined this statically. Just a random ip
    userAgent = request.headers["User-Agent"]

    url = cloaker.cloak(ip,userAgent)

    return redirect(url)


@app.route("/human-url")
def human():
    return "You're a human!"

@app.route("/bot-url")
def bot():
    return "You're a bot :("


if __name__ == "__main__":
    app.run(debug=True)

```


# WARNING : THIS MODULE MADE FOR JUST TESTS AND EDUCATİONAL PURPOSE.
# DO NOT USE THAT IN A REAL WEBSITE
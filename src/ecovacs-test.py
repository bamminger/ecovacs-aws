from sucks import *

config = {
    "device_id": EcoVacsAPI.md5(str(time.time())), # value taken from the sucks source
    "email": "***", # fill in your email
    "password_hash": EcoVacsAPI.md5("***"), # fill in your password
    "country": "***", # your ecovacs country e.g. at
    "continent": "***" # your continent e.g. eu
}

api = EcoVacsAPI(config['device_id'], config['email'], config['password_hash'], config['country'], config['continent'])

my_vac = api.devices()[0]
vacbot = VacBot(api.uid, api.REALM, api.resource, api.user_access_token, my_vac, config['continent'])
vacbot.connect_and_wait_until_ready()

vacbot.run(Charge()) # Run your activity

print('Action executed')
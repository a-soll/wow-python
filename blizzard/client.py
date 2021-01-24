from blizzard import config
from blizzard.models.pet import Pet
import requests

class Blizz_Conn:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client = requests.session()
        self.login()

    def login(self):
        headers = {}
        data = {
            'grant_type': 'client_credentials'
        }
        response = self.client.post('https://us.battle.net/oauth/token', data=data, auth=(self.client_id, self.client_secret))
        token = response.json()['access_token']
        headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'applications/json'
        })
        self.client.headers.update(headers)

    def get_pet_by_name(self, name):
        pet = ''
        params = {
            ':region': 'us',
            'namespace': 'static-us',
            'locale': 'en_US',
        }
        url = f'{config.baseurl}/data/wow/pet/index'
        response = self.client.get(url, params=params)
        pets = response.json()['pets']
        for pet_item in pets:
            if pet_item['name'].lower() == name.lower():
                pet = Pet(self.client, pet_item)
        return pet

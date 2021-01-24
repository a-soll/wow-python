import requests

class Pet:
    def __init__(self, client, fields):
        self.name = fields['name']
        self.id = fields['id']
        self.key = fields['key']
        self.client = client
        self.fields = fields


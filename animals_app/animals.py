import os
import pprint
import requests
from dotenv import load_dotenv


class Animals:
    '''
    A class to get info based on a animals name
    Enter the full name for animal and the applction 
    will show for you some information for this animal
    chosse the The information you want to know about it
    '''
    
    instance_caunt=0
    __instance__=None

    def __init__(self):
        if Animals.__instance__ is None:
            Animals.__instance__ = self
            self.name=None
            self.r=None
            self.api_key=os.getenv("api_key")
            Animals.instance_caunt+=1
        else:
            raise Exception("We can't create another class")
        
    def set_name(self,name):
        self.name=name
        self.update_data()

    def update_data(self):
        self.api_url= f'https://api.api-ninjas.com/v1/animals?name={self.name}'
        self.r = requests.get(self.api_url, headers={'X-Api-Key': self.api_key}).json() # respose

    def get_color(self):
        color=self.r[0]['characteristics']['color']
        return color

    def get_length(self):
        length=self.r[0]['characteristics']['length']
        return length

    def get_lifeSpan(self):
        lifeSpan=self.r[0]['characteristics']['lifespan']
        return lifeSpan

    def get_locations(self):
        locations=self.r[0]['locations']
        locations = ' - '.join(locations)
        return locations

    def get_animale_belongs(self):
        belongs=self.r[0]['taxonomy']['family']
        return belongs
    
    def get_full_name(self):
        full_name=self.r[0]['name']
        return full_name

load_dotenv()

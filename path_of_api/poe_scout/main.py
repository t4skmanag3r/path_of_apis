from path_of_api.poe_scout.currencies import Currencies
from path_of_api.poe_scout.default import Default
from path_of_api.poe_scout.items import Items
from path_of_api.poe_scout.leagues import Leagues
from path_of_api.poe_scout.realms import Realms
from path_of_api.poe_scout.uniques import Uniques


class Poe2ScoutAPI:
    def __init__(self, base_url: str = "https://poe2scout.com/api"):
        self.base_url = base_url
        self.default = Default(base_url)
        self.realms = Realms(base_url)
        self.leagues = Leagues(base_url)
        self.items = Items(base_url)
        self.uniques = Uniques(base_url)
        self.currencies = Currencies(base_url)

    
    

    
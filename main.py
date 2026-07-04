from path_of_apis.poe_scout.api import Poe2ScoutAPI

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
def test_default(api: Poe2ScoutAPI):
    print("Testing /Health")
    try:
        print(api.default.check_live())
        print(api.default.check_ready())
        print(f"{GREEN}/Health Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Health Failed ✗: {RESET}", e)
def test_realms(api: Poe2ScoutAPI, realm: str):
    print("Testing /Realms", end="")
    try:
        print(api.realms.get_realms()[0])
        print(api.realms.get_filters(realm)[0])
        print(api.realms.get_landing_splash_info(realm)[0])
        print(f"{GREEN}✓/Realms Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Realms Failed ✗: {RESET}", e)

def test_leagues(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Leagues for", realm, end="")
    try:
        print(api.leagues.get_leagues(realm)[0])
        print(api.leagues.get_exchange_snapshot(realm, league))
        print(api.leagues.get_reference_currencies(realm, league)[0])
        print(api.leagues.get_snapshot_history(realm, league, limit=3))
        print(api.leagues.get_snapshot_pairs(realm, league)[0])
        print(f"{GREEN}✓/Leagues Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Leagues Failed ✗: {RESET}", e)

def test_items(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Items", end="")
    try:
        print(api.items.get_items(realm, league)[0])
        print(api.items.get_categories(realm, league).CurrencyCategories[0])
        print(api.items.get_price_history(realm, league)[0])
        print(api.items.get_item_history(realm, league, item_id=1, log_count=8))
        print(f"{GREEN}✓/Items Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Items Failed ✗: {RESET}", e)

def test_uniques(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Uniques", end="")
    try:
        print(api.uniques.get_category_items(realm, league, category = "accessory").Items[0])
        print(f"{GREEN}✓/Uniques Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Uniques Failed ✗: {RESET}", e)

def test_currencies(api: Poe2ScoutAPI, realm: str, league:str):
    print("Testing /Currencies", end="")
    try:
        print(api.currencies.get_currency(realm, league, "chaos"))
        print(api.currencies.get_by_category(realm, league, "fragments").Items[0])
        print(api.currencies.get_pair_history(realm, league, 291, 295, limit=2))
        print(f"{GREEN}✓/Currencies Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Currencies Failed ✗: {RESET}", e)

def main():
    api = Poe2ScoutAPI()
    test_default(api)
    test_realms(api, realm="poe2")
    test_leagues(api, realm="poe2", league="runes")
    test_items(api, realm="poe2", league="runes")
    test_uniques(api, realm="poe2", league="runes")
    test_currencies(api, realm="poe2", league="runes")


if __name__ == "__main__":
    main()

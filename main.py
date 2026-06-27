from path_of_api.poe_scout.main import Poe2ScoutAPI

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
def test_realms(api: Poe2ScoutAPI):
    print("Testing /Realms", end="")
    try:
        print(api.realms.get_realms()[0])
        print(f"{GREEN}✓/Realms Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Realms Failed ✗: {RESET}", e)

def test_leagues(api: Poe2ScoutAPI, realm: str):
    print("Testing /Leagues for", realm, end="")
    try:
        print(api.leagues.get_leagues(realm)[0])
        print(f"{GREEN}✓/Leagues Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Leagues Failed ✗: {RESET}", e)

def test_items(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Items", end="")
    try:
        print(api.items.get_items(realm, league)[0])
        print(f"{GREEN}✓/Items Passed ✓{RESET}")
    except Exception as e:
        print(f"{RED}/Items Failed ✗: {RESET}", e)
def main():
    api = Poe2ScoutAPI()
    test_default(api)
    test_realms(api)
    test_leagues(api, realm="poe2")
    test_items(api, realm="poe2", league="runes")


if __name__ == "__main__":
    main()

import pytest

from path_of_apis.poe_scout.api import Poe2ScoutAPI

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

@pytest.fixture
def api():
    return Poe2ScoutAPI()

@pytest.mark.parametrize("realm", ["poe2"])
@pytest.mark.parametrize("league", ["runes"])
def test_default(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Health")
    api.default.check_live()
    api.default.check_ready()
    print(f"{GREEN}/Health Passed ✓{RESET}")

@pytest.mark.parametrize("realm", ["poe2"])
@pytest.mark.parametrize("league", ["runes"])
def test_realms(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Realms", end="")
    api.realms.get_realms()[0]
    api.realms.get_filters(realm)[0]
    api.realms.get_landing_splash_info(realm)[0]
    print(f"{GREEN}✓/Realms Passed ✓{RESET}")

@pytest.mark.parametrize("realm", ["poe2"])
@pytest.mark.parametrize("league", ["runes"])
def test_leagues(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Leagues for", realm, end="")
    api.leagues.get_leagues(realm)
    api.leagues.get_exchange_snapshot(realm, league)
    api.leagues.get_reference_currencies(realm, league)
    api.leagues.get_snapshot_history(realm, league, limit=3)
    api.leagues.get_snapshot_pairs(realm, league)
    print(f"{GREEN}✓/Leagues Passed ✓{RESET}")

@pytest.mark.parametrize("realm", ["poe2"])
@pytest.mark.parametrize("league", ["runes"])
def test_items(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Items", end="")
    api.items.get_items(realm, league)
    api.items.get_categories(realm, league).CurrencyCategories
    api.items.get_price_history(realm, league)
    api.items.get_item_history(realm, league, item_id=1, log_count=8)
    print(f"{GREEN}✓/Items Passed ✓{RESET}")

@pytest.mark.parametrize("realm", ["poe2"])
@pytest.mark.parametrize("league", ["runes"])
def test_uniques(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Uniques", end="")
    api.uniques.get_category_items(realm, league, category="accessory").Items
    print(f"{GREEN}✓/Uniques Passed ✓{RESET}")

@pytest.mark.parametrize("realm", ["poe2"])
@pytest.mark.parametrize("league", ["runes"])
def test_currencies(api: Poe2ScoutAPI, realm: str, league: str):
    print("Testing /Currencies", end="")
    api.currencies.get_currency(realm, league, "chaos")
    api.currencies.get_by_category(realm, league, "fragments").Items
    api.currencies.get_pair_history(realm, league, 291, 295, limit=2)
    print(f"{GREEN}✓/Currencies Passed ✓{RESET}")
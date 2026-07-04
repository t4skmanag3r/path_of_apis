# Path of Apis

**A single Python library for multiple APIs that cover Path of Exile**, currently supporting **poe2scout.com**.

## Overview

`path_of_apis` is a Python library designed to provide a clean, type-safe, and easy-to-use interface for interacting with various APIs related to **Path of Exile (PoE)**. Currently, it supports the **poe2scout.com** API, which provides data on items, leagues, currencies, and more.

This library is built with **type hints** and **modular design** in mind, making it easy to extend to support additional APIs in the future.

## Installation

```bash
pip install path_of_apis
```

## Usage

### ✅ Basic Example

```python
from path_of_apis.poe_scout.api import Poe2ScoutAPI

api = Poe2ScoutAPI()
api.default.check_live()
api.default.check_ready()
```

### 📦 Available Endpoints

- `/Health` - Check if the API is live and ready
- `/Realms` - Get realm data
- `/Leagues` - Get league data and exchange info
- `/Items` - Get item data, price history, and more
- `/Uniques` - Get unique item data
- `/Currencies` - Get currency data and exchange history

## 🧠 Type Hints

All classes and methods are fully typed with Python's type hints, ensuring better code readability and IDE support.

Example:

```python
from path_of_apis.poe_scout.api import Poe2ScoutAPI

api: Poe2ScoutAPI = Poe2ScoutAPI()
item: Item = api.items.get_items("poe2", "runes")[0]
```

## 🧪 Testing

This project includes a full test suite using `pytest`, and you can run it with:

```bash
pytest tests/test_poe_scout.py
```

## Example Usage

### Get Realms

```python
from path_of_apis.poe_scout.api import Poe2ScoutAPI

api = Poe2ScoutAPI()
realms = api.realms.get_realms()
print(realms)
```

### Get Leagues

```python
from path_of_apis.poe_scout.api import Poe2ScoutAPI

api = Poe2ScoutAPI()
leagues = api.leagues.get_leagues("poe2")
print(leagues)
```

### Get Items

```python
from path_of_apis.poe_scout.api import Poe2ScoutAPI

api = Poe2ScoutAPI()
items = api.items.get_items("poe2", "runes")
for item in items:
    print(f"{item.Name}: {item.CurrentPrice}")
```

## License

MIT License

## Contributing

Contributions are welcome! If you'd like to add support for additional APIs or improve the library, feel free to open a PR or issue.


## Roadmap

- Add support for more PoE APIs
- Improve type hints and documentation
- Add more detailed error handling
- Add async support for faster API calls

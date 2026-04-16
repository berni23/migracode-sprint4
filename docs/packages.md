# Python Packages

## What is a package?

A package is a collection of code that someone else has written and published so you can reuse it. Instead of writing everything from scratch, you install a package and import it into your project.

Python has two kinds:

1. **Built-in (standard library)** — comes pre-installed with Python. No installation needed, just `import` and use.
2. **Third-party packages** — written by the community and published on [PyPI](https://pypi.org/) (Python Package Index). You install these with `pip` or `uv add`.

---

## Built-in packages (standard library)

These are always available — no installation required.

### `json` — working with JSON data

```python
import json

data = {"name": "Ada", "age": 25}

# Convert dict to JSON string
text = json.dumps(data, indent=2)
print(text)

# Parse JSON string back to dict
parsed = json.loads(text)
print(parsed["name"])  # Ada
```

### `os` — interacting with the operating system

```python
import os

# Check if a file exists
print(os.path.exists("myfile.txt"))

# List files in a directory
print(os.listdir("."))

# Create a directory
os.makedirs("output", exist_ok=True)

# Get environment variables
print(os.getenv("HOME"))
```

### `datetime` — dates and times

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))  # 2026-04-18 14:30

# Date arithmetic
tomorrow = now + timedelta(days=1)
print(tomorrow.strftime("%A"))  # day of the week
```

### `math` — mathematical functions

```python
import math

print(math.sqrt(144))    # 12.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
print(math.pi)           # 3.141592653589793
```

### `random` — random numbers and choices

```python
import random

print(random.randint(1, 10))              # random int between 1 and 10
print(random.choice(["red", "blue"]))     # pick one at random
print(random.shuffle([1, 2, 3, 4, 5]))    # shuffle a list in place
```

### `csv` — reading and writing CSV files

```python
import csv

# Writing
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade"])
    writer.writerow(["Ada", 92])
    writer.writerow(["Bob", 45])

# Reading
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['Name', 'Grade'], ['Ada', '92'], ...
```

### Others worth knowing

| Package | What it does |
|---|---|
| `pathlib` | Modern file path handling (alternative to `os.path`) |
| `collections` | Specialized data structures (`Counter`, `defaultdict`) |
| `re` | Regular expressions for pattern matching |
| `urllib` | Make HTTP requests (basic, no install needed) |
| `sqlite3` | Embedded SQL database |
| `sys` | Access to Python interpreter settings and arguments |

Full list: [Python Standard Library docs](https://docs.python.org/3/library/)

---

## Third-party packages

These are published on [PyPI](https://pypi.org/) and need to be installed. Here are some of the most popular ones.

### `requests` — HTTP requests made simple

The go-to package for calling APIs. Much simpler than the built-in `urllib`.

```bash
uv add requests
```

```python
import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()
print(data["name"])      # The Octocat
print(data["location"])  # San Francisco
```

### `python-dotenv` — load environment variables from `.env` files

Keeps secrets (API keys, passwords) out of your code.

```bash
uv add python-dotenv
```

```
# .env file
API_KEY=abc123secret
DEBUG=true
```

```python
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("API_KEY"))  # abc123secret
```

### `rich` — beautiful terminal output

Colors, tables, progress bars, and more in the terminal.

```bash
uv add rich
```

```python
from rich import print
from rich.table import Table

table = Table(title="Students")
table.add_column("Name")
table.add_column("Grade")
table.add_row("Ada", "92")
table.add_row("Bob", "45")
print(table)
```

### `flask` — lightweight web framework

Build web servers and APIs in a few lines.

```bash
uv add flask
```

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

app.run()  # visit http://localhost:5000
```

### `pandas` — data analysis

The standard tool for working with tabular data (spreadsheets, CSVs, databases).

```bash
uv add pandas
```

```python
import pandas as pd

df = pd.read_csv("students.csv")
print(df.head())                        # first 5 rows
print(df["grade"].mean())               # average grade
print(df[df["grade"] >= 70])            # filter rows
```

### Other popular packages

| Package | What it does |
|---|---|
| `fastapi` | Modern web framework (async, auto-docs) |
| `pytest` | Testing framework |
| `black` | Code formatter |
| `pillow` | Image processing |
| `matplotlib` | Charts and graphs |
| `beautifulsoup4` | HTML/web scraping |
| `sqlalchemy` | Database ORM |

---

## Exercise: Build a GitHub profile viewer

Create a small CLI tool that fetches a GitHub user's profile and displays it in the terminal using `requests` and `rich`.

### Setup

```bash
uv init github-viewer
cd github-viewer
uv add requests rich
```

### Tasks

Write a script `main.py` that:

1. **Asks the user for a GitHub username** using `input()`
2. **Fetches their profile** from the GitHub API: `https://api.github.com/users/{username}`
3. **Handles errors** — if the user doesn't exist (status code 404), print a message and exit
4. **Displays a formatted table** using `rich` with:
   - Name
   - Bio
   - Location
   - Public repos (number)
   - Followers
5. **Fetches their repositories** from: `https://api.github.com/users/{username}/repos`
6. **Shows their 5 most starred repos** in a second table with columns: Repo Name, Stars, Language

### Expected output

```
Enter a GitHub username: octocat

┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field        ┃ Value                          ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Name         │ The Octocat                    │
│ Bio          │ -                              │
│ Location     │ San Francisco                  │
│ Public repos │ 8                              │
│ Followers    │ 16432                          │
└──────────────┴────────────────────────────────┘

Top repositories by stars:
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━┓
┃ Repo               ┃ Stars ┃ Language   ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━┩
│ Hello-World         │ 2541  │ -          │
│ Spoon-Knife         │ 12542 │ HTML       │
│ ...                 │ ...   │ ...        │
└─────────────────────┴───────┴────────────┘
```

### Hints

- `response.status_code` gives you the HTTP status code
- Use `response.json()` to parse the response body
- To sort repos by stars: `sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)`
- Some fields might be `None` — use `or "-"` to display a fallback (e.g. `data["bio"] or "-"`)

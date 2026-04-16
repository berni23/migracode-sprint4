# Virtual Environments in Python

## What problem do they solve?

In JavaScript, when you run `npm install`, packages go into a `node_modules/` folder **inside your project**. Each project gets its own dependencies — they don't interfere with each other.

Python doesn't work like that by default. If you run `pip install requests`, it installs the package **globally** — every Python project on your machine shares it. This causes problems:

- Project A needs `requests==2.28` but Project B needs `requests==2.31`
- You install something for one project and accidentally break another
- You can't tell which packages a specific project actually needs

**Virtual environments** fix this. They create an **isolated Python installation per project**, just like `node_modules` does for JavaScript.

| Concept | JavaScript | Python |
|---|---|---|
| Isolated dependencies | `node_modules/` (automatic) | Virtual environment (manual setup) |
| Dependency file | `package.json` | `requirements.txt` |
| Lock file | `package-lock.json` | `requirements.txt` (with pinned versions) |
| Install dependencies | `npm install` | `pip install -r requirements.txt` |
| Add a package | `npm install axios` | `pip install requests` |

---

## Using `venv` + `pip` (built-in)

Python ships with `venv` — no extra installation required.

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

This creates a `venv/` folder in your project with its own copy of Python and pip. The folder name `venv` is a convention — you can call it anything, but `venv` or `.venv` are the most common.

### 2. Activate it

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

Once activated, your terminal prompt changes to show `(venv)` at the beginning. This tells you that `python` and `pip` now point to the virtual environment, not your global installation.

### 3. Install packages

```bash
pip install requests
```

This installs `requests` **only inside the virtual environment**. Other projects are not affected.

### 4. Save your dependencies

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file listing every installed package and its exact version:

```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

This is your equivalent of `package.json` + `package-lock.json` combined — share it with your team so they can reproduce your environment.

### 5. Install from requirements.txt

When someone else clones your project (or you set it up on a new machine):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

This is the Python equivalent of `npm install`.

### 6. Deactivate

```bash
deactivate
```

This returns you to your global Python installation.

### Quick reference

```bash
# Full workflow from scratch
python3 -m venv venv          # create
source venv/bin/activate      # activate (macOS/Linux)
pip install requests          # install packages
pip freeze > requirements.txt # save dependencies
deactivate                    # leave the environment
```

### Important: add `venv/` to `.gitignore`

Just like you never commit `node_modules/`, never commit the `venv/` folder. Add it to your `.gitignore`:

```
venv/
```

The `requirements.txt` file is what you commit — not the environment itself.

---

## Bonus: `uv` — a faster alternative

[`uv`](https://github.com/astral-sh/uv) is a modern Python package manager written in Rust. Think of it as **npm for Python** — it handles virtual environments, package installation, and even Python version management, all in one tool. It's dramatically faster than `pip`.

### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# or with Homebrew
brew install uv
```

### The workflow with uv

`uv` simplifies the process — you don't need to manually create or activate environments.

#### Initialize a project

```bash
uv init my-project
cd my-project
```

This creates a `pyproject.toml` (the modern replacement for `requirements.txt`) and sets up the project structure.

#### Add a package

```bash
uv add requests
```

This automatically:
- Creates a virtual environment (`.venv/`) if one doesn't exist
- Installs the package
- Updates `pyproject.toml` and `uv.lock`

Compare this to the `venv` + `pip` workflow where you had to create the environment, activate it, install, and freeze — `uv add` does it all in one command.

#### Run your code

```bash
uv run python main.py
```

`uv run` executes the command inside the virtual environment without you having to activate it first. This is similar to `npx` in JavaScript.

#### Install from an existing project

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock` and installs everything — like `npm install`.

### Quick comparison

| Task | venv + pip | uv |
|---|---|---|
| Create environment | `python3 -m venv venv` | automatic on first `uv add` |
| Activate | `source venv/bin/activate` | not needed (`uv run`) |
| Install a package | `pip install requests` | `uv add requests` |
| Save dependencies | `pip freeze > requirements.txt` | automatic (`pyproject.toml`) |
| Install from file | `pip install -r requirements.txt` | `uv sync` |
| Run a script | `python main.py` (after activate) | `uv run python main.py` |
| Speed | slow | very fast |

### Which should you use?

- **`venv` + `pip`** — use this to learn how Python packaging works under the hood. It's built-in and universal — you'll find it everywhere.
- **`uv`** — use this for real projects. It's faster, simpler, and handles the tedious parts for you. If you're coming from JavaScript, `uv` will feel much more familiar.

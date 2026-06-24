# Python Roadmap
### From Absolute Beginner to Advanced Pythonista
 
---
 
# Table of Contents
 
1. [Python Basics](#1-python-basics)
2. [Control Flow & Functions](#2-control-flow--functions)
3. [Data Structures](#3-data-structures)
4. [File Handling & I/O](#4-file-handling--io)
5. [Object-Oriented Programming](#5-object-oriented-programming)
6. [Modules, Packages & Virtual Environments](#6-modules-packages--virtual-environments)
7. [Error Handling & Debugging](#7-error-handling--debugging)
8. [Iterators, Generators & Functional Tools](#8-iterators-generators--functional-tools)
9. [Regular Expressions](#9-regular-expressions)
10. [Working with APIs & HTTP](#10-working-with-apis--http)
11. [Databases](#11-databases)
12. [Testing](#12-testing)
13. [Concurrency & Parallelism](#13-concurrency--parallelism)
14. [Data Science & Analysis](#14-data-science--analysis)
15. [Web Development](#15-web-development)
16. [Automation & Scripting](#16-automation--scripting)
17. [Advanced Python Internals](#17-advanced-python-internals)
18. [Certifications Along the Journey](#certifications-along-the-journey)
19. [Real-World Projects](#-real-world-projects)
20. [Learning Resources](#-learning-resources)
21. [Complete Learning Path Summary](#%EF%B8%8F-complete-learning-path-summary)
---
 
## 1. Python Basics
 
> **Goal:** Get comfortable with Python syntax, how to run code, and the core building blocks.
> **Estimated Time:** 2–3 weeks
 
#### Core Topics
 
- Installing Python & setting up your environment (VS Code / PyCharm)
- Running scripts (`python script.py`) vs interactive REPL
- Variables and data types (`int`, `float`, `str`, `bool`, `None`)
- Type conversion (`int()`, `str()`, `float()`)
- Arithmetic, comparison, and logical operators
- String formatting (f-strings, `.format()`)
- User input with `input()`
- Comments and code style (PEP 8 basics)
```python
# Hello World & variables
name = "Alice"
age = 30
pi = 3.14159
is_active = True
 
print(f"Hello, {name}! You are {age} years old.")
 
# Type conversion
user_input = input("Enter a number: ")
number = int(user_input)
print(f"Double: {number * 2}")
 
# String operations
greeting = "  hello world  "
print(greeting.strip().title())   # Hello World
print(greeting.upper())
print(len(greeting))
```
 
#### Checklist
- [ ] Install Python 3.x and run your first script
- [ ] Use all basic data types and understand type coercion
- [ ] Write and format strings using f-strings
- [ ] Accept and process user input
- [ ] Follow PEP 8 naming and spacing conventions
---
 
## 2. Control Flow & Functions
 
> **Goal:** Control program logic with conditionals and loops, and organize code into reusable functions.
> **Estimated Time:** 2–3 weeks
 
#### Core Topics
 
- `if`, `elif`, `else` statements
- Ternary expressions
- `for` and `while` loops
- Loop control: `break`, `continue`, `pass`
- Defining functions with `def`
- Parameters, default values, `*args`, `**kwargs`
- Return values & scope (`local` vs `global`)
- Lambda functions
- Recursion basics
```python
# Conditionals & ternary
score = 85
grade = "Pass" if score >= 50 else "Fail"
 
# Loops
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
 
# Functions
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
 
def sum_all(*args):
    return sum(args)
 
# Lambda
square = lambda x: x ** 2
 
# Recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
 
print(factorial(5))   # 120
```
 
#### Checklist
- [ ] Write conditionals covering all edge cases
- [ ] Use `for` loops with `range()`, `enumerate()`, and `zip()`
- [ ] Write functions with default and keyword arguments
- [ ] Explain variable scope (local vs global vs enclosing)
- [ ] Write a simple recursive function (factorial, Fibonacci)
---
 
## 3. Data Structures
 
> **Goal:** Master Python's built-in data structures — the foundation for almost every real program.
> **Estimated Time:** 3–4 weeks
 
#### Core Topics
 
- **Lists:** indexing, slicing, list comprehensions, common methods
- **Tuples:** immutability, unpacking, named tuples
- **Dictionaries:** CRUD operations, dict comprehensions, `defaultdict`, `Counter`
- **Sets:** set operations (union, intersection, difference)
- **Strings:** immutability, slicing, common methods
- Choosing the right structure for a given problem
```python
# List comprehensions
squares = [x**2 for x in range(10) if x % 2 == 0]
 
# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
 
# Unpacking
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
 
# Counter — word frequency
from collections import Counter, defaultdict
text = "the quick brown fox the fox"
freq = Counter(text.split())
print(freq.most_common(2))  # [('the', 2), ('fox', 2)]
 
# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)   # intersection: {3, 4}
print(a | b)   # union: {1, 2, 3, 4, 5, 6}
print(a - b)   # difference: {1, 2}
```
 
#### Checklist
- [ ] Write list, dict, and set comprehensions confidently
- [ ] Use `Counter`, `defaultdict`, and `deque` from `collections`
- [ ] Unpack tuples and use starred expressions
- [ ] Choose between list, tuple, set, and dict for a given use case
- [ ] Sort lists and dicts using `sorted()` with a `key` function
---
 
## 4. File Handling & I/O
 
> **Goal:** Read, write, and process files — a core skill for scripting, data pipelines, and automation.
> **Estimated Time:** 1–2 weeks
 
#### Core Topics
 
- Opening files with `open()` and context managers (`with`)
- Read modes: `r`, `w`, `a`, `rb`, `wb`
- Reading line-by-line vs all at once
- Writing and appending to files
- Working with CSV (`csv` module)
- Working with JSON (`json` module)
- Path handling with `pathlib`
```python
# Reading & writing with context manager
with open("data.txt", "r") as f:
    lines = f.readlines()
 
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")
 
# JSON
import json
 
data = {"name": "Alice", "scores": [95, 87, 92]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
 
with open("data.json", "r") as f:
    loaded = json.load(f)
 
# CSV
import csv
 
with open("report.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "score": 95})
 
# pathlib
from pathlib import Path
 
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
for log_file in log_dir.glob("*.log"):
    print(log_file.name)
```
 
#### Checklist
- [ ] Read and write text files using context managers
- [ ] Parse a CSV file into a list of dicts
- [ ] Serialize and deserialize JSON data
- [ ] Use `pathlib` to navigate directories and find files by extension
- [ ] Handle file-not-found and permission errors gracefully
---
 
## 5. Object-Oriented Programming
 
> **Goal:** Model real-world problems with classes and objects — the building block of larger Python applications.
> **Estimated Time:** 3–4 weeks
 
#### Core Topics
 
- Classes and instances
- `__init__`, `__str__`, `__repr__` and other dunder methods
- Instance, class, and static methods
- Inheritance and method overriding
- `super()` and cooperative multiple inheritance
- Encapsulation: private/protected attributes (convention)
- Properties (`@property`, getters/setters)
- Dataclasses (`@dataclass`)
- Abstract base classes (`abc` module)
```python
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
 
# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
 
    def describe(self):
        return f"I am a {type(self).__name__} with area {self.area():.2f}"
 
# Inheritance + dataclass
@dataclass
class Rectangle(Shape):
    width: float
    height: float
 
    def area(self) -> float:
        return self.width * self.height
 
@dataclass
class Circle(Shape):
    radius: float
 
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2
 
rect = Rectangle(4, 5)
circ = Circle(3)
print(rect.describe())   # I am a Rectangle with area 20.00
print(circ.describe())   # I am a Circle with area 28.27
 
# Property example
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius
 
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
 
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
```
 
#### Checklist
- [ ] Build a class hierarchy with at least two levels of inheritance
- [ ] Implement dunder methods (`__str__`, `__eq__`, `__len__`)
- [ ] Use `@property` for controlled attribute access
- [ ] Refactor a plain dict-based structure into a `@dataclass`
- [ ] Define and implement an abstract base class
---
 
## 6. Modules, Packages & Virtual Environments
 
> **Goal:** Structure code across multiple files, manage dependencies, and publish reusable packages.
> **Estimated Time:** 1–2 weeks
 
#### Core Topics
 
- Importing modules: `import`, `from ... import`, aliasing
- The `__name__ == "__main__"` guard
- Creating your own modules and packages (`__init__.py`)
- Virtual environments (`venv`, `pip`)
- `requirements.txt` and pinning dependencies
- Introduction to `pyproject.toml` / `setup.cfg`
- Useful standard library modules: `os`, `sys`, `datetime`, `math`, `random`, `itertools`
```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows
 
pip install requests pandas
pip freeze > requirements.txt
pip install -r requirements.txt
```
 
```python
# mypackage/__init__.py
from .utils import format_date
from .models import User
 
# mypackage/utils.py
from datetime import datetime
 
def format_date(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")
 
# main.py
if __name__ == "__main__":
    from mypackage.models import User
    u = User(name="Alice")
    print(u)
```
 
#### Checklist
- [ ] Create and activate a virtual environment for every project
- [ ] Structure a project into modules and a package directory
- [ ] Use `requirements.txt` to reproduce an environment
- [ ] Understand relative vs absolute imports
- [ ] Explore at least 5 standard library modules beyond the basics
---
 
## 7. Error Handling & Debugging
 
> **Goal:** Write robust code that handles failures gracefully and is easy to diagnose when things go wrong.
> **Estimated Time:** 1–2 weeks
 
#### Core Topics
 
- Exception hierarchy (`BaseException` → `Exception` → specific errors)
- `try`, `except`, `else`, `finally`
- Raising exceptions with `raise`
- Custom exception classes
- Context managers for resource cleanup
- Logging with the `logging` module (vs `print`)
- Debugging with `pdb` and IDE breakpoints
```python
import logging
 
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
 
# Custom exception
class ValidationError(ValueError):
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"[{field}] {message}")
 
def parse_age(value: str) -> int:
    try:
        age = int(value)
        if age < 0 or age > 150:
            raise ValidationError("age", "Must be between 0 and 150")
        return age
    except ValueError:
        raise ValidationError("age", f"'{value}' is not a valid integer")
    finally:
        logger.debug("parse_age called with: %s", value)
 
# Context manager using __enter__ / __exit__
class Timer:
    import time
    def __enter__(self):
        self.start = __import__("time").time()
        return self
    def __exit__(self, *args):
        self.elapsed = __import__("time").time() - self.start
        print(f"Elapsed: {self.elapsed:.3f}s")
 
with Timer():
    sum(range(10_000_000))
```
 
#### Checklist
- [ ] Catch specific exceptions rather than bare `except`
- [ ] Write at least one custom exception class
- [ ] Replace `print` debugging with structured `logging`
- [ ] Use `finally` to guarantee cleanup (close files, connections)
- [ ] Set a breakpoint with `pdb` and step through code
---
 
## 8. Iterators, Generators & Functional Tools
 
> **Goal:** Write memory-efficient, expressive Python using lazy evaluation and higher-order functions.
> **Estimated Time:** 2–3 weeks
 
#### Core Topics
 
- Iterators vs iterables (`__iter__`, `__next__`)
- Generator functions (`yield`) and generator expressions
- `itertools` module (`chain`, `islice`, `product`, `groupby`)
- `functools` module (`reduce`, `lru_cache`, `partial`, `wraps`)
- `map()`, `filter()`, and when to prefer comprehensions
- Decorators: writing, stacking, and preserving metadata
```python
from itertools import islice, groupby
from functools import lru_cache, wraps
import time
 
# Generator — infinite sequence, zero memory
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
 
first_10 = list(islice(fibonacci(), 10))
print(first_10)
 
# lru_cache for memoization
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
 
# Decorator that times any function
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper
 
@timed
def heavy_computation(n):
    return sum(i**2 for i in range(n))
 
# groupby example
data = [("EU", "Germany"), ("EU", "France"), ("US", "Texas"), ("US", "NY")]
for region, items in groupby(data, key=lambda x: x[0]):
    print(region, list(items))
```
 
#### Checklist
- [ ] Write a generator function that yields values lazily
- [ ] Use `itertools.chain`, `islice`, and `groupby` in a real task
- [ ] Write a reusable decorator using `@wraps`
- [ ] Speed up a recursive function with `@lru_cache`
- [ ] Explain the difference between a generator and a list comprehension
---
 
## 9. Regular Expressions
 
> **Goal:** Extract, validate, and transform text using pattern matching.
> **Estimated Time:** 1–2 weeks
 
#### Core Topics
 
- `re` module: `match`, `search`, `findall`, `sub`, `split`
- Character classes, quantifiers, anchors, groups
- Named capture groups
- Lookaheads and lookbehinds
- Compiling patterns with `re.compile` for performance
- Common patterns: emails, IPs, URLs, dates
```python
import re
 
# Named groups
log_line = "2024-03-15 14:32:01 ERROR Connection refused to 192.168.1.10"
pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>\w+) (?P<message>.+)"
)
m = pattern.match(log_line)
if m:
    print(m.group("level"))    # ERROR
    print(m.group("date"))     # 2024-03-15
 
# Extract all IPv4 addresses from a block of text
text = "Hosts: 10.0.0.1, 192.168.1.254, and 8.8.8.8"
ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
ips = ip_pattern.findall(text)
print(ips)  # ['10.0.0.1', '192.168.1.254', '8.8.8.8']
 
# Substitution with a function
def mask_email(m):
    user, domain = m.group(1), m.group(2)
    return f"{user[0]}***@{domain}"
 
redacted = re.sub(r"([\w.]+)@([\w.]+)", mask_email, "Contact alice@example.com")
print(redacted)  # Contact a***@example.com
```
 
#### Checklist
- [ ] Write a pattern that validates email addresses
- [ ] Extract structured fields from log lines using named groups
- [ ] Replace/redact sensitive data using `re.sub` with a callable
- [ ] Use lookahead/lookbehind for context-sensitive matching
- [ ] Compile and reuse patterns for performance-critical code
---
 
## 10. Working with APIs & HTTP
 
> **Goal:** Consume web APIs, handle authentication, and build simple HTTP servers.
> **Estimated Time:** 2–3 weeks
 
#### Core Topics
 
- HTTP fundamentals: methods, status codes, headers
- `requests` library: GET, POST, sessions, timeouts, retries
- JSON deserialization and error handling
- Authentication: API keys, Bearer tokens, OAuth2 basics
- Rate limiting and pagination patterns
- Building simple APIs with FastAPI
- Environment variables for secrets (`python-dotenv`)
```python
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
 
# Resilient session with retries
def make_session(retries=3, backoff=0.5) -> requests.Session:
    session = requests.Session()
    retry = Retry(total=retries, backoff_factor=backoff,
                  status_forcelist=[429, 500, 502, 503])
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session
 
API_KEY = os.environ["MY_API_KEY"]
session = make_session()
 
response = session.get(
    "https://api.example.com/users",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"page": 1, "per_page": 50},
    timeout=10,
)
response.raise_for_status()
users = response.json()
 
# FastAPI mini-example
from fastapi import FastAPI
app = FastAPI()
 
@app.get("/health")
def health():
    return {"status": "ok"}
 
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Alice"}
```
 
#### Checklist
- [ ] Fetch paginated data from a public API and save it to JSON
- [ ] Handle common HTTP errors (4xx, 5xx) without crashing
- [ ] Use Bearer token auth and store the token in an env var
- [ ] Build a 3-route FastAPI app with request body validation
- [ ] Write a retry-with-backoff wrapper for flaky endpoints
---
 
## 11. Databases
 
> **Goal:** Persist and query data using both relational and document-based databases.
> **Estimated Time:** 2–3 weeks
 
#### Core Topics
 
- SQLite basics via the built-in `sqlite3` module
- SQL fundamentals: SELECT, INSERT, UPDATE, DELETE, JOIN
- ORM with SQLAlchemy (Core and ORM)
- Alembic for schema migrations
- Redis for caching and pub/sub (`redis-py`)
- MongoDB with `pymongo`
- Connection pooling and transaction management
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship
 
engine = create_engine("sqlite:///app.db", echo=True)
 
class Base(DeclarativeBase):
    pass
 
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    posts = relationship("Post", back_populates="author")
 
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
 
Base.metadata.create_all(engine)
 
with Session(engine) as session:
    alice = User(name="Alice")
    alice.posts.append(Post(title="My First Post"))
    session.add(alice)
    session.commit()
 
    users = session.query(User).filter(User.name.like("A%")).all()
```
 
#### Checklist
- [ ] Write raw SQL using `sqlite3` with parameterized queries
- [ ] Define SQLAlchemy models with a one-to-many relationship
- [ ] Write and run an Alembic migration
- [ ] Cache an API response in Redis with a TTL
- [ ] Use a context manager (`with Session`) to ensure transaction safety
---
 
## 12. Testing
 
> **Goal:** Write automated tests that give you confidence your code works — and stays working.
> **Estimated Time:** 2–3 weeks
 
#### Core Topics
 
- `pytest` fundamentals: test discovery, assertions, fixtures
- Parametrize tests with `@pytest.mark.parametrize`
- Mocking with `unittest.mock` (`MagicMock`, `patch`)
- Testing HTTP calls with `responses` or `httpretty`
- Code coverage with `pytest-cov`
- Test types: unit, integration, end-to-end
- Test-driven development (TDD) workflow
```python
# app/calculator.py
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
 
# tests/test_calculator.py
import pytest
from app.calculator import divide
 
def test_divide_normal():
    assert divide(10, 2) == 5.0
 
@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2.0),
    (0, 5, 0.0),
    (-9, 3, -3.0),
])
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected
 
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
 
# Fixture example
@pytest.fixture
def sample_user():
    return {"id": 1, "name": "Alice", "active": True}
 
def test_user_is_active(sample_user):
    assert sample_user["active"] is True
```
 
```bash
pytest tests/ -v --cov=app --cov-report=term-missing
```
 
#### Checklist
- [ ] Write unit tests for every public function in a module
- [ ] Use `@pytest.mark.parametrize` to cover edge cases efficiently
- [ ] Mock an external API call using `unittest.mock.patch`
- [ ] Achieve >80% code coverage on a small project
- [ ] Practice the red-green-refactor TDD cycle on a new feature
---
 
## 13. Concurrency & Parallelism
 
> **Goal:** Write code that handles I/O-bound and CPU-bound tasks efficiently.
> **Estimated Time:** 2–4 weeks
 
#### Core Topics
 
- The GIL and what it means for Python threading
- `threading` module for I/O-bound tasks
- `multiprocessing` for CPU-bound tasks
- `asyncio` — event loop, `async def`, `await`, `gather`
- `httpx` and `aiohttp` for async HTTP
- `concurrent.futures` — `ThreadPoolExecutor`, `ProcessPoolExecutor`
- When to use threads vs processes vs async
```python
import asyncio
import httpx
from concurrent.futures import ThreadPoolExecutor, as_completed
 
# Async HTTP — fetch many URLs concurrently
async def fetch(client: httpx.AsyncClient, url: str) -> dict:
    resp = await client.get(url, timeout=10)
    return {"url": url, "status": resp.status_code}
 
async def fetch_all(urls: list[str]):
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in urls]
        return await asyncio.gather(*tasks)
 
results = asyncio.run(fetch_all([
    "https://httpbin.org/get",
    "https://httpbin.org/status/200",
]))
print(results)
 
# CPU-bound with ProcessPoolExecutor
from multiprocessing import cpu_count
 
def compute(n: int) -> int:
    return sum(i**2 for i in range(n))
 
with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
    futures = [executor.submit(compute, 10_000_000) for _ in range(4)]
    for f in as_completed(futures):
        print(f.result())
```
 
#### Checklist
- [ ] Explain the GIL and its practical impact
- [ ] Rewrite a serial HTTP fetch loop using `asyncio` + `httpx`
- [ ] Use `ProcessPoolExecutor` to parallelize a CPU-bound task
- [ ] Handle exceptions inside `asyncio.gather` without crashing
- [ ] Measure and compare runtime: serial vs threaded vs async
---
 
## 14. Data Science & Analysis
 
> **Goal:** Analyze, transform, and visualize data using Python's data science stack.
> **Estimated Time:** 4–6 weeks
 
#### Core Topics
 
- **NumPy:** arrays, vectorized operations, broadcasting
- **Pandas:** Series, DataFrame, indexing, groupby, merge, pivot
- **Matplotlib / Seaborn:** line, bar, scatter, heatmaps
- **Jupyter Notebooks** for exploratory analysis
- Data cleaning: missing values, type casting, outliers
- Intro to **scikit-learn:** preprocessing, train/test split, simple models (linear regression, decision trees)
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
 
# NumPy vectorized operations
arr = np.array([1, 2, 3, 4, 5])
print(arr ** 2)          # [1 4 9 16 25]
print(arr.mean())        # 3.0
 
# Pandas — load, clean, group
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
df.dropna(subset=["revenue"], inplace=True)
monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
 
# Plot
monthly.plot(kind="bar", title="Monthly Revenue")
plt.tight_layout()
plt.savefig("revenue.png")
 
# scikit-learn
X = df[["ad_spend", "employees"]].values
y = df["revenue"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
 
model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
print(f"RMSE: {mean_squared_error(y_test, preds, squared=False):.2f}")
```
 
#### Checklist
- [ ] Reshape and operate on NumPy arrays without loops
- [ ] Clean a messy CSV (nulls, wrong dtypes, duplicates) with Pandas
- [ ] Produce a grouped summary and plot the result
- [ ] Train and evaluate a scikit-learn regression or classification model
- [ ] Share analysis in a well-documented Jupyter Notebook
---
 
## 15. Web Development
 
> **Goal:** Build production-grade web applications and APIs with Python.
> **Estimated Time:** 4–6 weeks
 
#### Core Topics
 
- **FastAPI** (async, type-safe, OpenAPI auto-docs) — preferred for APIs
- **Django** (batteries-included, ORM, admin, auth) — preferred for full apps
- Request/response lifecycle, middleware, CORS
- Pydantic models for data validation
- Background tasks and WebSockets
- Authentication: JWT, session-based
- Deployment: Gunicorn + Uvicorn, Docker, environment config
```python
# FastAPI — typed REST API with Pydantic
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import Optional
 
app = FastAPI(title="User API", version="1.0.0")
 
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
 
class UserResponse(UserCreate):
    id: int
    class Config:
        from_attributes = True
 
fake_db: dict[int, dict] = {}
counter = 0
 
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global counter
    counter += 1
    fake_db[counter] = {"id": counter, **user.model_dump()}
    return fake_db[counter]
 
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db[user_id]
```
 
```bash
uvicorn main:app --reload
# Docs auto-generated at http://localhost:8000/docs
```
 
#### Checklist
- [ ] Build a CRUD API with FastAPI and Pydantic validation
- [ ] Add JWT authentication to protect endpoints
- [ ] Connect FastAPI to a PostgreSQL database via SQLAlchemy
- [ ] Write a Django app with a model, view, URL, and admin registration
- [ ] Containerize and run the app with Docker
---
 
## 16. Automation & Scripting
 
> **Goal:** Automate repetitive tasks — file ops, browser control, emails, scheduling, and CLI tools.
> **Estimated Time:** 2–3 weeks
 
#### Core Topics
 
- CLI tools with `argparse` and `typer`
- File system automation with `pathlib`, `shutil`, `watchdog`
- Browser automation with `playwright` / `selenium`
- Email with `smtplib` + `email` or `yagmail`
- Scheduling with `schedule` or system cron
- PDF/Excel/image manipulation (`pypdf`, `openpyxl`, `Pillow`)
- Web scraping with `BeautifulSoup` + `requests`
```python
# CLI tool with typer
import typer
from pathlib import Path
 
app = typer.Typer()
 
@app.command()
def rename_files(
    directory: Path = typer.Argument(..., help="Target directory"),
    prefix: str = typer.Option("", help="Prefix to add to filenames"),
    dry_run: bool = typer.Option(False, help="Preview without making changes"),
):
    for f in directory.iterdir():
        if f.is_file():
            new_name = f.parent / f"{prefix}{f.name}"
            typer.echo(f"{f.name} → {new_name.name}")
            if not dry_run:
                f.rename(new_name)
 
if __name__ == "__main__":
    app()
```
 
```python
# Web scraping
from bs4 import BeautifulSoup
import requests
 
resp = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(resp.text, "html.parser")
titles = [a.text for a in soup.select(".titleline > a")]
print("\n".join(titles[:10]))
```
 
#### Checklist
- [ ] Build a CLI tool with `typer` that has flags, options, and help text
- [ ] Automate a file management task using `pathlib` + `shutil`
- [ ] Scrape a website and save results to CSV
- [ ] Send a formatted email via `smtplib`
- [ ] Schedule a script to run daily using `schedule` or cron
---
 
## 17. Advanced Python Internals
 
> **Goal:** Understand how Python actually works under the hood and write expert-level code.
> **Estimated Time:** 4–6 weeks (ongoing)
 
#### Core Topics
 
- Memory management: reference counting, garbage collection, `__slots__`
- The descriptor protocol (`__get__`, `__set__`, `__delete__`)
- Metaclasses (`type`, `__init_subclass__`)
- Context managers via `contextlib` (`@contextmanager`, `suppress`)
- Protocol typing and structural subtyping (`typing.Protocol`)
- `typing` module: generics, `TypeVar`, `Literal`, `overload`
- CPython bytecode (`dis` module)
- C extensions and `ctypes` / `cffi` basics
- Performance profiling (`cProfile`, `line_profiler`, `memory_profiler`)
```python
from typing import Protocol, TypeVar, Generic
from contextlib import contextmanager
import cProfile
 
# Protocol — structural typing
class Drawable(Protocol):
    def draw(self) -> str: ...
 
class Circle:
    def draw(self) -> str:
        return "○"
 
def render(shape: Drawable) -> None:
    print(shape.draw())
 
render(Circle())   # works without inheriting from Drawable
 
# __slots__ for memory efficiency
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
 
# Context manager via generator
@contextmanager
def managed_resource(name: str):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")
 
with managed_resource("database connection") as res:
    print(f"Using {res}")
 
# Profile a function
cProfile.run("sum(i**2 for i in range(1_000_000))", sort="cumulative")
```
 
```python
import dis
def add(a, b):
    return a + b
 
dis.dis(add)  # inspect CPython bytecode
```
 
#### Checklist
- [ ] Use `__slots__` and measure the memory savings vs a regular class
- [ ] Write a descriptor class that validates attribute assignments
- [ ] Define a `typing.Protocol` and use it for duck-typed interfaces
- [ ] Profile a slow function with `cProfile` and optimize the bottleneck
- [ ] Inspect bytecode with `dis` and explain what a simple function compiles to
---
 
## Certifications Along the Journey
 
| Stage | Certification | Focus |
|-------|---------------|-------|
| **Beginner** | PCEP — Certified Entry-Level Python Programmer | Python syntax & basics |
| **Beginner–Intermediate** | PCAP — Certified Associate in Python Programming | OOP, modules, exceptions |
| **Intermediate** | PCPP1 — Certified Professional Python Programmer 1 | Advanced OOP, decorators |
| **Intermediate** | PCPP2 — Certified Professional Python Programmer 2 | Networking, databases, testing |
| **Intermediate** | AWS Certified Developer – Associate | Python on AWS (Lambda, Boto3) |
| **Advanced** | Google Professional Data Engineer | Data pipelines, ML in GCP |
| **Advanced** | Databricks Certified Associate Developer for Apache Spark | PySpark & big data |
| **Advanced** | MongoDB Python Developer Path | NoSQL with PyMongo |
 
---
 
## 🧪 Real-World Projects
 
| Level | Project | Skills Practiced |
|-------|---------|------------------|
| Beginner | Number guessing game (CLI) | Control flow, functions, I/O |
| Beginner | Expense tracker with CSV storage | File I/O, dicts, loops |
| Beginner | Weather CLI app using OpenWeatherMap API | HTTP requests, JSON, argparse |
| Intermediate | URL shortener with SQLite + Flask/FastAPI | Web dev, databases, REST |
| Intermediate | Log parser & alerting script | Regex, file I/O, email automation |
| Intermediate | Stock price dashboard with Pandas + Matplotlib | Data analysis, APIs, visualization |
| Intermediate | Automated test suite for an existing codebase | pytest, mocking, coverage |
| Advanced | Async web scraper that crawls 1000+ pages | asyncio, httpx, rate limiting |
| Advanced | REST API with FastAPI, PostgreSQL, JWT auth | Full-stack API, Docker |
| Advanced | ML pipeline: data → model → FastAPI endpoint | scikit-learn, pandas, deployment |
| Expert | CLI DevOps tool with plugin architecture | Metaclasses, descriptors, packaging |
| Expert | Build your own mini web framework | WSGI, routing, decorators, internals |
 
---
 
## 📚 Learning Resources
 
### Official Documentation & References
- [Python Docs](https://docs.python.org/3/) — always the primary source
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Real Python](https://realpython.com) — in-depth tutorials for every level
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org)
- [pytest Docs](https://docs.pytest.org)
### Practice Platforms
- **Exercism.io** — mentor-reviewed Python exercises
- **LeetCode / HackerRank** — algorithm & data structure practice
- **Advent of Code** — annual puzzle series, great for intermediate skills
- **Kaggle** — datasets and notebooks for data science practice
### Books
| Title | Author | Level |
|-------|--------|-------|
| *Automate the Boring Stuff with Python* | Al Sweigart | Beginner |
| *Python Crash Course* | Eric Matthes | Beginner |
| *Fluent Python* | Luciano Ramalho | Intermediate–Advanced |
| *Python Cookbook* | David Beazley & Brian K. Jones | Intermediate–Advanced |
| *Architecture Patterns with Python* | Harry Percival & Bob Gregory | Advanced |
| *High Performance Python* | Micha Gorelick & Ian Ozsvald | Advanced |
 
### YouTube Channels
- **Corey Schafer** — comprehensive Python tutorials
- **ArjanCodes** — design patterns, clean code, advanced Python
- **mCoding** — Python internals and performance deep-dives
---
 
## 🗺️ Complete Learning Path Summary
 
```
Week 1–6    ─── Foundations ──────────────────────────────────────────
                Python Basics → Control Flow & Functions
                → Data Structures
 
Week 6–12   ─── Core Skills ───────────────────────────────────────────
                File Handling & I/O → OOP
                → Modules, Packages & Virtual Environments
 
Week 12–18  ─── Robustness & Expressiveness ─────────────────────────
                Error Handling & Debugging
                → Iterators, Generators & Functional Tools
                → Regular Expressions
 
Week 18–26  ─── External World ─────────────────────────────────────────
                APIs & HTTP → Databases → Testing
 
Week 26–32  ─── Scale & Specialization ──────────────────────────────
                Concurrency & Parallelism
                → Data Science & Analysis  (or)
                → Web Development          (or)
                → Automation & Scripting
 
Ongoing     ─── Mastery ──────────────────────────────────────────────
                Advanced Python Internals → Open Source Contributions
                → Build & publish your own package on PyPI
```
 
---
 
*Last updated: 2026 · Roadmap structured for a progressive, project-driven Python learning journey*
 

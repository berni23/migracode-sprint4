"""
Open Exercise — Event Schedule Builder

You're building a tool for a community center that manages weekly events.
Below you have raw JSON data about events and participants.

Your job: write functions to answer each question. There's no single
"right" answer — solve it however you like, but try to use dictionaries,
JSON, and list comprehensions where they make sense.

Run this file with:  python exercise.py
"""

import json

# ── Raw data ──────────────────────────────────────────────────────────

events_json = """
[
  {
    "id": "evt-1",
    "name": "Yoga Class",
    "day": "Monday",
    "time": "09:00",
    "capacity": 15,
    "category": "wellness",
    "participants": ["Alice", "Bob", "Cat", "Dan"]
  },
  {
    "id": "evt-2",
    "name": "Python Workshop",
    "day": "Monday",
    "time": "18:00",
    "capacity": 20,
    "category": "tech",
    "participants": ["Alice", "Eve", "Fay", "George", "Hanna"]
  },
  {
    "id": "evt-3",
    "name": "Book Club",
    "day": "Wednesday",
    "time": "17:00",
    "capacity": 10,
    "category": "culture",
    "participants": ["Bob", "Cat", "Ivan"]
  },
  {
    "id": "evt-4",
    "name": "Running Group",
    "day": "Wednesday",
    "time": "07:00",
    "capacity": 25,
    "category": "wellness",
    "participants": ["Dan", "Eve", "Fay", "Alice", "Jack", "Karen"]
  },
  {
    "id": "evt-5",
    "name": "JavaScript Study Group",
    "day": "Thursday",
    "time": "18:00",
    "capacity": 20,
    "category": "tech",
    "participants": ["George", "Hanna", "Alice", "Bob"]
  },
  {
    "id": "evt-6",
    "name": "Painting Night",
    "day": "Friday",
    "time": "19:00",
    "capacity": 12,
    "category": "culture",
    "participants": ["Cat", "Fay", "Ivan", "Karen", "Alice"]
  }
]
"""

events = json.loads(events_json)


# ── Tasks ─────────────────────────────────────────────────────────────

# 1. Write a function that receives a day (e.g. "Monday") and returns
#    the names of all events happening on that day.

def events_on_day(day):


    pass


# 2. Write a function that finds the event with the most available
#    spots (capacity - number of participants) and returns its name.

def most_available_event():
    pass


# 3. Write a function that receives a person's name and returns a list
#    of all event names they are signed up for.

def events_for_person(name):
    pass


# 4. Write a function that builds a summary dictionary:
#    {
#      "total_events": ...,
#      "total_unique_participants": ...,
#      "events_by_category": {"wellness": [...], "tech": [...], "culture": [...]},
#      "busiest_day": "..."   ← the day with the most events
#    }

def schedule_summary():
    pass


# 5. Write a function that returns a NEW list of events sorted by the
#    number of participants (most popular first). Do not modify the
#    original list.

def events_by_popularity():
    pass


# 6. Write a function that detects scheduling conflicts: people who are
#    signed up for two events on the same day. Return a dict like:
#    {"Alice": ["Monday"], "Bob": ["Monday"], ...}
#    (only include people who actually have conflicts)

def find_conflicts():
    pass


# ── Main ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Uncomment these as you implement each function:

    # print("Events on Monday:", events_on_day("Monday"))
    # print("Most available:", most_available_event())
    # print("Alice's events:", events_for_person("Alice"))
    # print("Summary:", json.dumps(schedule_summary(), indent=2))
    # print("By popularity:", [e["name"] for e in events_by_popularity()])
    # print("Conflicts:", find_conflicts())

    pass

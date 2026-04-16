"""
Bonus Exercise — Company Workforce Analyzer

You work at a growing company and HR has handed you a messy dataset of employees.
Your job: clean it up, analyze it, and produce three output files with your findings.

This exercise combines everything from the course: strings, lists, loops,
dictionaries, JSON, functions, and file I/O.

Run this file with:  python3 bonus_exercise.py
"""

import json

# ── Raw data ────────────────────────────────────────────────────────────
# Notes from HR:
#   - Some employees are missing a "department" (it's None)
#   - Salary is a string with a "$" and commas — you'll need to parse it
#   - "start_date" is a string in "YYYY-MM-DD" format
#   - "projects" may be an empty list or missing entirely for some employees

employees_json = """
[
  {"id": "E001", "name": "Alice Johnson",   "department": "Engineering", "salary": "$92,500",  "start_date": "2019-03-15", "projects": ["Atlas", "Beacon"]},
  {"id": "E002", "name": "Bob Martinez",    "department": "Engineering", "salary": "$88,000",  "start_date": "2020-07-01", "projects": ["Atlas"]},
  {"id": "E003", "name": "Carol Smith",     "department": "Marketing",   "salary": "$67,000",  "start_date": "2021-01-20", "projects": ["Cascade", "Dune", "Echo"]},
  {"id": "E004", "name": "Dan Lee",         "department": null,          "salary": "$73,500",  "start_date": "2020-11-10", "projects": ["Beacon"]},
  {"id": "E005", "name": "Eva Chen",        "department": "Engineering", "salary": "$105,200", "start_date": "2018-06-01", "projects": ["Atlas", "Beacon", "Cascade", "Dune"]},
  {"id": "E006", "name": "Frank Osei",      "department": "Marketing",   "salary": "$62,000",  "start_date": "2022-04-18", "projects": []},
  {"id": "E007", "name": "Grace Kim",       "department": "Sales",       "salary": "$71,000",  "start_date": "2021-09-05", "projects": ["Echo"]},
  {"id": "E008", "name": "Hiro Tanaka",     "department": null,          "salary": "$80,000",  "start_date": "2019-12-01", "projects": ["Dune", "Beacon"]},
  {"id": "E009", "name": "Isla Fernandez",  "department": "Sales",       "salary": "$69,500",  "start_date": "2023-02-14"},
  {"id": "E010", "name": "Jake Novak",      "department": "Engineering", "salary": "$97,800",  "start_date": "2020-01-10", "projects": ["Atlas", "Cascade"]},
  {"id": "E011", "name": "Karen Watts",     "department": "Marketing",   "salary": "$58,000",  "start_date": "2023-08-21", "projects": ["Echo"]},
  {"id": "E012", "name": "Leo Santos",      "department": "Sales",       "salary": "$74,200",  "start_date": "2019-05-30", "projects": ["Beacon", "Dune", "Echo"]},
  {"id": "E013", "name": "Mina Patel",      "department": "Engineering", "salary": "$112,000", "start_date": "2017-09-12", "projects": ["Atlas", "Beacon", "Cascade", "Dune", "Echo"]},
  {"id": "E014", "name": "Nora Berg",       "department": null,          "salary": "$66,400",  "start_date": "2022-06-01", "projects": ["Cascade"]},
  {"id": "E015", "name": "Oscar Ruiz",      "department": "Sales",       "salary": "$70,000",  "start_date": "2021-03-25", "projects": ["Echo", "Dune"]}
]
"""

employees = json.loads(employees_json)


# ── Helper ──────────────────────────────────────────────────────────────
# Hint: you'll need to convert salary strings like "$92,500" into numbers.
# Write a helper function here that you can reuse throughout.

def parse_salary(salary_str):
    """Convert a salary string like '$92,500' into a float. Returns 92500.0"""
    pass


# ── Part 1: Clean the data ─────────────────────────────────────────────
# Write a function that returns a NEW cleaned list of employee dicts where:
#   - "salary" is a float (not a string)
#   - "department" is "Unassigned" if it was None/null
#   - "projects" is an empty list [] if the key was missing
# Do NOT modify the original list.

def clean_employees(raw_employees):
    pass


# ── Part 2: Department report ──────────────────────────────────────────
# Write a function that takes the cleaned list and returns a dictionary:
# {
#   "Engineering": {"count": ..., "avg_salary": ..., "employees": [...]},
#   "Marketing":   {"count": ..., "avg_salary": ..., "employees": [...]},
#   ...
# }
# - "avg_salary" should be rounded to 2 decimal places
# - "employees" is a list of names sorted alphabetically

def department_report(cleaned):
    pass


# ── Part 3: Project analysis ───────────────────────────────────────────
# Write a function that takes the cleaned list and returns a dictionary:
# {
#   "Atlas":   {"team_size": ..., "members": [...], "total_salary_cost": ...},
#   "Beacon":  {"team_size": ..., "members": [...], "total_salary_cost": ...},
#   ...
# }
# - "members" is a list of employee names sorted alphabetically
# - "total_salary_cost" is the sum of salaries of everyone on that project

def project_analysis(cleaned):
    pass


# ── Part 4: Find overloaded employees ──────────────────────────────────
# Write a function that returns a list of dicts for employees on 3+ projects:
# [{"name": "...", "project_count": ..., "projects": [...]}, ...]
# Sorted by project_count descending, then by name ascending.

def find_overloaded(cleaned):
    pass


# ── Part 5: Salary ranking CSV ─────────────────────────────────────────
# Write a function that takes the cleaned list and writes a CSV file
# called "salary_ranking.csv" with columns: Rank, Name, Department, Salary
# Sorted by salary descending. Rank starts at 1.
#
# Expected output (salary_ranking.csv):
#   Rank,Name,Department,Salary
#   1,Mina Patel,Engineering,112000.0
#   2,Eva Chen,Engineering,105200.0
#   ...

def write_salary_ranking(cleaned, filename="salary_ranking.csv"):
    pass


# ── Part 6: Write the full report ──────────────────────────────────────
# Write a function that generates TWO files:
#
# 1. "report.txt" — a human-readable summary with:
#    - Total number of employees
#    - Number of departments
#    - Company-wide average salary
#    - The department report (formatted nicely)
#    - List of overloaded employees
#
# 2. "report.json" — a JSON file containing:
#    {"department_report": {...}, "project_analysis": {...}, "overloaded": [...]}
#
# Use the functions you wrote above!

def write_full_report(cleaned):
    pass


# ── Main ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Step 1: Clean
    cleaned = clean_employees(employees)

    # Step 2: Analyze (uncomment as you go)
    # dept = department_report(cleaned)
    # print("Department report:", json.dumps(dept, indent=2))

    # projects = project_analysis(cleaned)
    # print("Project analysis:", json.dumps(projects, indent=2))

    # overloaded = find_overloaded(cleaned)
    # print("Overloaded employees:", overloaded)

    # Step 3: Write output files
    # write_salary_ranking(cleaned)
    # print("Written: salary_ranking.csv")

    # write_full_report(cleaned)
    # print("Written: report.txt and report.json")

    pass

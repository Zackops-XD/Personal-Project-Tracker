import sqlite3

from database import get_projects, update_project, get_project, delete_project

delete_project(5)

print(get_projects())
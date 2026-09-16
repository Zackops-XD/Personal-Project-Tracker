import sqlite3


def create_database():
    connection = sqlite3.connect("tracker.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            deadline TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_project(name, description, status, priority, deadline):
    connection = sqlite3.connect("tracker.db")

    connection.execute("""
        INSERT INTO projects (name, description, status, priority, deadline)
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        description,
        status,
        priority,
        deadline
    ))

    connection.commit()
    connection.close()

def get_projects():
    connection = sqlite3.connect("tracker.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM projects")

    projects = cursor.fetchall()

    connection.close()

    return projects

def update_project(project_id, name, description, status, priority, deadline):
    connection = sqlite3.connect("tracker.db")

    connection.execute("""
        UPDATE projects
        SET name = ?, description = ?, status = ?, priority = ?, deadline = ?
        WHERE ID = ?
    """, (
        name,
        description,
        status,
        priority,
        deadline,
        project_id
    ))

    connection.commit()
    connection.close()

def get_project(project_id):
    connection = sqlite3.connect("tracker.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM projects where id = ?", 
        (project_id,)
    )

    project = cursor.fetchone()

    connection.close()

    return project

def delete_project(project_id):
    connection = sqlite3.connect("tracker.db")

    connection.execute("""
        DELETE FROM projects 
        WHERE id = ?
    """,(
        project_id,
    ))

    connection.commit()
    connection.close()


create_database()
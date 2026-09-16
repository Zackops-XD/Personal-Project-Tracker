from flask import Flask, render_template, url_for, request, redirect
from database import get_projects, add_project, get_project, update_project, delete_project
from datetime import date

app = Flask(__name__)

@app.route("/")
def dashboard():
    projects = get_projects()
    filter_type = request.args.get("filter", "none")

    today = date.today()

    current_projects = []

    for project in projects:
        deadline = project[5]

        if deadline:
            deadline_date_raw = date.fromisoformat(deadline)
            days_remaining = (deadline_date_raw - today).days
            deadline_date = deadline_date_raw.strftime("%B %d, %Y")
            
            if days_remaining < 0:
                urgency = "overdue"
            elif days_remaining <= 3:
                urgency = "urgent"
            elif days_remaining <= 7:
                urgency = "approaching"
            else:
                urgency = "safe"
        else:
            days_remaining = None
            urgency = "no-deadline"
            deadline_date = None

        current_projects.append({
            "project": project,
            "days_remaining": days_remaining,
            "urgency": urgency,
            "deadline_date": deadline_date
        })

    urgency_order = {
        "overdue": 0,
        "urgent": 1,
        "approaching": 2,
        "safe": 3,
        "no-deadline": 4
    }
    priority_order = {
        "high": 0,
        "medium": 1,
        "low": 2
    }
    print("FILTER:", filter_type)
    if filter_type == "priority":
        current_projects.sort(
            key=lambda item: priority_order[item["project"][4].lower()]
        )
    elif filter_type == "urgent":
        current_projects.sort(
            key=lambda item: urgency_order[item["urgency"]]
        )

    current_projects = current_projects[:3]

    return render_template(
        "dashboard.html", 
        current_projects=current_projects,
        filter_type=filter_type
    )

@app.route("/projects")
def projects():
    projects = get_projects()

    return render_template("projects.html", projects=projects)

@app.route("/projects/add", methods=["GET", "POST"])
def add_project_page():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        status = request.form["status"]
        priority = request.form["priority"]
        deadline = request.form["deadline"]

        add_project(name, description, status, priority, deadline)

        return redirect(url_for("projects"))

    return render_template("add_project.html")

@app.route("/projects/edit/<int:project_id>", methods=["GET", "POST"])
def edit_project_page(project_id):
    project = get_project(project_id)

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        status = request.form["status"]
        priority = request.form["priority"]
        deadline = request.form["deadline"]

        update_project(
            project_id,
            name,
            description,
            status,
            priority,
            deadline
        )

        return redirect(url_for("projects"))

    return render_template("edit_project.html", project=project)
    
@app.route("/projects/delete/<int:project_id>", methods=["POST"])
def delete_project_page(project_id):
    delete_project(project_id)

    return redirect(url_for("projects"))

@app.route("/projects/<int:project_id>")
def project_details(project_id):
    project = get_project(project_id)

    return render_template(
        "project_details.html",
        project=project
    )

if __name__ == "__main__":
    app.run(debug=True)
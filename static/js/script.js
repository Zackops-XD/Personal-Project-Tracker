const deleteForms = document.querySelectorAll(".delete-form");

for (const form of deleteForms) {

    form.addEventListener("submit", function(event) {

        const confirmed = confirm(
            "Are you sure you want to delete this project?"
        );

        if (!confirmed) {
            event.preventDefault();
        }

    });

}

const searchInput = document.querySelector("#project-search");

const statusFilter = document.querySelector("#status-filter");

const priorityFilter = document.querySelector("#priority-filter");

const projectRows = document.querySelectorAll(
    ".projects-table tbody tr"
);

const noProjectsMessage = document.querySelector(
    "#no-projects-message"
);

const tableBody = document.querySelector(".projects-table tbody");

function updateProjects() {
    const searchText = searchInput.value;
    const selectedStatus = statusFilter.value;
    const selectedPriority = priorityFilter.value;

    const projectMatches = [];

    let hasMatches = false;

    for (const row of projectRows) {

        const projectNameElement = row.querySelector(
            ".project-name-link"
        );

        const projectName = projectNameElement.textContent.trim();

        const isStartsWith = projectName
            .toLowerCase()
            .startsWith(searchText.toLowerCase());

        const isContains = projectName
            .toLowerCase()
            .includes(searchText.toLowerCase());

        const projectStatus = row.cells[1].textContent.trim();

        // Status
        const isStatusMatch =
            selectedStatus === "all" ||
            projectStatus === selectedStatus;

        // Priority
        const projectPriority = row.cells[2].textContent.trim();

        const isPriorityMatch =
        selectedPriority === "all" ||
        projectPriority === selectedPriority;

        if (isStartsWith && isStatusMatch && isPriorityMatch) {
            hasMatches = true;
            row.style.display = "";
            projectMatches.push(row);

        } else if (isContains && isStatusMatch && isPriorityMatch) {
            hasMatches = true;
            row.style.display = "";
            projectMatches.push(row);

        } else {
            row.style.display = "none";

        }

    }
    
    projectMatches.sort(function(a, b) {

        const deadlineA = a.cells[3].textContent.trim();
        const deadlineB = b.cells[3].textContent.trim();

        const dateA = new Date(deadlineA);
        const dateB = new Date(deadlineB);

        return dateA - dateB;
    });
            
    for (const row of projectMatches) {
        tableBody.appendChild(row);
    }

    if (hasMatches) {
    noProjectsMessage.style.display = "none";
    } else {
        noProjectsMessage.style.display = "";
    }

}

searchInput.addEventListener("input", function() {
    updateProjects();
});

statusFilter.addEventListener("change", function() {
    updateProjects();
});

priorityFilter.addEventListener("change", function() {
    updateProjects();
})

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

const projectRows = document.querySelectorAll(
    ".projects-table tbody tr"
);

const tableBody = document.querySelector(".projects-table tbody");

searchInput.addEventListener("input", function() {

    const searchText = searchInput.value;

    const startsWithMatches = [];
    const containsMatches = [];

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

        if (isStartsWith) {

            row.style.display = "";
            startsWithMatches.push(row);

        } else if (isContains) {

            row.style.display = "";
            containsMatches.push(row);

        } else {

            row.style.display = "none";

        }

    }

    for (const row of startsWithMatches) {
        tableBody.appendChild(row);
    }

    for (const row of containsMatches) {
        tableBody.appendChild(row);
    }

});

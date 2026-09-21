console.log("JavaScript loaded!");

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
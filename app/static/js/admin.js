document.addEventListener("DOMContentLoaded", function () {
    let tabs = document.querySelectorAll(".nav-link");
    let contents = document.querySelectorAll("main > div");

    tabs.forEach(tab => {
        tab.addEventListener("click", function (e) {
            e.preventDefault();

            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove("active"));

            // Hide all content sections
            contents.forEach(content => content.classList.add("d-none"));

            // Activate clicked tab
            tab.classList.add("active");

            // Show corresponding content
            let targetId = "content-" + tab.id.replace("tab-", "");
            document.getElementById(targetId).classList.remove("d-none");
        });
    });
});

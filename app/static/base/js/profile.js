console.log("✅ Profile.js has been loaded!");

// Check if tabs exist
const tabs = document.querySelectorAll(".profile-tabs .nav-link");
console.log(`🔍 Found ${tabs.length} tabs.`);

// Check if sections exist
const sections = document.querySelectorAll(".profile-section");
console.log(`🔍 Found ${sections.length} sections.`);

tabs.forEach(tab => {
    tab.addEventListener("click", function (event) {
        event.preventDefault();
        console.log(`🟢 Clicked tab: ${this.id}`);

        // Remove active class from all tabs
        tabs.forEach(t => t.classList.remove("active"));
        this.classList.add("active");

        // Hide all sections
        sections.forEach(section => section.classList.add("d-none"));

        // Show the clicked section
        const selectedTab = this.id.replace("tab-", "content-");
        const activeSection = document.getElementById(selectedTab);

        if (activeSection) {
            console.log(`✅ Showing section: ${selectedTab}`);
            activeSection.classList.remove("d-none");
        } else {
            console.error(`❌ Section not found: ${selectedTab}`);
        }
    });
});

//personal info 
document.addEventListener("DOMContentLoaded", function () {
    // Profile Picture Preview
    document.getElementById("profile-picture").addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                document.getElementById("profile-preview").src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    // Save Personal Information
    document.getElementById("personal-info-form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent page reload

        // Collect Data
        const fullName = document.getElementById("full-name").value.trim();
        const email = document.getElementById("email").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const address = document.getElementById("address").value.trim();
        const dob = document.getElementById("dob").value;

        if (!fullName || !email || !phone || !address || !dob) {
            document.getElementById("personal-info-message").textContent = "⚠️ Please fill in all fields.";
            document.getElementById("personal-info-message").classList.add("text-warning");
            return;
        }

        // Simulate API Request (Replace with actual API call)
        setTimeout(() => {
            document.getElementById("personal-info-message").textContent = "✅ Profile updated successfully!";
            document.getElementById("personal-info-message").classList.add("text-success");
        }, 1000);
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Change Password Form
    document.getElementById("change-password-form").addEventListener("submit", function(event) {
        event.preventDefault();
        
        let currentPassword = document.getElementById("current-password").value;
        let newPassword = document.getElementById("new-password").value;
        let confirmPassword = document.getElementById("confirm-password").value;
        let message = document.getElementById("password-message");

        if (newPassword !== confirmPassword) {
            message.textContent = "New passwords do not match!";
        } else if (newPassword.length < 6) {
            message.textContent = "Password must be at least 6 characters long!";
        } else {
            message.textContent = "Password updated successfully!";
            message.classList.remove("text-danger");
            message.classList.add("text-success");

            // Simulating password update (Replace with actual backend call)
            setTimeout(() => {
                document.getElementById("change-password-form").reset();
                message.textContent = "";
            }, 2000);
        }
    });

    // Toggle 2FA
    let twoFAEnabled = false;
    document.getElementById("toggle-2fa").addEventListener("click", function() {
        twoFAEnabled = !twoFAEnabled;
        let status = document.getElementById("2fa-status");

        if (twoFAEnabled) {
            status.textContent = "Two-Factor Authentication is ENABLED.";
            this.textContent = "Disable 2FA";
            this.classList.remove("btn-warning");
            this.classList.add("btn-danger");
        } else {
            status.textContent = "Two-Factor Authentication is DISABLED.";
            this.textContent = "Enable 2FA";
            this.classList.remove("btn-danger");
            this.classList.add("btn-warning");
        }
    });

    // Simulate Login Activity Data
    let loginActivity = [
        { date: "2024-02-05 10:30 AM", device: "Windows PC", location: "Lagos, Nigeria" },
        { date: "2024-02-04 08:15 PM", device: "iPhone 13", location: "Abuja, Nigeria" },
        { date: "2024-02-03 06:50 AM", device: "MacBook Air", location: "Accra, Ghana" }
    ];

    let activityTable = document.getElementById("login-activity");
    loginActivity.forEach(entry => {
        let row = `<tr>
            <td>${entry.date}</td>
            <td>${entry.device}</td>
            <td>${entry.location}</td>
        </tr>`;
        activityTable.innerHTML += row;
    });
});

//account preference
document.addEventListener("DOMContentLoaded", function() {
    // Load saved preferences from localStorage
    function loadPreferences() {
        let theme = localStorage.getItem("theme") || "light";
        let language = localStorage.getItem("language") || "en";
        let currency = localStorage.getItem("currency") || "USD";

        document.getElementById("theme-selector").value = theme;
        document.getElementById("language-selector").value = language;
        document.getElementById("currency-selector").value = currency;

        applyTheme(theme);
    }

    // Apply theme
    function applyTheme(theme) {
        if (theme === "dark") {
            document.body.classList.add("dark-mode");
        } else {
            document.body.classList.remove("dark-mode");
        }
    }

    // Save preferences
    document.getElementById("save-preferences").addEventListener("click", function() {
        let theme = document.getElementById("theme-selector").value;
        let language = document.getElementById("language-selector").value;
        let currency = document.getElementById("currency-selector").value;

        localStorage.setItem("theme", theme);
        localStorage.setItem("language", language);
        localStorage.setItem("currency", currency);

        document.getElementById("preferences-message").textContent = "Preferences saved successfully!";
        document.getElementById("preferences-message").classList.add("text-success");

        applyTheme(theme);
    });

    // Load preferences on page load
    loadPreferences();
});

//logout
document.addEventListener("DOMContentLoaded", function() {
    // Delete account functionality
    document.getElementById("delete-account-btn").addEventListener("click", function() {
        let password = document.getElementById("confirm-password").value;
        
        if (!password) {
            document.getElementById("delete-account-message").textContent = "⚠️ Please enter your password to confirm deletion.";
            document.getElementById("delete-account-message").classList.add("text-warning");
            return;
        }

        // Show confirmation alert
        if (confirm("Are you sure you want to delete your account? This action cannot be undone!")) {
            // Simulate an API call (Replace with actual API request)
            setTimeout(() => {
                document.getElementById("delete-account-message").textContent = "✅ Your account has been successfully deleted.";
                document.getElementById("delete-account-message").classList.add("text-success");

                // Redirect user after deletion (Example: Logout page)
                setTimeout(() => {
                    window.location.href = "/logout";
                }, 2000);
            }, 1500);
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const buyBtn = document.querySelector(".btn-success");
    const sellBtn = document.querySelector(".btn-danger");
    const assetType = document.getElementById("assetType");
    const amountInput = document.getElementById("amount");
    const transactionSummary = document.getElementById("transactionSummary");
    const summaryAsset = document.getElementById("summaryAsset");
    const summaryAmount = document.getElementById("summaryAmount");

    function updateTransaction(action) {
        const asset = assetType.options[assetType.selectedIndex].text;
        const amount = amountInput.value;

        if (amount === "" || amount <= 0) {
            alert("Please enter a valid amount.");
            return;
        }

        summaryAsset.innerText = asset;
        summaryAmount.innerText = amount;
        transactionSummary.style.display = "block";

        alert(`You have chosen to ${action} ${asset} worth $${amount}`);
    }

    buyBtn.addEventListener("click", () => updateTransaction("buy"));
    sellBtn.addEventListener("click", () => updateTransaction("sell"));
});

function calculateInvestment() {
    let amount = parseFloat(document.getElementById("investment-amount").value);
    let duration = parseFloat(document.getElementById("investment-duration").value);
    let returnRate = parseFloat(document.getElementById("expected-return").value);

    if (isNaN(amount) || isNaN(duration) || isNaN(returnRate)) {
        document.getElementById("investment-result").innerHTML = "<p class='text-danger'>Please fill all fields correctly!</p>";
        return;
    }

    // Simple investment formula: Final Value = Initial Amount * (1 + Rate/100) ^ Duration
    let finalValue = amount * Math.pow((1 + returnRate / 100), duration / 12);
    finalValue = finalValue.toFixed(2);

    document.getElementById("investment-result").innerHTML = `<p>Estimated Future Value: <strong>$${finalValue}</strong></p>`;
}

document.addEventListener("DOMContentLoaded", function () {
    // Get all "Invest Now" buttons
    const investButtons = document.querySelectorAll(".invest-now-btn");

    investButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default anchor behavior

            // Get asset name from the button's data-attribute
            const assetName = this.getAttribute("data-asset") || "Investment Package";

            // Update modal title and content dynamically
            document.getElementById("investmentModalTitle").innerText = `Invest in ${assetName}`;
            document.getElementById("investmentModalText").innerText = `Explore investment options in ${assetName} and grow your portfolio.`;

            // Show the modal
            const investmentModal = new bootstrap.Modal(document.getElementById("investmentModal"));
            investmentModal.show();
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Sample transaction data
    const transactions = [
        { date: "2024-02-07", type: "Deposit", amount: 500, status: "Completed" },
        { date: "2024-02-05", type: "Investment", amount: 1000, status: "Pending" },
        { date: "2024-01-30", type: "Withdrawal", amount: 200, status: "Completed" },
    ];

    const tableBody = document.getElementById("transactionTable");
    const filterBtn = document.getElementById("filterBtn");

    // Function to display transactions
    function displayTransactions(filteredTransactions) {
        tableBody.innerHTML = "";
        filteredTransactions.forEach(tx => {
            const row = `
                <tr>
                    <td>${tx.date}</td>
                    <td>${tx.type}</td>
                    <td>$${tx.amount}</td>
                    <td><span class="badge bg-${tx.status === "Completed" ? "success" : "warning"}">${tx.status}</span></td>
                    <td><button class="btn btn-info btn-sm">View</button></td>
                </tr>`;
            tableBody.innerHTML += row;
        });
    }

    // Function to filter transactions
    function filterTransactions() {
        const startDate = document.getElementById("startDate").value;
        const endDate = document.getElementById("endDate").value;
        const transactionType = document.getElementById("transactionType").value;
        const minAmount = document.getElementById("minAmount").value;
        const maxAmount = document.getElementById("maxAmount").value;

        let filteredTransactions = transactions.filter(tx => {
            const txDate = new Date(tx.date);
            const fromDate = startDate ? new Date(startDate) : null;
            const toDate = endDate ? new Date(endDate) : null;

            return (
                (!fromDate || txDate >= fromDate) &&
                (!toDate || txDate <= toDate) &&
                (transactionType === "" || tx.type === transactionType) &&
                (!minAmount || tx.amount >= minAmount) &&
                (!maxAmount || tx.amount <= maxAmount)
            );
        });

        displayTransactions(filteredTransactions);
    }

    // Event listener for filtering
    filterBtn.addEventListener("click", filterTransactions);

    // Function to export transactions as CSV
    function exportCSV() {
        let csvContent = "Date,Type,Amount,Status\n";
        transactions.forEach(tx => {
            csvContent += `${tx.date},${tx.type},${tx.amount},${tx.status}\n`;
        });

        const blob = new Blob([csvContent], { type: "text/csv" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "transactions.csv";
        link.click();
    }

    // Function to export transactions as PDF
    function exportPDF() {
        const pdfContent = transactions.map(tx => `${tx.date} - ${tx.type} - $${tx.amount} - ${tx.status}`).join("\n");
        const blob = new Blob([pdfContent], { type: "application/pdf" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "transactions.pdf";
        link.click();
    }

    // Event listeners for export buttons
    document.getElementById("exportCSV").addEventListener("click", exportCSV);
    document.getElementById("exportPDF").addEventListener("click", exportPDF);

    // Display initial transactions
    displayTransactions(transactions);
});

function processTransfer() {
    let source = document.getElementById("sourceAsset").value;
    let destination = document.getElementById("destinationAsset").value;
    let amount = document.getElementById("transferAmount").value;

    if (source === destination) {
        alert("You cannot transfer funds to the same asset.");
        return;
    }

    if (amount <= 0) {
        alert("Enter a valid transfer amount.");
        return;
    }

    alert(`Successfully transferred $${amount} from ${source.toUpperCase()} to ${destination.toUpperCase()}`);
}

//payment method
function addPaymentMethod() {
    let paymentType = document.getElementById("paymentType").value;
    let accountDetails = document.getElementById("accountDetails").value;

    if (accountDetails.trim() === "") {
        alert("Please enter account details.");
        return;
    }

    alert(`Payment method added: ${paymentType.toUpperCase()} - ${accountDetails}`);
    document.getElementById("addPaymentModal").classList.remove("show");
}

//withdrawal
// Show withdrawal details in modal
document.querySelector("button[data-bs-target='#withdrawConfirmModal']").addEventListener("click", function() {
    let amount = document.getElementById("withdrawAmount").value;
    let method = document.getElementById("withdrawMethod").value;

    if (amount <= 0) {
        alert("Please enter a valid amount.");
        return;
    }

    document.getElementById("confirmWithdrawAmount").textContent = amount;
    document.getElementById("confirmWithdrawMethod").textContent = method.toUpperCase();
});

// Process withdrawal
function processWithdrawal() {
    let amount = document.getElementById("withdrawAmount").value;
    let method = document.getElementById("withdrawMethod").value;

    alert(`Withdrawal of $${amount} via ${method.toUpperCase()} has been submitted.`);
    document.getElementById("withdrawAmount").value = "";
}

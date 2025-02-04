document.getElementById("calculate").addEventListener("click", function() {
    let amount = document.getElementById("amount").value;
    let interest = document.getElementById("interest").value;

    fetch("http://127.0.0.1:5000/calculate_emi", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ amount: amount, interest: interest, tenure: tenure })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "EMI: " + data.emi;
    });
});

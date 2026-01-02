function checkJob() {
    const text = document.getElementById("jobText").value;

    fetch("/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        let resultHTML = `
            <h3>Risk Level: ${data.risk_level}</h3>
            <p>Risk Score: ${data.risk_score}%</p>
            <ul>
        `;

        data.reasons.forEach(reason => {
            resultHTML += `<li>${reason}</li>`;
        });

        resultHTML += "</ul>";
        document.getElementById("result").innerHTML = resultHTML;
    });
}

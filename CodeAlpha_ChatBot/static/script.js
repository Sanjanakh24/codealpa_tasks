function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chat-box").innerHTML +=
            "<p><b>You:</b> " + message + "</p>" +
            "<p><b>Bot:</b> " + data.reply + "</p>";
    });

    input.value = "";
}

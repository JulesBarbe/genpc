document.addEventListener("DOMContentLoaded", () => {
  // Function to send AJAX request to Flask
  function sendRequest(url, data) {
    return fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }).then((response) => response.json());
  }

  // Handle Global Knowledge Text Input
  document.getElementById("uploadGlobalText").addEventListener("click", () => {
    const text = "Sample Global Text"; // Replace with actual text input
    sendRequest("/upload-text", { type: "global", text: text }).then((data) =>
      console.log(data)
    );
  });

  // Handle Global Knowledge Text enhancing
  document.getElementById("enhanceGlobalText").addEventListener("click", () => {
    const text = "Enhance keywords" //TODO: get text from user
    sendRequest("/enhance-text", { type: "global", text: text }).then((data) =>
      console.log(data)
    ); //TODO: show to user to decide if they want to add
  });

  // Handle Local Knowledge Text Input
  document.getElementById("uploadLocalText").addEventListener("click", () => {
    const text = "Sample Local Text"; // Replace with actual text input
    sendRequest("/upload-text", { type: "local", text: text }).then((data) =>
      console.log(data)
    );
  });

  // Handle Local Knowledge Text enhancing
  document.getElementById("enhanceLocalText").addEventListener("click", () => {
    const text = "Enhance keywords" //TODO: get text from user
    sendRequest("/enhance-text", { type: "global", text: text }).then((data) =>
      console.log(data)
    ); //TODO: show to user to decide if they want to add
  });

  // Handle Chatbot Message Send
  document.getElementById("sendMessage").addEventListener("click", () => {
    const userInput = document.getElementById("userInput").value;
    document.getElementById("userInput").value = ""; // Clear input field
    sendRequest("/chat", { message: userInput }).then((data) => {
      const chatArea = document.getElementById("chatArea");
      chatArea.innerHTML += `<div>User: ${userInput}</div>`;
      chatArea.innerHTML += `<div>Bot: ${data.response}</div>`;
    });
  });

  // Switch between setup and analysis mode for dynamic section
  document.getElementById("toggleMode").addEventListener("click", () => {
    const setupMode = document.getElementById("setupMode");
    const analysisMode = document.getElementById("analysisMode");

    if (setupMode.classList.contains("hidden")) {
      setupMode.classList.remove("hidden");
      analysisMode.classList.add("hidden");
    } else {
      setupMode.classList.add("hidden");
      analysisMode.classList.remove("hidden");
    }
  });
});

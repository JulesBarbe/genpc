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
      console.log("weeeeee")
    );
  });

  // Handle Global Knowledge Text enhancing
  document.getElementById("enhanceGlobalText").addEventListener("click", () => {
    const text = "Enhance keywords"; //TODO: get text from user
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
    const text = "Enhance keywords"; //TODO: get text from user
    sendRequest("/enhance-text", { type: "global", text: text }).then((data) =>
      console.log(data)
    ); //TODO: show to user to decide if they want to add
  });

  // Handle Chatbot Message Send
  document.getElementById("sendMessage").addEventListener("click", () => {
    const userInput = document.getElementById("userInput").value;
    document.getElementById("userInput").value = ""; // Clear input field

    //TODO: handle streaming
    animateGif();
    sendRequest("/chat", { message: userInput }).then((data) => {
      const chatArea = document.getElementById("chatArea");
      chatArea.innerHTML += `<div>User: ${userInput}</div>`;
      chatArea.innerHTML += `<div>Bot: ${data.response}</div>`;
    });
  });

  // Setup - Analysis mode switching
  const toggleModeButton = document.getElementById("toggleMode");
  toggleModeButton.addEventListener("click", () => {
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

  // Setup - Add Trigger
  const addTriggerButton = document.getElementById("addTrigger");
  const triggerModal = document.getElementById("triggerModal");
  const modalContent = document.querySelector(".trigger-modal-content"); // Add this class to your modal's content div
  const saveTriggerButton = document.getElementById("saveTrigger");
  const triggerList = document.getElementById("triggerList");
  const triggerText = document.getElementById("triggerText");
  saveTriggerButton.disabled = true;

  addTriggerButton.addEventListener("click", () => {
    triggerModal.classList.remove("hidden");
  });

  triggerModal.addEventListener("click", (event) => {
    if (event.target === triggerModal) {
      triggerModal.classList.add("hidden");
      // Clear input fields
      document.getElementById("triggerWord").value = "";
      document.getElementById("triggerValue").value = "";
      document.getElementById("triggerText").value = "";
    }
  });

  // Prevent modal content clicks from propagating to the background
  modalContent.addEventListener("click", (event) => {
    event.stopPropagation();
  });

  // Event listener to enable button when there's text
  triggerText.addEventListener("input", () => {
    saveTriggerButton.disabled = triggerText.value.trim() === "";
  });

  saveTriggerButton.addEventListener("click", () => {
    const word = document.getElementById("triggerWord").value;
    const value = document.getElementById("triggerValue").value;
    const text = document.getElementById("triggerText").value;

    // send to backend
    sendRequest("/add-trigger", {
      metric: word,
      value: value,
      text: text,
    }).then((data) => console.log(data));

    const newTrigger = document.createElement("li");
    newTrigger.classList.add("flex", "justify-between", "items-center", "mb-2");

    const textSpan = document.createElement("span");
    textSpan.textContent = `▇  ${word} - ${value} - ${
      text.length > 50 ? text.substring(0, 50) + "..." : text
    }`;
    textSpan.classList.add("flex-grow", "pr-2"); // Add padding to the right

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.classList.add(
      "bg-red-500",
      "hover:bg-red-700",
      "text-white",
      "font-bold",
      "py-1",
      "px-2",
      "text-xs",
      "rounded"
    );
    deleteButton.onclick = function () {
      triggerList.removeChild(newTrigger);
    };

    newTrigger.appendChild(textSpan);
    newTrigger.appendChild(deleteButton);
    triggerList.appendChild(newTrigger);

    // Clear input fields
    document.getElementById("triggerWord").value = "";
    document.getElementById("triggerValue").value = "";
    document.getElementById("triggerText").value = "";
    triggerModal.classList.add("hidden"); // Hide modal after saving
  });

  // Analysis
  const ctx = document.getElementById("lineChart").getContext("2d");
  const lineChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Label 1", "Label 2", "Label 3"], // Replace with your labels
      datasets: [
        {
          label: "Metric 1",
          data: [
            /* data points */
          ],
          borderColor: "rgb(255, 99, 132)", // Line color
          backgroundColor: "rgba(255, 99, 132, 0.5)", // Fill color
        },
        // ... Repeat for each metric ...
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
      plugins: {
        legend: {
          position: "top",
        },
      },
    },
  });

  // Face Gif lol
  const gifElement = document.getElementById("animatedGif");
  gifElement.src = "content/morshu-paused.gif";

  function animateGif() {
    gifElement.src = "content/morshu.gif";
  }

  function pauseGif() {
    gifElement.src = "content/morshu-paused.gif";
  }
});

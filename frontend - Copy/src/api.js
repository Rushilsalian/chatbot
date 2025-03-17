const API_BASE_URL = "http://localhost:5000";

export const askChatbot = async (question) => {
  try {
    const response = await fetch(`${API_BASE_URL}/ask`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: question }),
    });

    const data = await response.json();

    if (data.response) {
      console.log("Chatbot says:", data.response);
      return data.response;
    } else if (data.error) {
      console.error("Chatbot error:", data.error);
      return "Error from chatbot: " + data.error;
    } else {
      return "Unexpected response from chatbot.";
    }
  } catch (error) {
    console.error("Error fetching response:", error);
    return "Error connecting to chatbot.";
  }
};

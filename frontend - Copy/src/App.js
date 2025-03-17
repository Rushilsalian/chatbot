import React, { useState } from "react";
import { askChatbot } from "./api";
import {
  TextField,
  Button,
  Card,
  CardContent,
  Typography,
  Box,
} from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import ChatBubbleOutlineIcon from "@mui/icons-material/ChatBubbleOutline";
import { motion } from "framer-motion";

const App = () => {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);

  const handleAsk = async () => {
    if (!question.trim()) return;
    const botResponse = await askChatbot(question);
    setResponse(botResponse);
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        alignItems: "center",
        height: "100vh",
        background: "linear-gradient(135deg, #1e3c72, #2a5298)",
        color: "#fff",
        padding: 2,
      }}
    >
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Typography variant="h3" align="center" gutterBottom>
          <ChatBubbleOutlineIcon fontSize="large" /> Chatbot
        </Typography>
      </motion.div>

      {/* Scrollable content for responses */}
      <Box
        sx={{
          maxHeight: "calc(100vh - 200px)", // Adjust based on the fixed section height
          overflowY: "auto",
          width: "100%",
          marginBottom: "80px", // Space for the fixed input section
          padding: "0 16px", // Optional: Add padding for left and right space
        }}
      >
        {response && (
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5 }}
          >
            <Card
              sx={{
                mt: 3,
                backgroundColor: "#f5f5f5",
                color: "#000",
                width: "100%", // Ensure it takes up full width
                borderRadius: 2, // Optional: For rounded corners
                boxShadow: 3, // Optional: Add shadow for better visual depth
              }}
            >
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Response:
                </Typography>
                <Typography>{response}</Typography>
              </CardContent>
            </Card>
          </motion.div>
        )}
      </Box>

      {/* Fixed input section */}
      <Box
        sx={{
          position: "fixed",
          bottom: 0,
          left: 0,
          width: "100%",
          padding: "16px",
          backgroundColor: "#fff",
          display: "flex",
          gap: 1,
          alignItems: "center",
          zIndex: 1000, // Ensure it stays above other content
        }}
      >
        <TextField
          fullWidth
          variant="outlined"
          placeholder="Ask me anything..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          sx={{ backgroundColor: "#fff", borderRadius: 1 }}
        />
        <Button
          variant="contained"
          color="secondary"
          onClick={handleAsk}
          sx={{ padding: "12px" }}
        >
          <SendIcon />
        </Button>
      </Box>
    </Box>
  );
};

export default App;

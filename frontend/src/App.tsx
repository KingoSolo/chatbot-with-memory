import { useState } from "react";
import ChatMessage from "./components/chat/ChatMessage";

type Message = {
  role: "user" | "assistant";
  content: string;
};

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const data = await response.json();

    const botMessage: Message = {
      role: "assistant",
      content: data.response,
    };

    setMessages((prev) => [...prev, botMessage]);
    setInput("");
    setLoading(false);
  };

  return (
    
    <div className="h-screen bg-gray-900 text-white flex flex-col">
      <div className="flex-grow overflow-y-auto p-4 space-y-3">
        {messages.map((msg, i) => (
          <ChatMessage key={i} role={msg.role} content={msg.content} />
        ))}

        {loading && (
          <div className="text-gray-400 italic">
            Llama is thinking…
          </div>
        )}
      </div>

      <h1 className="text-red-500">Tailwind is OK</h1>

      <div className="p-4 border-t border-gray-700">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type your message…"
          className="w-full p-3 rounded-lg bg-gray-800 border border-gray-700 text-white outline-none"
        />
      </div>
    </div>
  );
}

export default App;
import { useState } from "react";
import ChatLayout from "../components/chat/ChatLayout";
import ChatList from "../components/chat/ChatList";
import ChatInput from "../components/chat/ChatInput";
import ChatLoader from "../components/chat/ChatLoader";

export default function ChatPage() {
  const [messages, setMessages] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = (text: string) => {
    setMessages((prev) => [...prev, { sender: "user", message: text }]);

    setLoading(true);

    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", message: "Thanks! I received your message." },
      ]);
      setLoading(false);
    }, 900);
  };

  return (
    <ChatLayout>
      <ChatList messages={messages} />

      {loading && <ChatLoader />}

      <ChatInput onSend={sendMessage} />
    </ChatLayout>
  );
}
import { useState } from "react";
import Button from "../ui/Button";

export default function ChatInput({ onSend }: any) {
  const [text, setText] = useState("");

  const send = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  return (
    <div className="flex items-center gap-3 p-3 border-t bg-white">
      <input
        className="flex-1 p-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500"
        placeholder="Type a message..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <Button onClick={send}>Send</Button>
    </div>
  );
}
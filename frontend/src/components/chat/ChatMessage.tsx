import Avatar from "../ui/Avatar";

export default function ChatMessage({ sender, message }: any) {
  const isUser = sender === "user";

  return (
    <div className={`flex gap-3 w-full ${isUser ? "justify-end" : ""}`}>
      {!isUser && <Avatar />}
      <div
        className={`max-w-md p-3 rounded-xl text-sm leading-relaxed shadow-sm ${
          isUser
            ? "bg-blue-600 text-white rounded-br-none"
            : "bg-gray-100 text-gray-900 rounded-bl-none"
        }`}
      >
        {message}
      </div>
      {isUser && <Avatar src="https://api.dicebear.com/9.x/pixel-art/svg" />}
    </div>
  );
}
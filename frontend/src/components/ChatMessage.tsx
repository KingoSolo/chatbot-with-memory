type Props = {
  role: "user" | "assistant";
  content: string;
};

export default function ChatMessage({ role, content }: Props) {
  const isUser = role === "user";

  return (
    <div className={`my-2 flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`px-4 py-2 rounded-2xl max-w-[80%] ${
          isUser ? "bg-blue-600 text-white" : "bg-gray-700 text-white"
        }`}
      >
        {content}
      </div>
    </div>
  );
}
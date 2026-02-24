import ChatMessage from "./ChatMessage";

export default function ChatList({ messages }: any) {
  return (
    <div className="flex flex-col gap-4 p-4 overflow-y-auto">
      {messages.map((msg: any, index: number) => (
        <ChatMessage key={index} sender={msg.sender} message={msg.message} />
      ))}
    </div>
  );
}
export default function ChatLayout({ children }: any) {
  return (
    <div className="flex flex-col h-screen max-w-3xl mx-auto bg-white shadow-lg">
      {children}
    </div>
  );
}
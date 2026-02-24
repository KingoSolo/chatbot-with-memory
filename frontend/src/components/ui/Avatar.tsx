export default function Avatar({ src }: { src?: string }) {
  return (
    <div className="w-10 h-10 rounded-full bg-gray-300 overflow-hidden flex items-center justify-center">
      {src ? (
        <img src={src} alt="Avatar" className="w-full h-full object-cover" />
      ) : (
        <span className="text-gray-600 text-sm">AI</span>
      )}
    </div>
  );
}
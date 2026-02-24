export default function Button({ children, ...props }: any) {
  return (
    <button
      {...props}
      className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700 transition disabled:opacity-40"
    >
      {children}
    </button>
  );
}
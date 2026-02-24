export default function Textarea(props: any) {
  return (
    <textarea
      {...props}
      className="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
    />
  );
}
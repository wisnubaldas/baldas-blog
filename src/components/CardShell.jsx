function CardShell({ children }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-sm px-6 py-8 ring shadow-sm ring-blue-500/50 transition hover:-translate-y-1 hover:shadow-2xl h-full">
      {children}
    </div>
  )
}

export default CardShell

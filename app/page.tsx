import App from "@/components/App";


export default function Home() {
  return (
    <main className="h-full w-full flex flex-col items-center justify-center">
      <div className='w-fit flex flex-col items-center'>
        <h1 className="">Enter your code</h1>
        <App />
      </div>
    </main>
  )
}

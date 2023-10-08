import App from "@/components/App";
import MongoTest from "@/components/MongoTest";


export default function Home() {
  return (
    <main className="h-full w-full flex flex-col items-center justify-center">
      <div className='w-fit flex flex-col items-center'>
        <h1 className="">Enter your code</h1>
        <App />
        <MongoTest />
      </div>
    </main>
  )
}

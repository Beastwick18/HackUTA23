import Camera from "@/components/CustomWebcam";


export default function Home() {
  return (
    <main className="h-full w-full flex flex-col items-center justify-center">
      <div className='w-fit flex flex-col items-center'>
        <Camera />
      </div>
    </main>
  )
}

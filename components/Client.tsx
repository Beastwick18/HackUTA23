import { useRef } from "react";

const Host = () => {
  const user = useRef(null)
  const id = useRef(null)
  const click = () => {
    const username = user.current?.['value']
    const id_value = id.current?.['value']
  }
  return (
    <div className="w-full h-full flex flex-col justify-center">
      <input ref={user} placeholder="Username" />
      <input ref={id} placeholder="Room ID" />
      <button onClick={click}>Join</button>
    </div>
  );
}

export default Host

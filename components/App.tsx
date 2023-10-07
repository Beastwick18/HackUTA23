"use client";

import { useEffect, useRef, useState } from "react"

const App = () => {
  const [state, setState] = useState("");
  const input = useRef(null)
  const click = () => {
    if (input.current && 'value' in input.current) {
      fetch(`/api/game_id?id=${input.current['value']}`)
        .then((res) => res.json())
        .then((json) => {
          console.log(json['message'])
          setState("The message is " + json['message'])
        })
    }

  }
  return (
    <div className="flex flex-col">
      <input placeholder='Code...' ref={input}></input>
      <button onClick={click}>Button</button>
      {state}
    </div>
  )
}

export default App;

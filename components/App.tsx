"use client";

import { useEffect, useRef, useState } from "react"
import CustomWebcam from "./CustomWebcam";

const App = () => {
  return (
    <div className="flex flex-col">
      <CustomWebcam />
    </div>
  )
}

export default App;

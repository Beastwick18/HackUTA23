"use client";

import { MongoClient, ServerApiVersion } from "mongodb";
import { useEffect, useState } from "react";


const MongoTest = () => {
  const [data, setData] = useState(null)
  const getMongo = async () => {
    const d = {
      id: 5002
    }
    const res = await fetch("/api/room_info", {
      method: "POST",
      body: JSON.stringify(d)
    })
    const json = await res.json()
    setData(json['data'])
    console.log(json)
    console.log(JSON.stringify(d))
  }
  useEffect(() => {
    const result = getMongo().catch(console.error)
    console.log(result)
  }, []);
  return (
    <div>
      {
        data ? data : "asd"
      }
    </div>
  )
}

export default MongoTest;

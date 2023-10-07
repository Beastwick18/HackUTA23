"use client";

import { MongoClient, ServerApiVersion } from "mongodb";
import { useEffect } from "react";

type MongoTestProps = {
  client: MongoClient
}

const MongoTest: React.FC<MongoTestProps> = ({ client }) => {
  const getMongo = async () => {
    try {
      await client.connect()
      await client.db("admin").command({ ping: 1 })
      console.log('wowzers')
    } finally {
      await client.close()
    }
  }
  useEffect(() => {
    const result = getMongo().catch(console.error)
    console.log(result)
  }, []);
  return (
    <div></div>
  )
}

export default MongoTest;

import { Roboto_Mono } from "next/font/google";
import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");
    let roomId = parseInt(req.body["id"])
    // let room = await db.collection("rooms").findOne({ id: roomId })
    // let room = await db.collection("rooms").find({ id: roomId }).toArray()
    // if (room.length > 0) {
    const result = await db.collection("rooms").updateMany({ id: roomId }, { $set: { playing: 1 } }, { upsert: true })
    console.log(`${roomId}`)
    console.log(result)
    res.status(200).send("lmao")
    // }

    // res.status(200).json({ data: players })
  } catch (e) {
    res.status(400).send("err")
    console.error(e);
  }
};

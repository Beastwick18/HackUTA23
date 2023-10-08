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
    const result = await db.collection("rooms").find({ id: roomId }).toArray()
    console.log(`${roomId}`)
    res.status(200).send(result[0]['playing'])

    // res.status(200).json({ data: players })
  } catch (e) {
    res.status(400).send("err")
    console.error(e);
  }
};

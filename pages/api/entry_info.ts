import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";

export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");
    let roomId = parseInt(req.body["id"])
    let room = await db.collection("rooms").findOne({ id: roomId })
    // let players = await db.collection("players").find({ roomId: roomId }).toArray()
    res.status(200).json({ data: room })
    console.log("wow");

  } catch (e) {
    res.status(400).send("err")
    console.error(e);
  }
};


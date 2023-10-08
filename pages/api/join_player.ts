import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");
    const username = req.body["username"]
    const roomId = parseInt(req.body["id"])
    const result = await db.collection("rooms").find({ id: roomId }).toArray()
    const player = await db.collection("players").find({ roomId: roomId, username: username }).toArray()
    if (result.length > 0 && player.length <= 0) {
      await db.collection("players").insertOne({ username: username, roomId: roomId });
      res.status(200).send("OK")
      return;
    }
    console.log(result)
  } catch (err: any) {
    console.log(err)
  }
  res.status(400).send("err")
};

import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");
    const id = req.body["id"]
    // const result = await db.collection("rooms").find({ id: roomId }).toArray()
    const player = await db.collection("players").find({ roomId: id }).toArray()
    // await db.collection("players").updateOne({ username: username }, { $set: { ready: 1 } });
    res.status(200).send()
    return;
    //console.log(result)
  } catch (err: any) {
    console.log(err)
  }
  res.status(400).send("err")
};

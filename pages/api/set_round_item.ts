import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");
    let roomId = parseInt(req.body["id"])
    let roundItem = req.body["roundItem"]
    const result = await db.collection("rooms").updateMany({}, { $set: { roundItem: roundItem, playing: 2 } }, { upsert: true })
    console.log(`${roomId} ${roundItem}`)
    console.log(result)
    res.status(200).send("lmao")
  } catch (e) {
    res.status(400).send("err")
    console.error(e);
  }
};

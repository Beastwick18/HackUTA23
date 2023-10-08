import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");
    const rooms = await db.collection("rooms").deleteMany({ id: parseInt(req.body["id"]) })
    const players = await db.collection("players").deleteMany({ roomId: parseInt(req.body["id"]) })
    console.log(rooms + " " + players)
  } catch (err: any) {
    console.log(err)
  }
  res.status(200).send("OK")
};

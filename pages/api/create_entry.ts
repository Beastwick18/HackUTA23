import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  const getRandomInt = (max: any) => {
    return Math.floor(Math.random() * max);
  }
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");

    let attempts = 0;
    while (attempts < 5) {
      let rand = getRandomInt(9999)
      const rooms = await db.collection("rooms").find({ id: rand }).toArray();
      if (rooms.length <= 0) {
        res.status(200).send(rand)
        db.collection("rooms").insertOne({ id: rand })
        break;
      }
      attempts++;
    }
    if (attempts == 5) {
      res.status(400).send("err")
    }
    // const movies = await db
    //   .collection("rooms")
    //   .find({})
    //   .sort({ metacritic: -1 })
    //   .limit(10)
    //   .toArray();
  } catch (e) {
    res.status(400).send("err")
    console.error(e);
  }
};

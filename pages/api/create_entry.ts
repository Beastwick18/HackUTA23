import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  const getRandomInt = (max: any) => {
    return Math.floor(Math.random() * max);
  }
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");

    let rando = getRandomInt(9999)
    res.status(200).send(rando)
    db.collection("rooms").insertOne({ id: rando, playing: 0, roundItem: "", playing: 0 })
    // break;
    //   }
    //   attempts++;
    // }
    // if (attempts == 5) {
    //   res.status(400).send("err")
    // }
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

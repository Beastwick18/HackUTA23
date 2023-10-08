import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";


export default async (req: NextApiRequest, res: NextApiResponse) => {
  const getRandomInt = (max: any) => {
    return Math.floor(Math.random() * max);
  }
  try {
    const client = await clientPromise;
    const db = client.db("hackuta");
    const image = req.body["image"]
    const labels = req.body["labels"]
    const selected = req.body["selected"]

    let rando = getRandomInt(9999)
    db.collection("rooms").insertOne({ id: rando, playing: 0, image: image, labels: labels, selected: selected })
    res.status(200).send(rando)
  } catch (e) {
    res.status(400).send("err")
    console.error(e);
  }
};

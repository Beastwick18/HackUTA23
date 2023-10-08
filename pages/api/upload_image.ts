import clientPromise from "@/lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";

export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const { ImageAnnotatorClient } = require('@google-cloud/vision').v1;
    const visionClient = new ImageAnnotatorClient({
      keyFilename: "./api.json"
    });
    let response = "err";
    const call = async () => {
      var b64str = req.body['image']
      var username = req.body['username']
      console.log(username)
      var buf = Buffer.from(b64str)
      // const response = await visionClient.batchAnnotateImages(request);
      const request = {
        image: {
          content: b64str
        }
      }
      try {
        const results = await visionClient.labelDetection(request)
        const labels = results[0].labelAnnotations
        response = labels
        console.log("labels:")
        labels.forEach((label: any) => { console.log(label.description) });
      } catch (err: any) {
        console.error(err)
      }
      try {
        const client = await clientPromise;
        const db = client.db("hackuta");
        db.collection("images").insertOne({ username: username, image: b64str })
      } catch (err: any) {
        console.log(err)
      }
      res.status(200).json({ data: response })
    }
    await call()
    res.status(200).send(response)

  } catch (e) {
    console.error(e);
  }
};

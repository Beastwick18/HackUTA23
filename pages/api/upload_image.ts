import clientPromise from "../../lib/mongodb";
import { NextApiRequest, NextApiResponse } from "next";

export default async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const { ImageAnnotatorClient } = require('@google-cloud/vision').v1;
    const visionClient = new ImageAnnotatorClient();
    const call = async () => {
      var b64str = req.body
      var buf = Buffer.from(b64str, "base64")
      const request = {
        buf
      }
      const response = await visionClient.batchAnnotateImages(request);
      console.log(response)
    }
    call()
    console.log(req.body)

  } catch (e) {
    console.error(e);
  }
};

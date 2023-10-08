import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    // res.status(200).write(req.body)
    var b64str = req.body
    var buf = Buffer.from(b64str, "base64")
    const fs = require("fs")
    fs.writeFileSync("image.jpg", buf)
    res.status(200).send(buf)
  } else {
    res.status(400).json({ message: "wrong" })
  }
}

import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const body = req.body['id']
    let result = parseInt(body) * 2
    res.status(200).json({ message: result })
  } else {
    res.status(400).json({ message: "wrong" })
  }
}

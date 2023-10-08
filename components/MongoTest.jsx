"use client";

import React from "react";
import CustomWebcam from "@/components/CustomWebcam"

const WebcamCapture = () => {
  const webcamRef = React.useRef(null);
  const [imgSrc, setImgSrc] = React.useState(null);

  const capture = React.useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImgSrc(imageSrc);
  }, [webcamRef, setImgSrc]);

  return (
    <CustomWebcam />
  );
};

export default WebcamCapture
// "use client";
// 
// import { MongoClient, ServerApiVersion } from "mongodb";
// import React from "react";
// import { useEffect, useState } from "react";
// import Webcam from "react-webcam";
// 
// type TType = {
//   username: string,
//   roomId: number
// }
// type TestType = Array<TType>;
// 
// const videoConstraints = {
//   width: 1280,
//   height: 720,
//   facingMode: "user"
// };
// 
// const MongoTest = () => {
//   // const [data, setData] = useState<TestType | null>(null)
//   // const getMongo = async () => {
//   //   const d = {
//   //     id: "3937"
//   //   }
//   //   const res = await fetch("/api/room_info", {
//   //     method: "POST",
//   //     body: JSON.stringify(d),
//   //     headers: {
//   //       "Content-Type": "application/json",
//   //       // 'Content-Type': 'application/x-www-form-urlencoded',
//   //     },
//   //   })
//   //   const json = await res.json()
//   //   setData(json['data'] as TestType)
//   //   console.log(json)
//   //   console.log(JSON.stringify(d))
//   // }
//   // useEffect(() => {
//   //   const result = getMongo().catch(console.error)
//   //   console.log(result)
//   // }, []);
//   // return (
//   //   <div>
//   //     {
//   //       data ? data.map(item => <div>{item.roomId}, {item.username}</div>) : "asd"
//   //     }
//   //     <Webcam
//   //       audio={false}
//   //       height={720}
//   //       screenshotFormat="image/jpeg"
//   //       width={1280}
//   //       videoConstraints={videoConstraints}
//   //     >
//   //       {({ getScreenshot }) => (
//   //         <button
//   //           onClick={() => {
//   //             const imageSrc = getScreenshot()
//   //           }}
//   //         >
//   //           Capture photo
//   //         </button>
//   //       )}
//   //     </Webcam>
//   //
//   //   </div>
//   // )
//   const webcamRef = React.useRef(null);
//   const [imgSrc, setImgSrc] = React.useState(null);
// 
//   const capture = React.useCallback(() => {
//     if (webcamRef.current) {
//       const imageSrc = webcamRef.current.getScreenshot();
//       setImgSrc(imageSrc);
//     }
//   }, [webcamRef, setImgSrc]);
// 
//   return (
//     <>
//       <Webcam
//         audio={false}
//         ref={webcamRef}
//         screenshotFormat="image/jpeg"
//       />
//       <button onClick={capture}>Capture photo</button>
//       {imgSrc && (
//         <img
//           src={imgSrc}
//         />
//       )}
//     </>
//   );
// }
// 
// export default MongoTest;

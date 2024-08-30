import React, { useState, useEffect } from 'react';
   const { AudioEngine } = require('../native-addons/audio-engine');

   const LoopLibrary = () => {
     const [loops, setLoops] = useState([]);
     const [audioEngine, setAudioEngine] = useState(null);

     useEffect(() => {
       setAudioEngine(new AudioEngine());
     }, []);

     const handleFileSelect = (event) => {
       const files = Array.from(event.target.files);
       setLoops(prevLoops => [...prevLoops, ...files]);
     };

     const playLoop = (filePath) => {
       if (audioEngine) {
         audioEngine.loadAudioFile(filePath);
         audioEngine.play();
       }
     };

     return (
       <div>
         <input type="file" accept="audio/*" multiple onChange={handleFileSelect} />
         <ul>
           {loops.map((loop, index) => (
             <li key={index}>
               {loop.name}
               <button onClick={() => playLoop(loop.path)}>Play</button>
             </li>
           ))}
         </ul>
       </div>
     );
   };

   export default LoopLibrary;
   
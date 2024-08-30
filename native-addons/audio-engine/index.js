// Desc: This file is the entry point for the native audio engine module.
//       It loads the native module and exports it for use in the React app.
//       The native module is used to load and play audio files.
//       The React app uses the native module to load and play audio files.
//       The native module is built using C++ and Node.js.
//       The React app is built using React and Electron.


const audioEngine = require('./build/Release/audio_engine.node'); // Load the native module

module.exports = audioEngine; // Export the native module for use in the React app

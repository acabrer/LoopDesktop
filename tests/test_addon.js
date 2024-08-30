// test_addon.js
const audioEngine = require('../native-addons/audio-engine/build/Release/audio_engine');

// Assuming your addon exports a function called 'initialize'
audioEngine.initialize();

console.log('Audio engine addon loaded successfully!');
// Add more tests here based on the functions your addon provides
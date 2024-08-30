const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  // Load the HTML file
  win.loadFile('index.html');

  // Create a child window for the JUCE app
  const juceWin = new BrowserWindow({
    width: 600,
    height: 400,
    parent: win,
    show: false
  });

  // Correct path considering main.js is in LoopApp/app/main.js
  const jucePath = path.join(__dirname, '..', 'Builds', 'MacOSX', 'build', 'Debug', 'LoopApp.app', 'Contents', 'MacOS', 'LoopApp');
  console.log('Attempting to load JUCE app from:', jucePath); // For debugging

  // Load the JUCE app
  juceWin.loadFile(jucePath);

  // Open the DevTools for debugging
  win.webContents.openDevTools();
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
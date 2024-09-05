# This is the configuration file for the audio_engine module.
# It specifies the source files and include directories for the module.
{
  "targets": [
    {
      "target_name": "audio_engine",
      "sources": [
        "audio_engine_wrapper.cpp",
        "../../native/audio/AudioEngine.cpp",
        "../../JuceLibraryCode/include_juce_audio_basics.mm",
        "../../JuceLibraryCode/include_juce_audio_devices.mm",
        "../../JuceLibraryCode/include_juce_audio_formats.mm",
        "../../JuceLibraryCode/include_juce_audio_processors.mm",
        "../../JuceLibraryCode/include_juce_audio_utils.mm",
        "../../JuceLibraryCode/include_juce_core.mm",
        "../../JuceLibraryCode/include_juce_data_structures.mm",
        "../../JuceLibraryCode/include_juce_events.mm",
        "../../JuceLibraryCode/include_juce_graphics.mm",
        "../../JuceLibraryCode/include_juce_gui_basics.mm",
        "../../JuceLibraryCode/include_juce_gui_extra.mm"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "../../native/audio",
        "../../JuceLibraryCode",
        "../..",
        "/Users/alex/JUCE/modules"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      "cflags!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc": ["-std=c++17"],
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "GCC_ENABLE_CPP_RTTI": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "CLANG_CXX_LANGUAGE_STANDARD": "c++17",
        "MACOSX_DEPLOYMENT_TARGET": "11.0",
        "OTHER_CPLUSPLUSFLAGS": [
          "-std=c++17",
          "-stdlib=libc++",
          "-fexceptions",
          "-frtti",
          "-Wall",
          "-Wno-deprecated-declarations",
          "-Wno-unused-variable",
          "-Wno-unused-function",
          "-Wno-unknown-pragmas"
        ],
        "OTHER_LDFLAGS": [
          "-framework CoreAudioKit",
          "-framework AudioToolbox",
          "-framework CoreAudio",
          "-framework Accelerate",
          "-framework CoreMIDI",
          "-framework IOKit",
          "-framework CoreGraphics",
          "-framework WebKit",
          "-framework Cocoa",
          "-framework OpenGL"
        ]
      },
      "defines": [
        "JUCE_GLOBAL_MODULE_SETTINGS_INCLUDED=1",
        "JUCE_STANDALONE_APPLICATION=1",
        "JUCE_SHARED_CODE=1",
        "JUCE_USE_CURL=0",
        "JUCE_WEB_BROWSER=0",
        "JUCE_USE_CAMERA=0",
        "JUCE_DISPLAY_SPLASH_SCREEN=0",
        "JUCE_REPORT_APP_USAGE=0",
        "JUCE_MODULE_AVAILABLE_juce_audio_basics=1",
        "JUCE_MODULE_AVAILABLE_juce_audio_devices=1",
        "JUCE_MODULE_AVAILABLE_juce_audio_formats=1",
        "JUCE_MODULE_AVAILABLE_juce_audio_processors=1",
        "JUCE_MODULE_AVAILABLE_juce_audio_utils=1",
        "JUCE_MODULE_AVAILABLE_juce_core=1",
        "JUCE_MODULE_AVAILABLE_juce_data_structures=1",
        "JUCE_MODULE_AVAILABLE_juce_events=1",
        "JUCE_MODULE_AVAILABLE_juce_graphics=1",
        "JUCE_MODULE_AVAILABLE_juce_gui_basics=1",
        "JUCE_MODULE_AVAILABLE_juce_gui_extra=1",
        "DEBUG=1",
        "MAC_OS_X_VERSION_MIN_REQUIRED=110000"
      ],
      "conditions": [
        ["OS==\"mac\"", {
          "xcode_settings": {
            "GCC_OPTIMIZATION_LEVEL": "0",
            "GCC_GENERATE_DEBUGGING_SYMBOLS": "YES"
          }
        }]
      ]
    }
  ]
}
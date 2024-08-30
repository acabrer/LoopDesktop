# This is the configuration file for the audio_engine module.
# It specifies the source files and include directories for the module.
{
  "targets": [
    {
      "target_name": "audio_engine",
      "sources": [
        "audio_engine_wrapper.cpp",
        "../../native/audio/AudioEngine.cpp",
        "/Users/alex/JUCE/modules/juce_core/juce_core.mm",
        "/Users/alex/JUCE/modules/juce_events/juce_events.mm",
        "/Users/alex/JUCE/modules/juce_audio_basics/juce_audio_basics.mm",
        "/Users/alex/JUCE/modules/juce_audio_devices/juce_audio_devices.mm",
        "/Users/alex/JUCE/modules/juce_audio_formats/juce_audio_formats.mm",
        "/Users/alex/JUCE/modules/juce_audio_processors/juce_audio_processors.mm",
        "/Users/alex/JUCE/modules/juce_audio_utils/juce_audio_utils.mm",
        "/Users/alex/JUCE/modules/juce_data_structures/juce_data_structures.mm",
        "/Users/alex/JUCE/modules/juce_graphics/juce_graphics.mm",
        "/Users/alex/JUCE/modules/juce_gui_basics/juce_gui_basics.mm",
        "/Users/alex/JUCE/modules/juce_gui_extra/juce_gui_extra.mm"
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
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "MACOSX_DEPLOYMENT_TARGET": "10.13",
        "OTHER_CPLUSPLUSFLAGS": [
          "-std=c++17",
          "-I/Users/alex/JUCE/modules"
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
        "JUCE_USE_CAMERA=0"
      ]
    }
  ]
}
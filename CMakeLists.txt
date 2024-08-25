cmake_minimum_required(VERSION 3.15)
project(LoopApp VERSION 1.0.0)

# Assuming JUCE is in a sibling directory to LoopDesktop
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../../JUCE JUCE)

juce_add_plugin(LoopApp
    FORMATS Standalone
    PRODUCT_NAME "LoopApp Audio Engine")

target_compile_features(LoopApp PRIVATE cxx_std_17)

target_sources(LoopApp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/Source/PluginProcessor.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/Source/PluginEditor.cpp)

target_compile_definitions(LoopApp
    PUBLIC
    JUCE_WEB_BROWSER=0
    JUCE_USE_CURL=0
    JUCE_VST3_CAN_REPLACE_VST2=0)

target_link_libraries(LoopApp PRIVATE
    juce::juce_audio_utils
    juce::juce_recommended_config_flags
    juce::juce_recommended_lto_flags)

#pragma once // include guard

#include <JuceHeader.h> //  include the JUCE library

class AudioEngine : public juce::AudioSource // inherit from AudioSource
{
public: // public methods
    AudioEngine(); // constructor
    ~AudioEngine() override; // destructor

    void prepareToPlay(int samplesPerBlockExpected, double sampleRate) override; // override the prepareToPlay method
    void getNextAudioBlock(const juce::AudioSourceChannelInfo& bufferToFill) override; // override the getNextAudioBlock method
    void releaseResources() override; // override the releaseResources method

    void loadAudioFile(const juce::File& file); // load an audio file
    void play();
    void stop();

private:
    std::unique_ptr<juce::AudioFormatReaderSource> readerSource; // create a unique pointer to an AudioFormatReaderSource
    juce::AudioTransportSource transportSource; // create an AudioTransportSource
    juce::AudioFormatManager formatManager; // create an AudioFormatManager
};

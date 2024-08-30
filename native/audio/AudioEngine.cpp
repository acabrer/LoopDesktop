
#include "AudioEngine.h" // include the header file
#include "../JuceLibraryCode/JuceHeader.h"

AudioEngine::AudioEngine()  // constructor
{
    formatManager.registerBasicFormats(); // register basic audio formats
}

AudioEngine::~AudioEngine() // destructor
{
    releaseResources();
}

void AudioEngine::prepareToPlay(int samplesPerBlockExpected, double sampleRate)
{
    transportSource.prepareToPlay(samplesPerBlockExpected, sampleRate);
}

void AudioEngine::getNextAudioBlock(const juce::AudioSourceChannelInfo& bufferToFill)
{
    if (readerSource.get() == nullptr)
    {
        bufferToFill.clearActiveBufferRegion();
        return;
    }

    transportSource.getNextAudioBlock(bufferToFill);
}

void AudioEngine::releaseResources()
{
    transportSource.releaseResources();
}

void AudioEngine::loadAudioFile(const juce::File& file)
{
    auto* reader = formatManager.createReaderFor(file);

    if (reader != nullptr)
    {
        auto newSource = std::make_unique<juce::AudioFormatReaderSource>(reader, true);
        transportSource.setSource(newSource.get(), 0, nullptr, reader->sampleRate);
        readerSource.reset(newSource.release());
    }
}

void AudioEngine::play()
{
    transportSource.start();
}

void AudioEngine::stop()
{
    transportSource.stop();
}

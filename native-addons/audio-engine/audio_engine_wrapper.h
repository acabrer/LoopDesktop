// Purpose: Declare the AudioEngineWrapper class, which is a wrapper around the AudioEngine class that exposes the AudioEngine class to JavaScript.
// The AudioEngineWrapper class inherits from Napi::ObjectWrap, which is a class provided by the N-API library that allows C++ classes to be exposed to JavaScript.
// The AudioEngineWrapper class has a constructor that takes a Napi::CallbackInfo object as an argument, which is used to create a new instance of the AudioEngineWrapper class.
// The AudioEngineWrapper class has static methods that are used to initialize the object and expose it to JavaScript.
// The AudioEngineWrapper class has instance methods that are used to load an audio file, play the audio, and stop the audio.
// The AudioEngineWrapper class has a private member variable audioEngine, which is a unique pointer to an AudioEngine object.
// The AudioEngineWrapper class has a static member variable constructor, which is a function reference to the constructor.
// The AudioEngineWrapper class has a static Init method that is used to initialize the object and expose it to JavaScript.
// The AudioEngineWrapper class has a LoadAudioFile method that is used to load an audio file.

#pragma once // include guard

#include <napi.h> // include the N-API headers
#include "AudioEngine.h" // include the AudioEngine header file

class AudioEngineWrapper : public Napi::ObjectWrap<AudioEngineWrapper>  // inherit from Napi::ObjectWrap
{
public:
    static Napi::Object Init(Napi::Env env, Napi::Object exports);      // initialize the object
    AudioEngineWrapper(const Napi::CallbackInfo& info);                // constructor

private:
    static Napi::FunctionReference constructor;                       // function reference to the constructor

    Napi::Value LoadAudioFile(const Napi::CallbackInfo& info);     // load an audio file
    Napi::Value Play(const Napi::CallbackInfo& info);           // play the audio
    Napi::Value Stop(const Napi::CallbackInfo& info);          // stop the audio

    std::unique_ptr<AudioEngine> audioEngine;              // create a unique pointer to an AudioEngine
};

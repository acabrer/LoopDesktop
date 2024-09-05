// Purpose: Wraps the AudioEngine class in a Napi object.
// The AudioEngineWrapper class inherits from Napi::ObjectWrap, which is a class provided by the N-API library that allows C++ classes to be exposed to JavaScript.


#include "./audio_engine_wrapper.h"   // include the header file
#include "../../native/audio/AudioEngine.h" // include the AudioEngine header file
#include "../JuceLibraryCode/JuceHeader.h" // include the JUCE library

Napi::FunctionReference AudioEngineWrapper::constructor;

Napi::Object AudioEngineWrapper::Init(Napi::Env env, Napi::Object exports) {
    Napi::HandleScope scope(env);

    Napi::Function func = DefineClass(env, "AudioEngine", {
        InstanceMethod("loadAudioFile", &AudioEngineWrapper::LoadAudioFile),
        InstanceMethod("play", &AudioEngineWrapper::Play),
        InstanceMethod("stop", &AudioEngineWrapper::Stop),
    });

    constructor = Napi::Persistent(func);
    constructor.SuppressDestruct();

    exports.Set("AudioEngine", func);
    return exports;
}

AudioEngineWrapper::AudioEngineWrapper(const Napi::CallbackInfo& info)
    : Napi::ObjectWrap<AudioEngineWrapper>(info) {
    Napi::Env env = info.Env();
    Napi::HandleScope scope(env);

    audioEngine = std::make_unique<AudioEngine>();
}

Napi::Value AudioEngineWrapper::LoadAudioFile(const Napi::CallbackInfo& info) {
    Napi::Env env = info.Env();
    if (info.Length() < 1 || !info[0].IsString()) {
        Napi::TypeError::New(env, "String expected").ThrowAsJavaScriptException();
        return env.Null();
    }

    std::string filePath = info[0].As<Napi::String>().Utf8Value();
    audioEngine->loadAudioFile(juce::File(filePath));

    return env.Undefined();
}

Napi::Value AudioEngineWrapper::Play(const Napi::CallbackInfo& info) {
    audioEngine->play();
    return info.Env().Undefined();
}

Napi::Value AudioEngineWrapper::Stop(const Napi::CallbackInfo& info) {
    audioEngine->stop();
    return info.Env().Undefined();
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    return AudioEngineWrapper::Init(env, exports);
}

NODE_API_MODULE(audio_engine, Init)
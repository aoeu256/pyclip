import speech_recognition as sr
import pyaudio
p = pyaudio.PyAudio()
 
# Initialize the recognizer
r = sr.Recognizer()

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if dev['maxInputChannels'] > 0:
        print('Found microphone: {} {}'.format(i, dev['name']))
 
# Function to convert text to
# speech
def SpeakText(command):
    pass 
    # Initialize the engine
    #import pyttsx3
    #engine = pyttsx3.init()
    #engine.say(command)
    #engine.runAndWait()
    
while True:        
    try:
         
        # use the microphone as source for input.
        with sr.Microphone(device_index=1) as source2:
            # adjust the energy threshold based on
            r.adjust_for_ambient_noise(source2, duration=0.1)
             
            audio2 = r.listen(source2)
             
            MyText = r.recognize_google(audio2, language="ZH")
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            #SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
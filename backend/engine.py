import pyttsx3
from textblob import TextBlob
import time
import os

def analyze_and_generate(text: str, output_dir: str) -> tuple:
    # 1. Analyze Sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # 2. Determine Modulation Parameters
    if polarity > 0.2:
        emotion = "Positive"
        rate = 160       # Fast
        volume = 1.0     # Loud
    elif polarity < -0.2:
        emotion = "Negative"
        rate = 120       # Slow
        volume = 0.6     # Softer
    else:
        emotion = "Neutral"
        rate = 140       # Normal
        volume = 0.8     # Normal

    # 3. Initialize TTS and apply parameters
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # 4. Create a unique filename using a timestamp
    timestamp = int(time.time())
    filename = f"audio_{timestamp}.mp3"
    filepath = os.path.join(output_dir, filename)

    # 5. Save the file
    engine.save_to_file(text, filepath)
    engine.runAndWait()

    return emotion, filename

# ... (Keep your existing analyze_and_generate function above this) ...

if __name__ == "__main__":
    # 1. Setup the path to your generated_audio folder (one level up from backend)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEST_AUDIO_DIR = os.path.join(BASE_DIR, "generated_Audio")
    os.makedirs(TEST_AUDIO_DIR, exist_ok=True)

    print(f"Starting Local Test. Audio will be saved to: {TEST_AUDIO_DIR}\n")

    # 2. Define test sentences covering all three emotional states
    test_sentences = [
        "I am absolutely thrilled and so happy about this amazing news!",  # Should be Positive
        "This is terrible, I am very sad and deeply disappointed.",        # Should be Negative
        "The package is scheduled to arrive on Tuesday afternoon."         # Should be Neutral
    ]

    # 3. Run the sentences through the engine
    for i, sentence in enumerate(test_sentences):
        print(f"Testing Sentence {i+1}: '{sentence}'")
        try:
            emotion, filename = analyze_and_generate(sentence, TEST_AUDIO_DIR)
            print(f"Success! Detected Emotion: {emotion}")
            print(f"Saved File: {filename}")
        except Exception as e:
            print(f"Failed: {e}")
        
        print("-" * 50)
        time.sleep(1) # 1-second pause to ensure unique timestamps for filenames
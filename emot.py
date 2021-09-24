# We install the FER() library to perform facial recognition
# This installation will also take care of any of the above dependencies if they are missing
#pip install FER

from fer import FER
import matplotlib.pyplot as plt


def emo_det(img):
    emo_detector = FER(mtcnn=True)
    # Capture all the emotions on the image
    captured_emotions = emo_detector.detect_emotions(img)
    # Print all captured emotions with the image
    plt.imshow(img)

    # Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(img)
    #return(dominant_emotion, emotion_score)
    return dominant_emotion, emotion_score

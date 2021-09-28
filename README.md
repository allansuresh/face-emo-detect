# Dataset
I used the [FER-2013](http://www.socsci.ru.nl:8180/RaFD2/RaFD?p=main) Faces Database, a set of 28,709 pictures of people displaying 7 emotional expressions (angry, disgusted, fearful, happy, sad, surprised and neutral) to train the model.

# face-emo-detect Setup
Set up a Python virtual environment using the following command in the root directory:

Windows:

```shell
$ python -m venv venv
$ venv\Scripts\activate
```

Mac / Linux:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
```

Install tensorflow and opencv on your virtual python environment

```shell
(venv) $ pip install tensorflow
(venv) $ pip install opencv-python
 ```
 
 Install the FER library on your virtual python environment
 
 ```shell
 (venv) $ pip install FER
 ```

# Run
Run the `det.py` program on your virtual environemt.
The `emo.py` is simply to figure out the emotions {happy, sad, neutral, angry, surprised}.

### Webcam:
A rectangle will appear over your face, showing the face recognition works

### Emotion detection:
The result of this will be displayed on the rectangle box. Both the dominant emotion and score will be shown.

# Quit
Select the webcam window and press 'q' to quit.

# Ouput

![Happy](https://raw.github.com/allansuresh/face-emo-detect/tree/main/Ouput/happy1.png)

![Sad](https://raw.github.com/allansuresh/face-emo-detect/tree/main/Ouput/sad1.png)

![Neutral](https://raw.github.com/allansuresh/face-emo-detect/tree/main/Ouput/neutral2.png)

![Surprise](https://raw.github.com/allansuresh/face-emo-detect/tree/main/Ouput/surprise1.png)

![Fear](https://raw.github.com/allansuresh/face-emo-detect/tree/main/Ouput/fear1.png)

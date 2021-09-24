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

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

![Sad](https://user-images.githubusercontent.com/47358327/135108861-53382a61-3921-4602-ab15-96d088a79d5e.png)
![Surprise](https://user-images.githubusercontent.com/47358327/135108872-d4174ee6-2322-4e0c-84a7-11297f6f0988.png)
![Fear](https://user-images.githubusercontent.com/47358327/135108874-1039cdcb-f2d2-466c-a433-8085ac215940.png)
![Happy](https://user-images.githubusercontent.com/47358327/135108876-57bc4931-116c-46fe-99aa-334051b0c07b.png)
![Neutral](https://user-images.githubusercontent.com/47358327/135108879-bff51249-ab7f-451a-b53b-dd6f080b7518.png)

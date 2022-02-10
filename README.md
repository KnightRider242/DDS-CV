# DDS-CV

Deep-Learning-Drowsy-Driver-Detection-System.

This Repository is a project that uses computer vision to classify whether a driver is Awake or not.

**Using Deep Leaning Models**

CNN (Convalution Neural Networks) for image feature extraction.

## Requirements

> [p]()ip install opencv
>
> conda install opencv

## Run Method

1. Run record.py in the folder "Video-Recorder"
   1. This Script takes your video from webcam and store it in greyscale format
   2. Data stored at "..//Data//Video//"filename".avi"
   3. Video Codec : DIVX and stored in .avi file format
2. Run frame.py in the folder "Extract-Frames"
   1. This script takes in the grayscale video as input.
   2. Extract all the frames and stores at "..//Data//Video//"filename".jpg".
   3. Images stored in **Joint Photographic Experts Group** (JPG) file format.

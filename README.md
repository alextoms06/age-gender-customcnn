# Age and Gender Detection on Raspberry Pi 3

## Overview

This project implements a real-time age and gender detection system running entirely on a Raspberry Pi 3.

The system captures video from the Raspberry Pi Camera, performs face detection and demographic analysis using pretrained ONNX models, and streams annotated results to a web browser.

## Features

* Real-time face detection
* Age estimation
* Gender classification
* Browser-based live video stream
* Fully offline edge AI inference
* Raspberry Pi Camera integration

## Technology Stack

* Raspberry Pi 3
* Python
* OpenCV
* Picamera2
* Flask
* ONNX Runtime
* SCRFD Face Detector
* Age/Gender ONNX Models

## System Architecture

Pi Camera → Frame Capture → Face Detection → Age/Gender Inference → Annotation → Flask Stream → Browser

## Results

* Successful local deployment on Raspberry Pi 3
* Real-time age and gender estimation
* Browser-accessible live video feed
* Edge inference without cloud connectivity

# Age and Gender Detection on Raspberry Pi 3

/table
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

# Real-Time Age and Gender Detection on Raspberry Pi 3

Real-time age and gender detection system deployed on Raspberry Pi 3 using ONNX Runtime, Picamera2, OpenCV and Flask.

---

## Table of Contents

1. Introduction
2. System Architecture
3. Getting Started
4. Results
5. Project Information

---

# 1. Introduction

## What the Project Does

This project implements a real-time age and gender detection system running entirely on a Raspberry Pi 3.

Video is captured using the Raspberry Pi Camera Module, processed locally using pretrained ONNX deep learning models, and streamed to a web browser with live age and gender predictions overlaid on detected faces.

## Why the Project is Useful

The project demonstrates practical Edge AI deployment on resource-constrained hardware. It can serve as a building block for assistive technology, smart surveillance, demographic analytics, human-computer interaction systems, and embedded AI applications where cloud connectivity is unavailable or undesirable.

## Key Features

* Real-time face detection
* Age estimation
* Gender classification
* Browser-based live video stream
* Fully offline inference
* Raspberry Pi Camera integration
* ONNX Runtime deployment
* Edge AI optimization for Raspberry Pi

---

# 2. System Architecture

## Hardware Components

* Raspberry Pi 3 Model B
* Raspberry Pi Camera Module
* Wi-Fi Network
* Browser-enabled device

## Software Stack

* Python
* OpenCV
* Picamera2
* Flask
* ONNX Runtime

## AI Models

* SCRFD Face Detector
* Age/Gender ONNX Model

## Data Flow

Pi Camera → Frame Capture → Face Detection → Age/Gender Classification → Frame Annotation → Flask Server → Browser

[Insert Architecture Diagram Here]

---

# 3. Getting Started

## Prerequisites

* Raspberry Pi OS (64-bit)
* Raspberry Pi Camera Module
* Python 3.x
* Internet Connection

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd <repository_name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Launch the application:

```bash
python age_gender_stream.py
```

Access the stream:

```text
http://<raspberry-pi-ip>:5000
```

---

# 4. Results

## Output

The system successfully performs:

* Face detection
* Age prediction
* Gender classification
* Real-time browser streaming

[Insert Live Detection Screenshot]

## Performance

Platform: Raspberry Pi 3

Current optimizations:

* Reduced frame resolution
* Periodic inference execution
* JPEG compression for streaming

---

# 5. Project Information

## Getting Help

For issues, feature requests, or deployment assistance, please create a GitHub issue.

## Future Improvements

* Voice-based feedback
* Multi-face tracking
* Emotion recognition
* Raspberry Pi 5 deployment
* Mobile application interface

## Maintainer

Alex Thomas

Electronics and Communication Engineering Undergraduate & Intern at CIDAC, Project Coordinator @MACE IOT CLUB and PROJECT INTERN AT NISH, TRIVANDRUM

Mar Athanasius College of Engineering

## Acknowledgement

Age and gender inference is performed using pretrained ONNX models. The focus of this project is edge deployment, optimization, and system integration on Raspberry Pi 3.

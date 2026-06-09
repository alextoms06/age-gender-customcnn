# Age-Gender Detection on Raspberry Pi 3

## Engineering Learning Log

### Initial Objective

Goal: Run age and gender detection from Raspberry Pi camera and display results in real time.

---

### Model Selection

Initial thought:

* Train a custom Haar Cascade classifier.

Learning:

* Haar Cascades are traditional CV models.
* Good for simple face detection.
* Cannot estimate age or gender.
* Lower robustness under varying lighting and poses.

Decision:

* Use pretrained CNN models instead.

Reason:

* Age and gender estimation requires learned facial features.
* CNNs significantly outperform Haar Cascades.

---

### TensorFlow vs ONNX

Initial thought:

* Use TensorFlow models.

Issue:

* TensorFlow installation on Raspberry Pi ARM64 is large and dependency-heavy.
* Existing repository already provided ONNX weights.

Learning:

* ONNX is a model exchange format.
* ONNX Runtime is optimized for inference.
* Deployment is easier than running full TensorFlow.

Decision:

* Use ONNX Runtime.

---

### Camera Access Problem

Initial implementation:

* OpenCV VideoCapture(0)

Issue:

* OpenCV could not access Raspberry Pi camera.

Observed errors:

* Failed to grab frame.
* Camera index out of range.

Learning:

* Modern Raspberry Pi OS uses libcamera.
* CSI camera is not always exposed as a standard USB webcam.

Decision:

* Move to Picamera2.

---

### Camera Hardware Debugging

Observation:

* Camera LED stopped blinking.
* No frames received.

Hypothesis:

* Ribbon cable issue.
* Sensor issue.
* Driver issue.

Tests performed:

* Checked /dev/video devices.
* Checked v4l2 devices.
* Examined dmesg logs.
* Ran libcamera tests.

Learning:

* Presence of camera device does not guarantee image capture.
* CSI ribbon orientation matters.
* Sensor initialization and actual frame acquisition are different stages.

Outcome:

* Camera hardware confirmed working after successful frame capture.

---

### SSH Display Problem

Issue:

* Running OpenCV GUI remotely.

Observed:

* Qt xcb display errors.

Learning:

* SSH sessions have no graphical display.
* cv2.imshow() requires a GUI session.

Decision:

* Browser-based visualization instead of OpenCV windows.

---

### Browser Streaming

Initial thought:

* Display video directly using OpenCV.

Issue:

* Not practical over SSH.

Learning:

* Flask can stream MJPEG frames.
* Browser becomes remote display.

Decision:

* Build Flask streaming server.

Result:

* Video visible on laptop browser.

---

### Raspberry Pi Camera Integration

Issue:

* Existing repository expected OpenCV camera input.

Learning:

* Existing AI pipeline only requires image frames.
* Frame source can be replaced without changing CNN logic.

Decision:

* Feed Picamera2 frames into model pipeline.

Important insight:

* AI model is independent of camera source.

---

### CNN Verification

Question:

* Is the model actually working?

Method:

* Capture still image.
* Run inference on image.

Result:

* Faces detected: 1
* Age: 46
* Gender: 1

Learning:

* Always validate model on a static image before debugging real-time video.

---

### Real-Time Performance Bottleneck

Observation:

* Approximately 7-second delay.

Root cause:

* SCRFD face detector.
* Age/Gender CNN.
* Raspberry Pi 3 CPU limitations.

Learning:

* Edge AI performance depends more on inference cost than camera speed.

Optimization:

* Lower resolution.
* Run inference every 5 frames.
* Reduce JPEG quality.

Result:

* Improved responsiveness.

---

### Project-Level Learning

Key realization:

* Most real-world AI projects are not about training models.

Actual work involved:

* Model deployment.
* Hardware integration.
* Camera interfacing.
* Runtime optimization.
* Debugging drivers.
* Building user-facing applications.

Final understanding:

* AI engineering = model + system integration + deployment.

The deployment effort was significantly larger than running the pretrained model itself.

Traffic AI system (YOLO-based vehicle detection, 4-lane video processing, signal logic, and number plate OCR) usually relies on a small ecosystem of Python libraries. Each one plays a different role in the pipeline: computer vision, deep learning, OCR, and utilities.

Think of the system as a little factory. Video frames go in, neural networks inspect them, text readers decode number plates, and OpenCV draws boxes and dashboards.





Computer vision backbone
opencv-python handles video reading, frame processing, drawing bounding boxes, and creating the four-lane display grid. Without it, the system can’t see frames.

Numerical engine
numpy is the silent workhorse. Frames are arrays of numbers, and nearly every vision algorithm manipulates them.

Deep learning framework
torch and torchvision power the neural network that YOLO runs on. They handle GPU acceleration, tensor math, and model loading.

YOLO detection layer
ultralytics provides the YOLO implementation itself. It loads the model and outputs detections like car, truck, bus, bike.

Data handling
pandas helps store vehicle counts, logs, and signal-timing statistics.

Image utilities
pillow supports image transformations used by OCR and preprocessing.

Number plate reading
easyocr extracts text from the detected license plate region.

Tracking & counting
scipy, filterpy, and lap support object tracking algorithms (like SORT/DeepSORT style tracking). These prevent counting the same car multiple times.

Visualization & progress tools
matplotlib helps debugging visual outputs and plots.
tqdm provides progress bars when processing long videos.
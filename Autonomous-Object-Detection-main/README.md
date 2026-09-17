# Autonomous Object Detection Pipeline

A real-time, CPU-optimized object detection system built on the **YOLOv8** architecture. The pipeline takes an input image, runs it through a pre-trained YOLOv8 model, and produces an annotated output image with bounding boxes and confidence scores for each detected object.

**Course:** Computer Vision (CSE3010) — VIT Bhopal University
**Author:** Aditya Rawat (24BAC10015)

---

## 1. Overview

The system follows a linear pipeline:

```
Image Input → Preprocessing → YOLOv8 Model Inference → Postprocessing → Annotated Output
```

It is built around two core classes:

| Class | Responsibility |
|---|---|
| `Detector` | Loads the YOLOv8 model and runs inference on an image |
| `DataProcessor` | Reads input images and saves the annotated output |

The model used is **YOLOv8** (via the Ultralytics library), pre-trained on the **COCO** dataset (80 object categories). The lightweight **COCO8** subset was used during development for fast pipeline validation before running on full-size/production images.

---

## 2. Project Structure

```
computer-vision/
├── src/
│   ├── detector.py          # Detector class — model loading & inference
│   └── data_processor.py    # DataProcessor class — I/O handling
├── main.py                  # CLI entry point
├── data/                    # Place input images here (e.g., test.jpg)
├── runs/
│   └── detect/
│       └── results/
│           └── predictions/ # Annotated output images are saved here
├── yolov8n.pt                # YOLOv8 pre-trained weights (auto-downloaded on first run)
├── requirements.txt
└── README.md
```



---

## 3. Prerequisites

- Python 3.9 or later
- pip (Python package manager)
- ~2 GB free disk space (for PyTorch + model weights)
- (Optional) A CUDA-capable GPU — the pipeline is CPU-optimized and runs without one

Check your Python version:

```bash
python --version
```

---

## 4. Setup Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/A-R-star/Autonomous-Object-Detection/tree/main
cd <Autonomous-Object-Detection>
```

### Step 2: Create and activate a virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` should include, at minimum:

```
ultralytics
opencv-python
torch
numpy
```

### Step 4: Model weights

The pipeline uses `yolov8n.pt` (the nano YOLOv8 variant, chosen for its speed on CPU). Ultralytics will **automatically download** this file on the first run if it isn't already present in the project root. No manual download is required, provided you have an internet connection the first time you run the pipeline.

---

## 5. Running the Project

### Step 1: Add an input image

Place the image you want to run detection on inside the `data/` folder, e.g. `data/test.jpg`.

### Step 2: Run the detection pipeline

```bash
python main.py --source data/test.jpg
```

If you are running the detector script directly instead of through `main.py`:

```bash
python src/detector.py --source data/test.jpg
```

### Step 3: View the results

The annotated output image (with bounding boxes and confidence scores drawn on detected objects) is saved to:

```
runs/detect/results/predictions/
```

Open the saved image to see the detections — for example, objects like `laptop` and `book` will be labeled with their class name and confidence score (e.g., `laptop 0.97`).

---

## 6. Configuration

You can adjust the following in `main.py` / `src/detector.py` as needed:

| Parameter | Description | Default |
|---|---|---|
| `model_path` | Path to the YOLOv8 weights file | `yolov8n.pt` |
| `source` | Path to the input image | `data/test.jpg` |
| `conf` | Minimum confidence threshold for a detection to be kept | `0.25` |
| `save` | Whether to save annotated output images | `True` |

---

## 7. Testing

Testing was carried out via command-line execution on individual images to verify:

1. **Bounding box accuracy** — visually confirming detected objects are correctly localized and labeled.
2. **Inference latency** — benchmarking runtime against the project's target of sub-300 ms per image on CPU.

To reproduce a test run:

```bash
python main.py --source data/test.jpg
```

Check the terminal output for the reported inference time, and inspect the saved image in `runs/detect/results/predictions/` for detection quality.

---

## 8. Troubleshooting

| Issue | Likely Cause / Fix |
|---|---|
| `ModuleNotFoundError: No module named 'ultralytics'` | Run `pip install -r requirements.txt` inside your activated virtual environment |
| Model weights fail to download | Check your internet connection, or manually place `yolov8n.pt` in the project root |
| `FileNotFoundError` for the input image | Confirm the path passed to `--source` matches an actual file in `data/` |
| Slow inference on CPU | Use the `yolov8n` (nano) weights rather than larger variants (`s`/`m`/`l`/`x`), and reduce input image resolution |

---

## 9. Author

**Aditya Rawat**
Registration Number: 24BAC10015
B.Tech ECE (AI and Cybernetics), VIT Bhopal University

from ultralytics import YOLO

def run_detection(image_path, output_path):
    # Load the pre-trained COCO model
    model = YOLO('yolov8n.pt') 
    # Run inference and save the result
    results = model(image_path, save=True, project=output_path, name='predictions', exist_ok=True)
    print(f"Results saved inside the {output_path} folder.")
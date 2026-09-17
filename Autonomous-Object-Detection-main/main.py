import argparse
from src.detector import run_detection

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Object Detection")
    parser.add_argument('--input', type=str, required=True, help='Path to input image or folder')
    parser.add_argument('--output', type=str, default='results', help='Path to save outputs')
    
    args = parser.parse_args()
    run_detection(args.input, args.output)
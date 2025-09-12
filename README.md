# sist2-script-paddleocr
sist2 user script to perform OCR using ![paddle](https://github.com/PaddlePaddle/PaddleOCR) instead of the tesseract default.

## Usage Requirements
See the following for RAM usage of these models:
 - https://www.paddleocr.ai/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html

The script by default uses the PP-OCRv5_server-* models on the CPU with all auxiliary features enabled. **Without any auxiliary features**, this is stated to have a peak RAM usage of **4020.85 MB**.

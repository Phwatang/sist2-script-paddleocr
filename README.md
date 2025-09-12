# sist2-script-paddleocr
sist2 user script to perform OCR using [paddle](https://github.com/PaddlePaddle/PaddleOCR) instead of the tesseract default.

Lasted tested with sist2 v3.5.0 installed under docker.

## Usage Requirements
See the following for RAM usage of these models:
 - https://www.paddleocr.ai/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html

The script by default uses the PP-OCRv5_server-* models on the CPU with all auxiliary features enabled. 
 - **Without any auxiliary features**, this is stated to have a peak RAM usage of **4020.85 MB**
 - From my personal testing, 6 GiB of RAM was enough to handle sist2, elasticsearch and the Paddle scripts all at once

## Extra Command Line Options
Many of the following command line options will relate to how the Paddle model is initialised.
 - https://www.paddleocr.ai/main/en/version3.x/pipeline_usage/OCR.html#22-python-script-integration

```
--append_only=<bool>,                  Output from Paddle is only appended onto the existing content embeddings of the file instead of rewriting it. Default: False
--lang=<str>,                          Language mode of the model. DEFAULT: en
--text_detection_model_name=<str>      Specify text detection model. DEFAULT: PP-OCRv5_server_det
--text_recognition_model_name=<str>    Specify text recognition model. DEFAULT: PP-OCRv5_server_rec
--use_doc_orientation_classify=<bool>  Enable document orientation classification workflow. DEFAULT: True
--use_doc_unwarping=<bool>             Enable document unwarping workflow. Default: True
--use_textline_orientation=<bool>      Enable textline orientation workflow. Default: True
```

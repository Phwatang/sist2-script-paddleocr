#!/bin/bash

# libgl1-mesa-glx need to fix libGL.so.1 issue
# https://github.com/PaddlePaddle/PaddleSeg/issues/3435
apt install libgl1-mesa-glx

pip install -r requirements.txt
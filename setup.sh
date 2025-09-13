#!/bin/bash

# libgl1-mesa-glx need to fix libGL.so.1 issue
# https://github.com/PaddlePaddle/PaddleSeg/issues/3435
apt update -y
apt install libgl1-mesa-glx -y

pip install -r requirements.txt
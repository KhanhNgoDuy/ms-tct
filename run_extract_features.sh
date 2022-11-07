#!/bin/bash

python extract_features.py \
	--mode rgb \
	--root charades/charades_v1_rgb \
	--load_model pytorch-i3d/models/rgb_charades.pt \
	--gpu 0 \
	--save_dir pytorch-i3d/results \
	

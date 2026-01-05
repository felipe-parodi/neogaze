# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NeoGaze is a deep learning system for real-time gaze classification during neonatal resuscitation. It processes first-person POV video from eye-tracking glasses and classifies gaze targets into 7 semantic categories: Airway-Equipment, CMAC-Screen, Infant, Non-Team-Member, Other-Physical-Objects, Airway-Provider, Vitals-Monitor.

**Publication**: "Vision-language Models for Decoding Provider Attention During Neonatal Resuscitation" - CVPR Workshops 2024

## Architecture

The pipeline consists of:
1. **Gaze Detection**: Find greenest pixel in frame (eye-tracker overlay indicator)
2. **Cropping**: Extract 128x128 region around detected gaze point
3. **Classification**: Run through trained model (MobileViT, ResNet50, or ViT)
4. **Output**: JSON predictions with class probabilities per frame

Key architectural decisions:
- Uses OpenMMLab's **mmpretrain** framework for model training/inference
- Configs use MMPreTrain's Python dict format with inheritance
- Zero-shot approach uses CLIP vision-language models
- Fine-tuned models achieve >98% accuracy (MobileViT best: 93% top-1, 98.7% top-3)

## Commands

### Environment Setup
```bash
conda env create -f docs/neogaze_supp/environment.yml
conda activate openmmlab
```

### Training
```bash
bash src/dist_train.sh configs/<config>.py <num_gpus> <work_dir> [--amp]
# Example:
bash src/dist_train.sh configs/mobilevit-small_8xb128_in1k_singleclass.py 1 results/mobilevit/
```

### Testing
```bash
bash src/dist_test.sh configs/<config>.py <checkpoint.pth> <num_gpus> <work_dir>
```

### Video Inference
```bash
python src/video_demo.py <video_path> <config_path> --checkpoint <checkpoint.pth> --device cuda:0
```

## Key Files

- `src/video_demo.py` - Main inference script with `get_greenest_pixel()` for gaze detection
- `configs/` - Model configs (mobilevit, resnet50, vit) using MMPreTrain format
- `notebooks/NG-2-SegmentAnything.ipynb` - MobileSAM segmentation pipeline
- `notebooks/NG-3-ZeroShotGazeClassify.ipynb` - CLIP zero-shot classification

## Dependencies

Core: PyTorch 2.0.1, CUDA 11.7, mmpretrain, mmcv 2.0.1, mmengine 0.8.4, transformers 4.33.1

## Data Format

- Training data uses MMPreTrain's CustomDataset format
- Split files: `train_full.txt`, `val_full.txt` in `data/`
- Annotations originally created with DeepEthogram GUI

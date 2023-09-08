# NeoGaze Model Gaze Classification Results

### Zero-Shot Classification by OpenCLIP Laion-ViT-B-32
| Model | InputType | Top-1 (%) | Top-3 (%) | Crop-Radius | Weights | 
| :---: | :-------: | :-------: | :-------: | :---------: | :-----: |
| OpenCLIP-ViT-B-32 | Crop | 36.93 | 62.22 | 128 | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |
| OpenCLIP-ViT-B-32 | Crop | 37.92 | 49.39 | 256 | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) | 
| OpenCLIP-ViT-B-32 | Mask | 23.15  | 53.67 | NA | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |
| OpenCLIP-ViT-B-32 | Crop + Mask | 37.92 | 76.10 | 128 | NA | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |

### EIRD Fine-Tuned Gaze Classification
| Model | Top-1 (%) | Top-3 (%) | Inference Time (FPS) | Params (M) | Flops (G) | Weights | 
| :---: | :-------: | :-------: | :------------------: | :-----: | :-----: | :-----: | 
| ResNet50 | 82.98 | 96.53 | ... | 25.56 | 4.12 | [G-Drive](https://drive.google.com/file/d/1whnjqlWjwo6pbBEbitgg1MAeaZE_juZf/view?usp=drive_link) |
| MobileViT |  93.02 | 98.74 | ... | 5.58 | 2.03 | [G-Drive](https://drive.google.com/file/d/1V2Za-HmDx-chUBovKvfAr_67s6D1_GTo/view?usp=drive_link) |
| OpenCLIP-ViT-B-32 | 87.51 | 97.21 | 3.2 | 86.57 | 16.86 | ... |

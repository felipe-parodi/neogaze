# NeoGaze Model Gaze Classification Results

### Zero-Shot Classification by OpenCLIP Laion-ViT-B-32
| Model | InputType | Top1 | Top3-Strict | Top3-Flex | Crop-Radius | Weights | 
| :-------: | :--: | :---------: | :-------: | :----: | :----: | :----: |
| OpenCLIP-ViT-B-32 | Crop      | 36.93% | 62.22%     | 82.21%   | 128    | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |
| OpenCLIP-ViT-B-32 | Crop      | 37.92% | 49.39%     | 72.49%   | 256    | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) | 
| OpenCLIP-ViT-B-32 | Mask      | 23.15%  | 53.67%     | 60.08%  | NA      | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |
| OpenCLIP-ViT-B-32 | Crop + Mask      | ...  | ...     | ...  | NA      | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |

### EIRD Fine-Tuned Gaze Classification
| Model | Top-1 (%) | Top-3 (%) | Inference Time (FPS) | Params (M) | Flops (G) | Weights | 
| :---: | :-------: | :-------: | :------------------: | :-----: | :-----: | :-----: | 
| ResNet50 | 82.98 | 96.53 | ... | 25.56 | 4.12 | [G-Drive](https://drive.google.com/file/d/1whnjqlWjwo6pbBEbitgg1MAeaZE_juZf/view?usp=drive_link) |
| MobileViT |  93.02 | 98.74 | ... | 5.58 | 2.03 | [G-Drive](https://drive.google.com/file/d/1V2Za-HmDx-chUBovKvfAr_67s6D1_GTo/view?usp=drive_link) |
| OpenCLIP-ViT-B-32 | ... | ... | 3.2 | 86.57 | 16.86 | ... |

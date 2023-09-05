# NeoGaze Model Gaze Classification Results

### Zero-Shot Classification by OpenCLIP Laion-ViT-B-32
| Model | InputType | Top1 | Top3-Strict | Top3-Flex | Crop-Radius | Weights | 
| :-------: | :--: | :---------: | :-------: | :----: | :----: | :----: |
| OpenCLIP-ViT-B-32 | Crop      | 36.93% | 62.22%     | 82.21%   | 128    | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |
| OpenCLIP-ViT-B-32 | Crop      | 37.92% | 49.39%     | 72.49%   | 256    | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) | 
| OpenCLIP-ViT-B-32 | Mask      | 23.15%  | 53.67%     | 60.08%  | NA      | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |
| OpenCLIP-ViT-B-32 | Crop Mask      | ...  | ...     | ...  | NA      | [HuggingFace](https://huggingface.co/laion/CLIP-ViT-B-32-DataComp.M-s128M-b4K) |

### EIRD Fine-Tuned Gaze Classification
| Model | InputType | Top1 | Top3-Strict | Top3-Flex | Crop=Radius | Inference Time (FPS) | Weights | 
| :---: | :-------: | :--: | :---------: | :-------: | :----: | :------------------: | :-----: | 
| ResNet50 | ... | ... | ... | ... | 128 | ... | ... |
| ViT   | ... | ... | ... | ... | 128 | ... | ... |
| FastViT| ... | ... | ... | ... | 128 | ... | ... |
| OpenCLIP-ViT-B-32 |  ... | ... | ... | ... | 128 | 3.2 | ... |
| OpenCLIP-ViT-L-32 | ... | ... | ... | ... | 128 | ... | ... |

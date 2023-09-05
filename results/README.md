# NeoGaze Model Gaze Classification Results

### Zero-Shot Classification by OpenCLIP Laion-ViT-B-32
| InputType | Top1 | Top3-Strict | Top3-Flex | Radius |
| :-------: | :--: | :---------: | :-------: | :----: |
| Crop      | 36.93% | 62.22%     | 82.21%   | 128    |
| Crop      | 37.92% | 49.39%     | 72.49%   | 256    |
| Mask      | 23.15%  | 53.67%     | 60.08%  | NA      |

### Fine-Tuned Classification on EIRD
| Model | InputType | Top1 | Top3-Strict | Top3-Flex | Radius | Inference Time (FPS)
| :---: | :-------: | :--: | :---------: | :-------: | :----: | :------------: |
| ResNet50 | ... | ... | ... | ... | ... | ... |
| ViT   | ... | ... | ... | ... | ... | ... |
| FastViT| ... | ... | ... | ... | ... | ... |
| OpenCLIP-ViT-B-32 |  ... | ... | ... | ... | ... | 3.2 |
| OpenCLIP-ViT-L-32 | ... | ... | ... | ... | ... | ... |

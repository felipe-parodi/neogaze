# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser
import cv2
import numpy as np
from mmengine.fileio import dump
from rich import print_json

from mmpretrain.apis import ImageClassificationInferencer

RADIUS = 128

def get_greenest_pixel(image_array):
    green = image_array[:,:,1] - image_array.mean(axis=2)
    argmax2d_green = np.unravel_index(np.argmax(green), green.shape)
    return np.array([argmax2d_green[1], argmax2d_green[0]])

def subset_image_around_centroid(image_array, radius):
    greenest_point = get_greenest_pixel(image_array)
    y,x = greenest_point
    cropped_image = image_array[max(0, x - radius): min(image_array.shape[0], x + radius), 
                                max(0, y - radius): min(image_array.shape[1], y + radius)]
    return cropped_image

def main():
    parser = ArgumentParser()
    parser.add_argument('video', help='Video file')
    parser.add_argument('model', help='Model name or config file path')
    parser.add_argument('--checkpoint', help='Checkpoint file path.')
#     parser.add_argument(
#         '--show',
#         action='store_true',
#         help='Whether to show the prediction result in a window.')
    parser.add_argument(
        '--show-dir',
        type=str,
        help='The directory to save the visualization image.')
    parser.add_argument('--device', help='Device used for inference')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file

#     python video_demo.py /mmpose/fparodi/neogaeo_demo.py /mmpose/fparodi/neogaze/configs/mobilevit-small_8xb128_in1pose/fpaogaze/rmultilabels_fromsk.py /mmpose/fparodi/neogaze/results/mobilevit_multilabels_fromscratclti-labe.pth --hwithbce/best_multi-label_mAP_epoch_88.pth --device cuda:0
    
#     model = 'mobilevit-small_8xb128_in1k.py'
    try:
        pretrained = args.checkpoint or True
        inferencer = ImageClassificationInferencer(
            args.model, pretrained=pretrained)
    except ValueError:
        raise ValueError(
            f'Unavailable model "{args.model}", you can specify find a model '
            'name or a config file or find a model name from '
            'https://mmpretrain.readthedocs.io/en/latest/modelzoo_statistics.html#all-checkpoints'  # noqa: E501
        )

    cap = cv2.VideoCapture(args.video)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cropped_frame = subset_image_around_centroid(frame, RADIUS)
        if cropped_frame.size == 0:
            continue

        result = inferencer(cropped_frame)[0]
        print_json(dump(result, file_format='json', indent=4))

#         if args.show:
#             cv2.imshow('Frame', frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

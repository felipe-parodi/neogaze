# Decoding Physician Visual Attention During Neonatal Resuscitation

### Abstract
Neonatal resuscitations are highly complex, requiring physicians to remain calm and attentive while processing multiple information streams. To drive targeted interventions for physician training and real-time decision support, continuous monitoring of gaze sequences by physicians is critical but remains challenging. Current approaches relying on manual gaze coding or simulated scenarios have limited scalability and ecological validity in real neonatal intensive care units (NICUs). Here, we introduce an automated deep learning-based method that decodes physician gaze directly from egocentric, first-person point-of-view data captured during live resuscitations. Without training, our zero-shot pipeline combines state-of-the-art real-time segmentation with vision-language networks to achieve 76% classification accuracy for gaze targets without training. Following minimal fine-tuning with fewer than 1,000 images, gaze classification accuracy exceeds 90%, approaching the precision observed in human observers. This system enables objective, scalable quantification of physician attention dynamics during live neonatal care. Our approach to automated gaze analysis in the NICU paves the way for enhancing the understanding of clinical decision-making and showcases a scalable approach that can integrate with existing systems for real-time analysis and optimization.

### Gaze Classes
| Class ID | Class Name |
| :------: | :--------: |
| 0 | Airway-Equipment |
| 1 | CMAC-Screen |
| 2 | Infant |
| 3 | Non-Team-Member |
| 4 | Other-Physical-Objects |
| 5 | Airway-Provider | 
| 6 | Vitals-Monitor |

### Repository Contents
/configs   --> Configuration files for each deep learning model. </br>
/data      --> Example annotation files for testing. </br>
/notebooks --> Jupyter Notebooks for data preprocessing and model testing. </br>
/results   --> Results and figures. </br>
/src       --> Helper functions and source code. </br>

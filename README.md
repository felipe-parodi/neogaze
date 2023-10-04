# Decoding Physician Visual Attention During Neonatal Resuscitation

### Abstract
Neonatal resuscitations demand an exceptional level of attentiveness and composure from physicians, who must process multiple streams of information simultaneously. For more targeted physician training and enhanced real-time decision support, a system capable of continuous monitoring of gaze patterns is essential. Current approaches rely on manual gaze coding or simulated environments, and therefore fall short in offering scalability. For this reason, there is no solution yet applicable for rapid, robust gaze classification in real-world neonatal intensive care units (NICUs). Here, we introduce an automated real-time deep learning approach capable of decoding physician gaze into semantic classes, directly from first-person point-of-view data recorded during live resuscitations. Combining state-of-the-art real-time segmentation with vision-language networks, our zero-shot pipeline attains a remarkable 76\% classification accuracy in identifying gaze targets, even without prior training. Upon minimal fine-tuning, the performance of our gaze-guided vision transformer exceeds 98\% accuracy in real-time gaze classification, approaching human-level precision. This system, capable of real-time inference, enables objective, scalable quantification of physician attention dynamics during live neonatal care. Our approach not only opens avenues for a deeper understanding of clinical decision-making processes but also exemplifies a scalable solution that seamlessly integrates with existing infrastructures for real-time analysis and optimization.

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
| Directory  | Description                                                       |
|------------|-------------------------------------------------------------------|
| _/configs_ | Configuration files for each deep learning model.                 |
| _/data_    | Example annotation files for testing.                             |
| _/notebooks_ | Jupyter Notebooks for data preprocessing and model testing.   |
| _/results_ | Results and figures.                                              |
| _/src_     | Helper functions and source code.                                 |

[Link to paper](https://docs.google.com/document/d/1PDUD8o4m2I60d2R2R8J5qVvWJAIlWw9LEQGdPxiIJv4/edit#heading=h.e8kd2lcjikdm)

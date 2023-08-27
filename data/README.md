# NeoGaze Dataset

### Overview
NeoGaze is a sparse dataset consisting of 20,405 first-person Point-Of-View (POV) frames featuring clinicians performing neonatal resuscitation procedures. Each frame within the clips is categorized into one of 11 pre-defined Areas of Interest (AOIs).

### Categories

Frames are sorted into the following 11 AOIs:

1. Patient (Infant): Includes any equipment or hands touching the infant.
2. Monitor: Vital signs monitor.
3. Video Laryngoscope Screen: CMAC screen.
4. Airway Equipment: Includes Endotracheal Tube (ETT), Stylet, Laryngoscope, CMAC blade, Mask, Pedicap, and suction catheter.
5. Airway Provider / Intubator: Team member actively involved in airway management.
6. Other Intubators (OI): Team members physically involved in resuscitation but not in airway management.
7. Non-Intubator (NI): Present in frame but not involved in any part of resuscitation.
8. Other Physical Objects (OPO): Any other object not included in the pre-defined AOIs.

### Terminology

- Gaze Point: A single eye-tracking data point for 1 frame.
- Fixation: Three or more sequential gaze points that fall within the same AOI.
- Saccade: Two or fewer consecutive gaze points when changing focus.
- AOI Border: A 2-inch region surrounding each object categorized as an AOI.

### Criteria for Classification

1. A gaze is only considered if it lasts more than 3 frames.
2. Fixations on team members’ hands above the infant are mapped onto the infant.
3. Saccades that fall within an AOI are mapped as such.
4. Gaze points within a 2-inch border around an AOI are mapped to that AOI.
5. In case of AOI overlap within the 2-inch border, the gaze point is mapped to the closest AOI.

### Special Considerations

- Airway Equipment: If looking at the distal end of the suction catheter while its proximal end is in the infant, it is classified as equipment.
- Team Members: Includes Leader, Bedside RN, HR person, RT, Recording RN.
- Non-team members: Consists of other observers and providers placing lines.

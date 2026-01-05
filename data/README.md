# NeoGaze Data

Training data uses MMPretrain's CustomDataset format with annotation files.

**Note:** Raw video data is not released due to privacy concerns (contains identifiable patient/clinician information).

## Format

- `train_full.txt` / `val_full.txt`: Annotation files mapping images to class labels
- Images organized by class in `all_data/` subdirectory

## Classes (7)

1. Airway-Equipment
2. CMAC-Screen
3. Infant
4. Non-Team-Member
5. Other-Physical-Objects
6. Airway-Provider
7. Vitals-Monitor

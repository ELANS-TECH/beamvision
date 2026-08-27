# Training plan (Windows)

Models: YOLO11n (web/fast) and YOLO11s (native/accurate). Input 640×384. Lane model decided after detector is solid.

1. Install Ultralytics + CUDA PyTorch; verify GPU.
2. Download BDD100K; convert to YOLO format with the 14-class mapping.
3. Train n and s, 150 epochs, mosaic + night/rain augmentation. Target ≥0.5 mAP50 on person/car/truck at night.
4. Relabel truck sub-types; fine-tune on own footage.
5. Export: ONNX (web), CoreML FP16 (iOS), TFLite (Android). Exports live outside git (see .gitignore); attach to GitHub Releases.
6. Benchmark exports in the phone browser using web/beamvision-cam.html.

Timeline: week 1 setup + BDD training, week 2 own footage + fine-tune, week 3 export + benchmarks.

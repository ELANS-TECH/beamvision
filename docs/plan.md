# Build plan

## Product
Tesla-style live drive visualization for any car, plus a dashcam. 3D view is the hero; camera feed is an inset.

## Architecture
- Single HTML app: Three.js scene, HUD, tracker, recording UI.
- Detection module returns `[{class, score, box}]` and is swappable:
  - Web: MediaPipe (now) → ONNX Runtime Web + custom YOLO11n (WebGPU).
  - Native: Capacitor plugin → Apple Vision/CoreML (iOS), TFLite (Android). Boxes sent to the webview as JSON.
- `camera-preview` plugin for the feed and recording.
- Tracker: low-gain prediction filter, lane-centre bias, outlier gate, rate-limited render position.

## Order
1. Drive-view look and feel (done: models, PBR, bloom, road).
2. Camera test build with stock model (done).
3. Train custom model (see training-plan.md), export ONNX/CoreML/TFLite.
4. Native detection plugin (iOS when the Mac arrives; Android on Windows).
5. Dashcam: rolling buffer, one-tap incident save, timestamp burn-in, incident PDF report.
6. Trip summary, parking mode, driver-cam (front camera drowsiness / phone use).
7. Pro tier via RevenueCat; App Store + Play submission.

## Differentiators vs existing apps
Full 3D view as the main screen, Android support, insurance-grade incident export, no-watermark free tier, cleaner glanceable UI, optional OBD-II later.

## Identity
Name: Beam Vision. Subtitle: AI Drive View & Dashcam. Bundle ID: com.elanstech.beamvision. Signature: headlight beam sweeping detected objects.

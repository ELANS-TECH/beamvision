# Beam Vision

AI drive view and dashcam for iPhone and Android, by Elans Gaming Studios.
Mount your phone on the windshield and your ordinary car gets a live 3D driver-assist display: your car on a virtual road, surrounding vehicles, cyclists and pedestrians placed by real distance estimation, traffic-light state, speed and heading — with the dashcam recording underneath.

## Status
Prototype. See `docs/plan.md` for the build order.

| File | What it is |
|---|---|
| `web/beamvision.html` | 3D drive-view prototype fed by a scripted scenario |
| `web/beamvision-cam.html` | Camera test build: live detection (MediaPipe EfficientDet-Lite0) driving the 3D view |

Both are single self-contained HTML files. Open over HTTPS (GitHub Pages) for camera access.

## Stack
Single-file HTML + Three.js r128 (inlined), Capacitor 6, Codemagic CI, on-device detection (MediaPipe / ONNX Runtime Web on the web layer, CoreML / TFLite via native plugins).

## Credits
Vehicle models: [Kenney Car Kit](https://kenney.nl) (CC0).

## License
Source code © Elans Gaming Studios. All rights reserved.

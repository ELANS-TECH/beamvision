# Detection classes (v1)

Detection (12): person, bicycle, motorcycle, car, van, truck, semi-truck, bus, traffic light, stop sign, speed-limit sign, cone.
State heads: traffic-light colour (red / amber / green); lane lines (segmentation).

Sources: BDD100K (bulk), Mapillary Traffic Sign (speed limits), COCO subset (cones, people, bikes), own dashcam footage (~500 labelled frames).
BDD "truck" is split into van / truck / semi-truck by relabeling ~2k crops.

Each class maps to a 3D asset in the app: sedan/SUV, van, truck, semi rig, bus, motorcycle, bicycle, pedestrian, light pole, stop sign, speed sign with number, cone, lane ribbons.

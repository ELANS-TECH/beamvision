"""Patch dfine_n_beamvision.onnx so no EXTERNAL tensor is int64.

ONNX Runtime Web's WebGPU EP fails OrtRun() on int64 graph inputs/outputs
(tensor_shape.cc int64_t). D-FINE exports `orig_target_sizes` (input) and
`labels` (output) as int64. We change both to int32 at the boundary and insert
Cast nodes inside the graph, so the model's internals are untouched.

Usage (from training/, venv active):
    python patch_onnx_int32.py                       # patches model/dfine_n_beamvision.onnx in place
    python patch_onnx_int32.py ..\\web\\models\\dfine_n_beamvision.onnx

Idempotent: running it on an already-patched model is a no-op.
Run export_dfine.py first when deploying a new checkpoint, then this, then copy to web/models/.
"""
import sys
import onnx
from onnx import helper, TensorProto

src = sys.argv[1] if len(sys.argv) > 1 else 'model/dfine_n_beamvision.onnx'
m = onnx.load(src)
g = m.graph
changed = False

# --- input: orig_target_sizes int64 -> int32 (+ Cast to int64 inside) ---
for inp in g.input:
    if inp.name == 'orig_target_sizes' and inp.type.tensor_type.elem_type == TensorProto.INT64:
        inner = inp.name + '_i64'
        for n in g.node:
            for i, x in enumerate(n.input):
                if x == inp.name:
                    n.input[i] = inner
        g.node.insert(0, helper.make_node('Cast', [inp.name], [inner], to=TensorProto.INT64, name='bv_cast_sizes_i64'))
        inp.type.tensor_type.elem_type = TensorProto.INT32
        changed = True
        print('input  orig_target_sizes: int64 -> int32')

# --- output: labels int64 -> int32 (Cast at the end) ---
for out in g.output:
    if out.name == 'labels' and out.type.tensor_type.elem_type == TensorProto.INT64:
        inner = out.name + '_i64'
        for n in g.node:
            for i, x in enumerate(n.output):
                if x == out.name:
                    n.output[i] = inner
        g.node.append(helper.make_node('Cast', [inner], [out.name], to=TensorProto.INT32, name='bv_cast_labels_i32'))
        out.type.tensor_type.elem_type = TensorProto.INT32
        changed = True
        print('output labels: int64 -> int32')

if not changed:
    print('already patched — nothing to do')
    sys.exit(0)

onnx.checker.check_model(m)
onnx.save(m, src)
print('patched', src)

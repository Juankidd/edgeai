import onnxruntime as ort
import numpy as np

# Cargar modelo ONNX
session = ort.InferenceSession("lechuga_model.onnx")
input_name = session.get_inputs()[0].name

# Entrada: temperatura y humedad
input_data = np.array([[22.5, 65.0]], dtype=np.float32)
inputs = {input_name: input_data}

# Inferencia
outputs = session.run(None, inputs)
print("Producción estimada de lechuga (kg):", outputs[0][0][0])

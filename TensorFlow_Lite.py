import tensorflow as tf
import numpy as np

# Cargar modelo TFLite
interpreter = tf.lite.Interpreter(model_path="lechuga_model.tflite")
interpreter.allocate_tensors()

# Obtener detalles de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Simular entrada: temperatura y humedad
input_data = np.array([[22.5, 65.0]], dtype=np.float32)

# Ejecutar inferencia
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Obtener resultado
output_data = interpreter.get_tensor(output_details[0]['index'])
print("Producción estimada de lechuga (kg):", output_data[0][0])

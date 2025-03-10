# Esta plantilla requiere modelo precompilado con TVM
import tvm
from tvm import runtime
import numpy as np

# Cargar módulo
loaded_lib = tvm.runtime.load_module("lechuga_deploy_lib.tar")
dev = tvm.cpu()
module = tvm.contrib.graph_executor.GraphModule(loaded_lib["default"](dev))

# Entrada: temperatura y humedad
input_data = np.array([[22.5, 65.0]], dtype="float32")
module.set_input("input", input_data)
module.run()

# Salida
output = module.get_output(0).numpy()
print("Producción estimada de lechuga (kg):", output[0][0])

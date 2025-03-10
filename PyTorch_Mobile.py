import torch

# Cargar modelo TorchScript
model = torch.jit.load("lechuga_model_script.pt")
model.eval()

# Entrada: temperatura y humedad
input_tensor = torch.tensor([[22.5, 65.0]])

# Inferencia
with torch.no_grad():
    output = model(input_tensor)

print("Producción estimada de lechuga (kg):", output[0][0].item())

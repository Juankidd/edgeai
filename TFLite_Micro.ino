#include "model_data.h" // modelo .h generado
#include "tensorflow/lite/micro/micro_interpreter.h"

// ... configuración de memoria e intérprete

float input[] = {22.5f, 65.0f}; // temperatura, humedad
float output[1];

// Suponiendo inicialización del modelo y setup ya realizados
interpreter->set_input_tensor(0, input);
interpreter->Invoke();
interpreter->get_output_tensor(0, output);

Serial.print("Producción estimada de lechuga (kg): ");
Serial.println(output[0]);

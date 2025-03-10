#include "lechuga_model.h"

int main() {
    float input[2] = {22.5, 65.0};
    float output[1];

    model_run(input, output);
    printf("Producción estimada de lechuga (kg): %f\n", output[0]);
    return 0;
}

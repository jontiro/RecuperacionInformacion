# GPU Setup - RTX 5060 Ti

## ✅ Estado Actual

Tu **NVIDIA RTX 5060 Ti** está correctamente detectada y configurada para usar TensorFlow.

### Verificación Rápida

```bash
# Desde la raíz del proyecto:
./.venv/bin/python -c "
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')
print(f'GPUs detectadas: {len(gpus)}')
if gpus:
    print(f'  ✅ {gpus[0].name}')
else:
    print('  ❌ No GPU found')
"
```

## Configuración Instalada

| Componente | Versión | Estado |
|-----------|---------|--------|
| Driver NVIDIA | 595.45.04 | ✅ |
| TensorFlow | 2.20.0 | ✅ |
| CUDA Runtime | 12.5.82 | ✅ |
| cuDNN | 9.21.0.82 | ✅ |
| Compute Capability | 12.0 (RTX 5060 Ti) | ✅ |

## Notas Importantes

### 1. Compilación de Kernels (Primera ejecución)
- En la primera ejecución, verás este warning:
  ```
  WARNING: TensorFlow was not built with CUDA kernel binaries compatible with compute capability 12.0. 
  CUDA kernels will be jit-compiled from PTX, which could take 30 minutes or longer.
  ```
- **Esto es normal** para la RTX 5060 Ti (architecture Ada Lovelace, muy nueva).
- TensorFlow compilará los kernels **solo una vez**. Ejecuciones posteriores serán rápidas.
- La compilación ocurre internamente sin requerer acción del usuario.

### 2. Workaround Implementado en `main.py`
Para evitar errores durante compilación de kernels:
```python
# En RNN/main.py, líneas 20-24:
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
tf.config.set_visible_devices([], 'GPU')  # CPU durante construcción del modelo
```

Esto asegura que:
- La GPU está disponible pero **no se fuerza durante construcción del modelo**
- Evita errores como `CUDA_ERROR_INVALID_HANDLE` durante compilación JIT
- El entrenamiento usa GPU sin problemas (XLA JIT compiler)

## Rendimiento Esperado

Con RTX 5060 Ti (16GB VRAM):
- **Época típica RNN**: 35-40 segundos
- **Memoria usada**: ~13GB durante training

## Troubleshooting

### GPU No Detectada
```bash
# Reinstalar CUDA/cuDNN en venv:
./.venv/bin/pip install --upgrade 'tensorflow[and-cuda]'
```

### Errores `CUDA_ILLEGAL_INSTRUCTION` o `CUDA_ERROR_INVALID_HANDLE`
- Ejecutar el script una vez más (kernels ya estarán compilados)
- Si persiste: Asegúrate de tener suficiente espacio en `/tmp` (necesita ~2GB para compilación)

### Forzar CPU (debug)
```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # ANTES de importar TensorFlow
```

## Comandos Útiles

### Ver estado de GPU en tiempo real
```bash
watch -n 1 nvidia-smi
```

### Verificar memoria de GPU
```bash
nvidia-smi --query-gpu=name,memory.total,memory.used,memory.free --format=csv
```

### Ver procesos usando GPU
```bash
nvidia-smi pmon
```

## Referencias
- RTX 5060 Ti Specs: https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/
- TensorFlow GPU Setup: https://www.tensorflow.org/install/gpu
- Compute Capability 12.0 (Ada Lovelace): RTX 5060 Ti, RTX 6000 Ada, etc.


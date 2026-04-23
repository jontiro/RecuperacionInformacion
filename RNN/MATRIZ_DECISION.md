# 🎯 MATRIX DE DECISIÓN: Diagnosis y Acción

## ¿Cuál es Tu Situación?

Responde las preguntas para encontrar la solución:

---

## PREGUNTA 1: ¿Cómo se ve tu accuracy?

### Opción A: Baja consistentemente cada época
```
Epoch 1: 0.92
Epoch 2: 0.90 ↓
Epoch 3: 0.87 ↓
Epoch 4: 0.83 ↓↓
```
**→ OVERFITTING SEVERO**
- Ve: TROUBLESHOOTING.md → Scenario 1
- Soluciones rápidas: Aumentar Dropout → Aumentar L2 → Reducir LR

---

### Opción B: Sube al principio, luego baja
```
Epoch 1: 0.88
Epoch 2: 0.90 ↑
Epoch 3: 0.91 ↑
Epoch 4: 0.89 ↓ (Early Stop)
```
**→ OVERFITTING LEVE** ✓ Esperado
- Esto es NORMAL con Early Stopping
- Tu modelo se detiene en el mejor punto
- NO necesitas cambios

---

### Opción C: Se queda en 0.50
```
Epoch 1: 0.50
Epoch 2: 0.50
Epoch 3: 0.50
```
**→ MODELO NO ENTRENA**
- Ve: TROUBLESHOOTING.md → Scenario 4
- Verificar: datos etiquetados, learning rate, arquitectura

---

### Opción D: Oscila mucho
```
Epoch 1: 0.92
Epoch 2: 0.88
Epoch 3: 0.91
Epoch 4: 0.87
```
**→ GRADIENTES RUIDOSOS**
- Problema: Batch size pequeño
- Solución: Aumentar batch_size a 64

---

## PREGUNTA 2: ¿Cuánto dura cada época?

### < 1 minuto
✅ Perfecto, no cambiar

### 1-5 minutos
✅ Normal, aceptable

### 5-10 minutos
⚠️ Algo lento, considera:
- Reducir vocab_size: 5000 → 2000
- Reducir max_len si es muy grande
- Ver TROUBLESHOOTING.md → Scenario 2

### > 10 minutos
🔴 Muy lento, acciones requeridas:
- Aumentar batch_size: 32 → 64 o 128
- Reducir embedding dims: 16 → 8
- Reducir vocab: 5000 → 2000

---

## PREGUNTA 3: ¿Cuál es tu validación accuracy?

### Val Acc ≈ Train Acc (diferencia < 0.02)
```
Train Acc: 0.92
Val Acc:   0.91  (diferencia 0.01)
```
✅ PERFECTO - Modelo generaliza bien
- No hacer cambios
- Dejar que Early Stop termine naturalmente

---

### Val Acc << Train Acc (diferencia > 0.05)
```
Train Acc: 0.92
Val Acc:   0.87  (diferencia 0.05)
```
⚠️ OVERFITTING - Acciones:
1. Aumentar Dropout: 0.3 → 0.5
2. Aumentar L2: 0.001 → 0.01
3. Si aún persiste, reducir complejidad
- Ve: TROUBLESHOOTING.md → Scenario 3

---

### Val Acc > Train Acc (muy raro)
```
Train Acc: 0.88
Val Acc:   0.92
```
🔍 Investigar:
- Posible desbalance de datos
- Posible leak de información
- Revisar estratificación en train_test_split

---

## PREGUNTA 4: ¿Se activa Early Stopping?

### Sí (ves "Early stopping" en salida)
✅ CORRECTO
- El modelo se detiene en óptimo
- Usa pesos del mejor epoch
- Esto es lo esperado

### No (entrena las 30 épocas completas)
⚠️ Podría significar:
1. La validación no mejora suficientemente
   - Aumentar patience: 3 → 5
2. La métrica es muy inestable
   - Reducir learning rate
3. El monitor es incorrecto
   - Verificar: `monitor='val_loss'`

---

## PREGUNTA 5: ¿Cuál es tu Test Accuracy?

### > 0.90
✅ EXCELENTE
- Tu modelo generaliza bien
- Test set es representativo
- ¡Éxito! No cambiar nada

### 0.85-0.90
✅ BUENO
- Modelo funciona bien
- Pequeñas mejoras son opcionales
- Considera pequeños ajustes si quieres exprimir

### 0.80-0.85
⚠️ REGULAR
- Modelo necesita mejoras
- Revisa TROUBLESHOOTING.md
- Intenta Scenario 1 soluciones

### < 0.80
🔴 BAJO
- Serios problemas
- Revisa: datos, arquitectura, entrenamiento
- Consulta TROUBLESHOOTING.md completo

---

## ÁRBOL DE DECISIÓN RÁPIDO

```
¿Accuracy baja cada época?
├─ Sí → ¿Diferencia (Train-Val) > 0.05?
│      ├─ Sí → Aumentar Dropout: 0.3→0.5
│      └─ No → Aumentar L2: 0.001→0.01
│
├─ No → ¿Se vuelve inestable?
│       ├─ Sí → Aumentar Batch Size: 32→64
│       └─ No → ✓ NORMAL, continuar
│
└─ Ni una ni otra → ¿Test Acc > 0.90?
                    ├─ Sí → ✓ ÉXITO, no cambiar
                    └─ No → Revisar datos y arquitectura
```

---

## MATRIZ DE SÍNTOMAS Y SOLUCIONES

| Síntoma | Causa Probable | Solución Rápida | Prioridad |
|---------|---|---|---|
| Acc baja 📉 | Overfitting | Dropout 0.3→0.5 | 🔴 Alta |
| Val << Train | Memorización | L2 0.001→0.01 | 🔴 Alta |
| Oscila mucho | Ruido gradientes | Batch 32→64 | 🟡 Media |
| Muy lento | Arquitectura pesada | Reducir vocab | 🟢 Baja |
| Acc = 0.50 | No entrena | Revisar datos | 🔴 Alta |
| No Early Stop | Val no mejora | Aumentar patience | 🟡 Media |
| CUDA error | Memoria GPU | Batch 32→16 | 🔴 Alta |
| Test << Val | Desbalance datos | Revisar split | 🟡 Media |

---

## PLAN DE ACCIÓN POR ESCENARIO

### ESCENARIO 1: Accuracy baja rápidamente (Como el tuyo)
```
PASO 1: Verificar que main.py tenga los últimos cambios
         → Si no, aplicar desde COMPARACION_ANTES_DESPUES.md

PASO 2: Ejecutar y observar 3 primeras épocas
         Epoch 1: Acc = ?
         Epoch 2: Acc = Epoch1 ± 0.01 (debe ser similar)
         Epoch 3: Acc = Epoch2 ± 0.01 (debe ser similar)

PASO 3: Si sigue bajando
         → Aumentar Dropout: 0.3 → 0.5 en todas partes
         → Ejecutar de nuevo

PASO 4: Si aún baja
         → Aumentar L2: 0.001 → 0.01
         → Ejecutar de nuevo

PASO 5: Si aún baja
         → Simplificar modelo (quitar un RNN layer)
         → Ejecutar de nuevo

RESULTADO: Accuracy debe estabilizarse ✓
```

---

### ESCENARIO 2: Accuracy está estable pero baja
```
PASO 1: Observar salida completa
        ¿Se ve "Early stopping"? 
        → Si sí: ÉXITO, es comportamiento esperado
        → Si no: aumentar patience

PASO 2: Comparar train vs val
        Diferencia < 0.02? → BUENO
        Diferencia > 0.05? → Aumentar Dropout

PASO 3: Verificar test accuracy
        > 0.90? → ÉXITO ✓
        < 0.85? → Revisar datos
```

---

### ESCENARIO 3: Todo funciona bien
```
Accuracy estable → ✓
Validation similar → ✓
Test accuracy > 0.90 → ✓
Early stop activado → ✓

🎉 ÉXITO TOTAL

Próximos pasos (opcionales):
- Experimento con hiperparámetros
- Probar diferentes arquitecturas
- Agregar más datos si es posible
```

---

## CHECKLIST PRE-EJECUCIÓN

```
VERIFICACIÓN TÉCNICA:
□ main.py tiene train/val split
□ main.py tiene EarlyStopping
□ main.py tiene Dropout(0.3)
□ main.py tiene kernel_regularizer=l2(0.001)
□ main.py tiene batch_size=32
□ main.py tiene validation_data=(X_val, y_val)

VERIFICACIÓN DE DATOS:
□ sentiment.csv existe y es accesible
□ Equal.csv existe y es accesible
□ Datos no tienen NaN críticos
□ Sentimientos son 'positive'/'negative'

VERIFICACIÓN DE AMBIENTE:
□ Python 3.8+
□ TensorFlow 2.10+
□ pandas, numpy, sklearn instalados
□ GPU disponible (opcional pero recomendado)
```

Si todo ✓, entonces ejecuta:
```bash
python3 main.py
```

---

## 🎯 RESUMEN

Tu problema: **Accuracy baja de 0.92 a 0.79 en 6 épocas**

Causa: **Overfitting por batch=4 + sin validación + sin regularización**

Solución: **6 cambios implementados** (ver main.py)

Resultado esperado: **Accuracy estable ~0.91, Early Stop ~época 6**

Verificación: **Test accuracy > 0.90**

---

✅ **¿Listo? Ejecuta:**
```bash
python3 main.py
```

**¿Problemas? Consulta:**
- TROUBLESHOOTING.md para scenarios específicos
- COMPARACION_ANTES_DESPUES.md para ver qué cambió
- SOLUCION_ACCURACY.md para teoría completa


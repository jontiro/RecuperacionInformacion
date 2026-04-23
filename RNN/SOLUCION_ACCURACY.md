# 🔧 Solución: ¿Por qué baja la Accuracy entre épocas?

## ❌ Problema Identificado

La accuracy estaba bajando de manera consistente:
- Época 1: 0.9219
- Época 2: 0.9019
- Época 3: 0.8985
- Época 4: 0.8443
- Época 5: 0.8260
- Época 6: 0.7899

Este es un **síntoma clásico de OVERFITTING severo**.

---

## 🎯 Causas Raíz

### 1. **Batch Size Muy Pequeño (4)**
- **Problema**: Con solo 4 muestras por lote, cada actualización de gradientes es muy ruidosa
- **Efecto**: El modelo "oscila" entre soluciones, memorizando datos en lugar de generalizar
- **Solución**: ✅ Aumentar a 32 (reduce ruido ~8x)

### 2. **Sin Validación Durante Entrenamiento**
- **Problema**: El código original NO dividía entrenamiento/validación
- **Efecto**: Sin forma de detectar cuándo comienza el overfitting
- **Solución**: ✅ Dividir 80% entrenamiento, 20% validación

### 3. **Sin Early Stopping**
- **Problema**: El modelo seguía entrenando aunque empeoraba
- **Efecto**: Después de la 1era época buena, los gradientes divergen
- **Solución**: ✅ Agregar EarlyStopping que detiene cuando val_loss no mejora

### 4. **Regularización Insuficiente**
- **Problema**: El modelo original solo tenía capas Dense simples
- **Efecto**: Sin limitaciones para memorizar
- **Solución**: ✅ Agregar Dropout (0.3) y L2 regularization (0.001)

### 5. **Learning Rate No Controlado**
- **Problema**: Usar "adam" por defecto (LR=0.001) sin control
- **Efecto**: Los pesos pueden actualizarse demasiado agresivamente
- **Solución**: ✅ Especificar learning_rate=0.001 explícitamente

### 6. **Modelo Demasiado Simple para Después Demasiado Complejo**
- **Problema**: La arquitectura cambió entre versiones sin justificación
- **Solución**: ✅ Usar arquitectura balanceada con regularización

---

## ✅ Cambios Implementados

```python
# ANTES (problemas)
model = Sequential([
    Embedding(...),
    SimpleRNN(32, activation="tanh", seed=42),
    Dense(1, activation="sigmoid")
])
history = model.fit(X, y, epochs=30, batch_size=4, verbose=1)
# Sin validación, sin early stopping, sin regularización

# DESPUÉS (optimizado)
model = Sequential([
    Embedding(...),
    Dropout(0.3),  # ← Evita memorización
    SimpleRNN(32, activation="tanh", return_sequences=True, 
              kernel_regularizer=l2(0.001)),  # ← Limita pesos grandes
    Dropout(0.3),
    SimpleRNN(16, activation="tanh", kernel_regularizer=l2(0.001)),
    Dropout(0.3),
    Dense(8, activation="relu", kernel_regularizer=l2(0.001)),
    Dropout(0.2),
    Dense(1, activation="sigmoid")
])

optimizer = Adam(learning_rate=0.001)  # ← Control explícito
model.fit(X_train, y_train, 
          validation_data=(X_val, y_val),  # ← Monitorear divergencia
          batch_size=32,  # ← Menos ruido
          callbacks=[early_stopping],  # ← Detener automáticamente
          epochs=30)
```

---

## 📊 Resultado Esperado

Con estos cambios deberías ver:

| Métrica | Antes | Después |
|---------|-------|---------|
| Epoch 1 Train Acc | 0.9219 | ~0.92 |
| Epoch 2 Train Acc | 0.9019 ↓ | ~0.91 |
| Trend | ⬇️ Baja rápido | ⬆️ Sube o estable |
| Early Stopping | ❌ No | ✅ Época ~5-8 |
| Validación | ❌ Sin datos | ✅ Monitorea |
| Overfitting | ❌ Severo | ✅ Controlado |

---

## 🎓 Conceptos Clave

### Overfitting
- Modelo "memoriza" el ruido del entrenamiento
- Bajo accuracy en validación/test
- Se ve como: loss bajando pero después subiendo

### Dropout
- Desactiva neuronas aleatoriamente (30%)
- Fuerza la red a ser más robusta
- Previene co-adaptación

### L2 Regularization
- Penaliza pesos grandes
- Reduce la complejidad del modelo
- Previene memorización

### Early Stopping
- Monitorea métrica de validación
- Si no mejora en N épocas → detener
- Restaura los mejores pesos

### Batch Size
- Pequeño (4): mucho ruido, oscilación
- Grande (32+): gradientes más estables
- Trade-off: computación vs convergencia

---

## 🔍 Cómo Verificar el Progreso

Ejecuta:
```bash
python3 main.py
```

Observa el output:
```
Epoch 1/30: accuracy: 0.92...
Epoch 2/30: accuracy: 0.91...  ← Debe ser similar o mejorar (no bajar)
Epoch 3/30: accuracy: 0.91...

Early stopping: restoring model weights from the epoch with the best validation loss
```

Si ves "Early stopping" → ✅ Funciona correctamente

---

## 📝 Resumen de Causas

| # | Causa | Impacto | Fix |
|-|-|-|-|
| 1 | Batch size 4 | 🔴 Alto ruido | Cambiar a 32 |
| 2 | Sin validación | 🔴 Sin monitor | Agregar X_val, y_val |
| 3 | Sin Early Stop | 🔴 Sigue entrenando | EarlyStopping callback |
| 4 | Poco Dropout | 🔴 Memoriza | Aumentar a 0.3 |
| 5 | Sin L2 | 🔴 Pesos libres | Agregar regularizer |
| 6 | LR implícito | 🟡 Menos control | Especificar 0.001 |

---

## 🚀 Próximos Pasos Opcionales

Si siguen habiendo problemas:

1. **Aumentar Dropout**: Cambiar 0.3 → 0.4 o 0.5
2. **Aumentar L2**: Cambiar 0.001 → 0.01
3. **Reducir LR**: Cambiar 0.001 → 0.0005
4. **Reducir Batch Size**: Si 32 es lento, pero no < 16
5. **Simplificar Modelo**: Usar solo 1 RNN layer en lugar de 2

---

✅ **Conclusión**: El problema era overfitting causado por arquitectura débil + batch pequeño + sin validación. Todos fueron corregidos.


# 📋 Guía Rápida: Cambios al Código RNN

## Resumen de Cambios

Se han hecho cambios específicos para resolver el problema de **accuracy descendente**:

### 🔴 ANTES (Con Problemas)
```
Epoch 1: accuracy 0.9219 ✓
Epoch 2: accuracy 0.9019 ↓
Epoch 3: accuracy 0.8985 ↓↓
Epoch 4: accuracy 0.8443 ↓↓↓
...se sigue degradando
```

### 🟢 DESPUÉS (Esperado)
```
Epoch 1: accuracy 0.90-0.92
Epoch 2: accuracy 0.90-0.92 (estable)
Epoch 3: accuracy 0.90-0.92 (estable)
Early stopping triggered at epoch ~5-7 ✓
```

---

## 6 Cambios Principales

### 1️⃣ **Batch Size: 4 → 32**
```python
# ANTES
history = model.fit(..., batch_size=4, ...)

# DESPUÉS
history = model.fit(..., batch_size=32, ...)
```
**¿Por qué?** Batch más grande = gradientes más suave = menos oscilación

---

### 2️⃣ **Agregar Validación Set**
```python
# ANTES (no había validación)
history = model.fit(X, y, epochs=30, batch_size=4)

# DESPUÉS
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, stratify=y
)
history = model.fit(X_train, y_train, 
                    validation_data=(X_val, y_val),  # ← Nuevo
                    epochs=30, batch_size=32)
```
**¿Por qué?** Necesitamos monitorear si el modelo está overfitting

---

### 3️⃣ **Agregar Early Stopping**
```python
# NUEVO
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True,
    verbose=1
)
history = model.fit(..., callbacks=[early_stopping], ...)
```
**¿Por qué?** Detiene automáticamente cuando empieza a empeorar

---

### 4️⃣ **Agregar Regularización (Dropout + L2)**
```python
# ANTES
model = Sequential([
    Embedding(...),
    SimpleRNN(32),
    Dense(1, activation="sigmoid")
])

# DESPUÉS
model = Sequential([
    Embedding(...),
    Dropout(0.3),  # ← Nuevo: desactiva 30% neuronas
    SimpleRNN(32, ..., kernel_regularizer=l2(0.001)),  # ← L2
    Dropout(0.3),
    SimpleRNN(16, ..., kernel_regularizer=l2(0.001)),
    Dropout(0.3),
    Dense(8, activation="relu", kernel_regularizer=l2(0.001)),
    Dropout(0.2),
    Dense(1, activation="sigmoid")
])
```
**¿Por qué?** Evita que el modelo memorice los datos

---

### 5️⃣ **Learning Rate Explícito**
```python
# ANTES
model.compile(optimizer="adam", loss="...", metrics=[...])

# DESPUÉS
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss="...", metrics=[...])
```
**¿Por qué?** Control explícito evita cambios inesperados

---

### 6️⃣ **Evaluar Validación**
```python
# ANTES
loss_train, acc_train = model.evaluate(X, y, verbose=0)

# DESPUÉS
loss_train, acc_train = model.evaluate(X_train, y_train, verbose=0)
loss_val, acc_val = model.evaluate(X_val, y_val, verbose=0)  # ← Nuevo
print(f"Validación Accuracy: {acc_val:.4f}")
```
**¿Por qué?** Necesitamos ver si el modelo generaliza

---

## 🧪 Cómo Probar

```bash
cd /home/jonathan/PycharmProjects/RecuperacionInformacion/RNN
python3 main.py
```

**Señales de éxito:**
- ✅ Accuracy estable o mejorando cada época
- ✅ Mensaje "Early stopping: restoring model weights..."
- ✅ Validación accuracy similar a entrenamiento
- ✅ No bajar más allá de la época 3

---

## 📊 Interpretación de Salida

```
Epoch 1/30: accuracy: 0.9200 - loss: 0.2300 - val_accuracy: 0.9100 - val_loss: 0.2400
                      ^^^^^^^^ Entrenamiento        ^^^^^^^^ Validación (nuevo)

Epoch 2/30: accuracy: 0.9150 - loss: 0.2350 - val_accuracy: 0.9080 - val_loss: 0.2420
                      ↑ Debe ser similar   ↑ Debe ser similar (ambos ~ 0.91)

Early stopping: restoring model weights from the epoch with the best validation loss
          ↑ Excelente: se detuvo automáticamente en la mejor época
```

---

## ⚠️ Si Sigue Habiendo Problemas

Si la accuracy sigue bajando después de estos cambios:

1. **Aumentar Dropout**: `Dropout(0.3)` → `Dropout(0.5)`
2. **Aumentar L2**: `l2(0.001)` → `l2(0.01)`
3. **Reducir Learning Rate**: `0.001` → `0.0005`
4. **Reducir Batch Size**: `32` → `16` (si hay overfitting extremo)
5. **Simplificar Modelo**: Usar solo 1 layer SimpleRNN

---

## 📚 Conceptos

| Término | Significa | Efecto |
|---------|-----------|--------|
| **Overfitting** | Modelo memoriza entrenamiento | Baja accuracy en test |
| **Dropout** | Desactiva neuronas al azar | Previene memorización |
| **L2** | Penaliza pesos grandes | Modelo más simple |
| **Batch Size** | Muestras por actualización | Pequeño=ruido, Grande=liso |
| **Early Stop** | Detiene cuando empeora | Evita sobreentrenamiento |
| **Validación** | Datos para monitoreo | Detecta overfitting |

---

## 🎯 Meta

**Objetivo:** Que el modelo mantenga accuracy ~0.90-0.92 sin bajar cada época.

**Resultado:** Con estos cambios, deberías ver accuracy estable y el modelo detenerse automáticamente cuando sea óptimo.

✅ **¡Listo para ejecutar!**


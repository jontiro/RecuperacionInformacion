# 🔧 TROUBLESHOOTING: Si Aún Hay Problemas

## Scenario 1: Accuracy SIGUE bajando

**Diagnóstico:**
```
Epoch 1: 0.92
Epoch 2: 0.91
Epoch 3: 0.89
Epoch 4: 0.86 ← PROBLEMA: sigue bajando
```

**Soluciones en orden de intentar:**

### 1️⃣ Aumentar Dropout
```python
# ACTUAL
Dropout(0.3)

# INTENTA
Dropout(0.5)  # Desactiva 50% en lugar de 30%
```
**Efecto**: Reduce memorización más agresivamente

### 2️⃣ Aumentar L2 Regularization
```python
# ACTUAL
kernel_regularizer=l2(0.001)

# INTENTA
kernel_regularizer=l2(0.01)  # 10x más fuerte
```
**Efecto**: Penaliza pesos grandes mucho más

### 3️⃣ Reducir Learning Rate
```python
# ACTUAL
optimizer = Adam(learning_rate=0.001)

# INTENTA
optimizer = Adam(learning_rate=0.0005)  # 50% más bajo
```
**Efecto**: Actualizaciones más conservadoras

### 4️⃣ Simplificar Modelo
```python
# ACTUAL (8 capas)
model = Sequential([
    Embedding(...),
    Dropout(0.3),
    SimpleRNN(32, return_sequences=True, kernel_regularizer=l2(0.001)),
    Dropout(0.3),
    SimpleRNN(16, kernel_regularizer=l2(0.001)),
    Dropout(0.3),
    Dense(8, activation="relu", kernel_regularizer=l2(0.001)),
    Dropout(0.2),
    Dense(1, activation="sigmoid")
])

# INTENTA (más simple - 5 capas)
model = Sequential([
    Embedding(...),
    Dropout(0.4),
    SimpleRNN(16, kernel_regularizer=l2(0.01)),  # Menos units
    Dropout(0.4),
    Dense(1, activation="sigmoid")
])
```
**Efecto**: Modelo más simple = menos overfitting

### 5️⃣ Aumentar paciencia de Early Stopping
```python
# ACTUAL
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True,
    verbose=1
)

# INTENTA si es muy agresivo
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5,  # Esperar 5 épocas en lugar de 3
    restore_best_weights=True,
    verbose=1
)
```
**Efecto**: Más tolerancia antes de detener

---

## Scenario 2: Entrenamiento muy lento

**Diagnóstico:**
```
Cada época tarda 10+ minutos
```

**Soluciones:**

### Opción A: Aumentar Batch Size
```python
# ACTUAL
batch_size=32

# INTENTA
batch_size=64  # Si GPU lo permite
```

### Opción B: Reducir Dimensión de Embedding
```python
# ACTUAL
Embedding(input_dim=vocab_size, output_dim=16)

# INTENTA
Embedding(input_dim=vocab_size, output_dim=8)  # Menos dims
```

### Opción C: Reducir Vocab Size
```python
# ACTUAL
tokenizer = Tokenizer(num_words=5000)

# INTENTA
tokenizer = Tokenizer(num_words=2000)  # Menos palabras
```

---

## Scenario 3: Validation accuracy muy diferente de Train

**Diagnóstico:**
```
Train Acc:  0.95
Val Acc:    0.80  ← Demasiada diferencia
```

**Soluciones:**

### 1️⃣ Aumentar Dropout más
```python
Dropout(0.3) → Dropout(0.5)
```

### 2️⃣ Aumentar L2
```python
l2(0.001) → l2(0.01)
```

### 3️⃣ Revisar balance de datos
```python
# En main.py después de cargar
print(f"Train positivos: {sum(etiquetas)} / {len(etiquetas)}")
print(f"Train negativos: {len(etiquetas) - sum(etiquetas)}")
print(f"Test positivos: {sum(test_etiquetas)} / {len(test_etiquetas)}")
print(f"Test negativos: {len(test_etiquetas) - sum(test_etiquetas)}")

# Si desbalance > 70/30, usar class_weight
```

---

## Scenario 4: Accuracy 0.50 (random guessing)

**Diagnóstico:**
```
Accuracy = 0.50 o 0.51 (lo mismo que lanzar moneda)
```

**Causas potenciales:**

### Problema 1: Datos sin etiquetar bien
```python
# Verificar en main.py
print(train_df['Sentiment'].value_counts())
print(test_df['Sentiment'].value_counts())
```

### Problema 2: Modelo no entrena
```python
# Verificar learning rate
optimizer = Adam(learning_rate=0.1)  # Intenta más alto
```

### Problema 3: Arquitectura rota
```python
# Verificar shapes
print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")
# Deben ser (N, max_len) y (N,)
```

---

## Scenario 5: Error: "CUDA out of memory"

**Diagnóstico:**
```
RuntimeError: CUDA out of memory
```

**Soluciones en orden:**

1. Reducir batch_size: 32 → 16
2. Reducir vocab: 5000 → 2000  
3. Reducir embedding dims: 16 → 8
4. Usar CPU: Agrega al inicio
```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Fuerza CPU
```

---

## Scenario 6: "Early Stopping" nunca se activa

**Diagnóstico:**
```
Nunca ve "Early stopping: restoring model weights..."
```

**Soluciones:**

1. Verificar que validación funciona
```python
# Agregar debug
print(f"Val Loss Epoch 1: {history.history['val_loss'][0]}")
```

2. Aumentar paciencia
```python
patience=3  # aumenta a patience=10
```

3. Verificar monitor
```python
# En EarlyStopping
monitor='val_loss'  # Asegúrate que está correcto
```

---

## Checklist de Diagnóstico

Antes de cambiar código, verifica:

```
□ ¿Se ven 2 líneas de accuracy? (train y val)
  └─ Si no: falta validation_data

□ ¿La validación accuracy es similar a train?
  └─ Si es mucho menor: aumentar regularización

□ ¿Se detiene antes de 30 épocas?
  └─ Si no: ajustar patience en EarlyStopping

□ ¿El test accuracy es > 0.85?
  └─ Si no: modelo necesita más mejoras

□ ¿Cada época toma < 1 minuto?
  └─ Si no: considerar reducir batch size o features

□ ¿El accuracy es estable (±0.01)?
  └─ Si oscila: reducir learning rate o aumentar batch
```

---

## Script de Diagnóstico

Ejecuta esto para ver el estado completo:

```python
# Agregar al final de main.py
print("\n" + "="*60)
print("DIAGNÓSTICO DEL ENTRENAMIENTO")
print("="*60)

train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
train_loss = history.history['loss']
val_loss = history.history['val_loss']

print(f"Épocas completadas: {len(train_acc)}")
print(f"Best train acc: {max(train_acc):.4f} @ epoch {train_acc.index(max(train_acc))+1}")
print(f"Best val acc: {max(val_acc):.4f} @ epoch {val_acc.index(max(val_acc))+1}")
print(f"Diferencia (train-val): {(train_acc[-1] - val_acc[-1]):.4f}")

if (train_acc[-1] - val_acc[-1]) > 0.05:
    print("⚠️  OVERFITTING DETECTADO (>5% diferencia)")
elif (train_acc[-1] - val_acc[-1]) < -0.05:
    print("⚠️  UNDERFITTING DETECTADO (val > train)")
else:
    print("✅ Modelo balanceado")

print(f"Tendencia:")
if val_acc[-1] < val_acc[-3]:
    print("  ⚠️  Validación empeorando")
else:
    print("  ✅ Validación estable")

print("="*60)
```

---

## Contacto de Referencia

Si necesitas más ayuda, verifica:

1. **SOLUCION_ACCURACY.md** - Explicación completa
2. **COMPARACION_ANTES_DESPUES.md** - Cambios específicos
3. **ANALISIS_DETALLADO.md** - Visualización de problemas

---

✅ **Si logras identificar el scenario, la solución está arriba**


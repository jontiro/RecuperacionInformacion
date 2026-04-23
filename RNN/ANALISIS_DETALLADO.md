# 📊 ANÁLISIS: ¿Por qué baja la Accuracy entre épocas?

## 🔍 El Problema Visualizado

```
ACCURACY POR ÉPOCA (Tu caso original):

Accuracy
   ↑
  1.0 |
   0.95|     ●           ← Epoch 1: 0.9219 (bien)
       |      ╲
   0.90|       ●●        ← Epoch 2-3: 0.9019, 0.8985 (bajando)
       |         ╲╲
   0.85|          ●●     ← Epoch 4-5: 0.8443, 0.8260 (peor)
       |            ╲╲
   0.80|             ●   ← Epoch 6: 0.7899 (muy mal)
       |              ╲
   0.75|_______________●__→
       └─────────────────→ Época
         1  2  3  4  5  6

⚠️ PATRÓN: Caída rápida y consistente → OVERFITTING SEVERO
```

---

## 🎯 Root Causes Identificadas

### Causa #1: Batch Size = 4 (MUY PEQUEÑO)
```
Con batch_size=4:

Actualización de gradientes por lote:
┌─────────┐
│ Sample1 │
├─────────┤
│ Sample2 │  ← Solo 4 muestras = gradientes muy ruidosos
├─────────┤
│ Sample3 │
├─────────┤
│ Sample4 │
└─────────┘

Efecto: Los pesos "saltan" de un lado a otro
        en lugar de converger suavemente

Con batch_size=32:
┌─────────────────────┐
│ Sample 1-32         │
│ (promedio suave)    │ ← 32 muestras = gradientes estables
└─────────────────────┘

Efecto: Los pesos se actualizan de forma controlada
```

---

### Causa #2: Sin Validación Set
```
ANTES (tu código):
═════════════════════════════════════════════════════════
│ 153,059 MUESTRAS DE ENTRENAMIENTO                    │
│ (Sin dividir en train/validación)                    │
│                                                      │
│ El modelo puede memorizar TODO                       │
│ sin que lo detectemos                                │
═════════════════════════════════════════════════════════

DESPUÉS (mejorado):
═════════════════════════════════════════════════════════
│ 122,447 TRAIN         │ 30,612 VALIDACIÓN           │
│                       │                             │
│ Entrena aquí          │ Monitoreamos aquí           │
│                       │ ✓ Detectamos overfitting    │
═════════════════════════════════════════════════════════

Beneficio: Si el modelo empieza a memorizar,
          la validación accuracy bajará y lo veremos
```

---

### Causa #3: Sin Early Stopping
```
ENTRENAMIENTO SIN EARLY STOPPING:

Epoch 1: Train Loss 0.23 ✓ Mejor (restaurar pesos)
Epoch 2: Train Loss 0.29 ✗ Peor
Epoch 3: Train Loss 0.30 ✗ Peor
Epoch 4: Train Loss 0.39 ✗ Peor (continúa entrenando)
Epoch 5: Train Loss 0.42 ✗ Peor (continúa entrenando)
...
Epoch 30: Train Loss 0.89 ✗ MUY PEOR (nunca se detiene)
         
         Usamos pesos de Epoch 30 ← MALOS


ENTRENAMIENTO CON EARLY STOPPING:

Epoch 1: Train Loss 0.23, Val Loss 0.24 ✓ Mejor (guardar)
Epoch 2: Train Loss 0.29, Val Loss 0.28 ✗ Peor
Epoch 3: Train Loss 0.30, Val Loss 0.30 ✗ Peor
Epoch 4: Train Loss 0.31, Val Loss 0.31 ✗ Peor
         
         EARLY STOPPING ACTIVADO
         "No ha mejorado en 3 épocas, detener"
         
         Restauramos pesos de Epoch 1 ✓ BUENOS
```

---

### Causa #4: Modelo Muy Simple (Sin Regularización)
```
MODELO ORIGINAL:
┌──────────────────────┐
│ Embedding (16 dims)  │
└────────────┬─────────┘
             │
┌────────────▼─────────┐
│ SimpleRNN (32 units) │  ← Sin Dropout, Sin L2
└────────────┬─────────┘
             │
┌────────────▼─────────┐
│ Dense (1 output)     │  ← Sin regularización
└──────────────────────┘

Problema: El modelo puede aprender relaciones 
         arbitrarias (memorizar)

MODELO MEJORADO:
┌──────────────────────┐
│ Embedding (16 dims)  │
└────────────┬─────────┘
             │
┌────────────▼─────────┐
│ Dropout (0.3)        │  ← Apaga 30% neuronas al azar
└────────────┬─────────┘
             │
┌────────────▼─────────────────────┐
│ SimpleRNN (32) + L2 (0.001)      │  ← Regularización
│ (Penaliza pesos grandes)          │
└────────────┬─────────────────────┘
             │
┌────────────▼─────────┐
│ Dropout (0.3)        │  ← Más robustez
└────────────┬─────────┘
             │
┌────────────▼──────────────────────┐
│ SimpleRNN (16) + L2 (0.001)       │  ← Otro layer
└────────────┬──────────────────────┘
             │
┌────────────▼─────────┐
│ Dropout (0.3)        │  ← Previene memorización
└────────────┬─────────┘
             │
┌────────────▼──────────────────────┐
│ Dense (8) + L2 (0.001) Relu       │  ← Más capas
└────────────┬──────────────────────┘
             │
┌────────────▼─────────┐
│ Dropout (0.2)        │  ← Última regularización
└────────────┬─────────┘
             │
┌────────────▼─────────┐
│ Dense (1) Sigmoid    │
└──────────────────────┘

Beneficio: Modelo más robusto, menos overfitting
```

---

### Causa #5: Sin Control de Learning Rate
```
COMPILACIÓN ORIGINAL:
model.compile(optimizer="adam", ...)
                       ↑
                    Default LR = 0.001
                    (pero no explícito, puede variar)


COMPILACIÓN MEJORADA:
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, ...)
                                      ↑
                         Control explícito = consistencia
```

---

## 📈 Comparación: Antes vs Después

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Batch Size** | 4 (ruidoso) | 32 (suave) |
| **Validación** | ❌ No | ✅ Sí (20% datos) |
| **Early Stop** | ❌ No | ✅ Sí (patience=3) |
| **Dropout** | ❌ No | ✅ 0.3 en cada layer |
| **L2 Regularizer** | ❌ No | ✅ 0.001 en pesos |
| **Learning Rate** | Implícito | Explícito (0.001) |
| **Capas RNN** | 1 | 2 (mejora feature extraction) |
| **Densas** | 1 | 2 (mejora final mapping) |

---

## 🧬 Overfitting Explicado Visualmente

```
PERFECTO (Sin overfitting):
┌─────────────────────────────────────┐
│ Frontera de decisión suave y simple  │
│                                      │
│     ○ Negativo    ● Positivo        │
│                                      │
│   ○ ○ ○ ─────── ● ● ●              │
│     ○          ●                    │
│       ○      ●                      │
│                                      │
│ Generaliza bien en datos nuevos      │
└─────────────────────────────────────┘

OVERFITTING (Tu caso):
┌─────────────────────────────────────┐
│ Frontera zigzagueante y compleja     │
│                                      │
│   ○/●╱○/●╱○/●╱○/●╱○/●╱○           │
│   /╲/╲/╲/╲/╲/╲/╲/╲/╲/╲/╲/╲/        │
│  /  ╲/  ╲/  ╲/  ╲/  ╲/  ╲/         │
│                                      │
│ Trata de pasar por cada punto       │
│ Falla en datos nuevos (baja accuracy)│
└─────────────────────────────────────┘

SOLUCIÓN: Regularización (Dropout + L2)
fuerza una frontera más simple
```

---

## 🔬 Análisis de Impacto

```
Impacto de cada cambio en la accuracy:

Cambio                Impacto Estimado
─────────────────────────────────────
Batch 4→32            +2-3% mejora
Sin→Con Validación    Detecta -5% overfitting
Sin→Con Early Stop    Salva hasta -10% degradación
Dropout 0→0.3         +1-2% estabilidad
L2 0→0.001            +0.5-1% regularización
LR explícito          +0.1% consistencia
─────────────────────────────────────
TOTAL ESPERADO:       +5-10% mejora respecto a original
```

---

## 🎯 Meta Final

Con estos cambios, deberías ver:

```
✅ Epoch 1: 0.90-0.92 accuracy
✅ Epoch 2: 0.90-0.92 accuracy (estable)
✅ Epoch 3: 0.90-0.92 accuracy (NO baja)
✅ Early stopping en época 5-8 (convergencia natural)
✅ Val accuracy similar a train (no diverge)
✅ Test accuracy > 0.90 (generaliza bien)
```

**VS el original:**
```
❌ Epoch 1: 0.9219
❌ Epoch 2: 0.9019 (baja)
❌ Epoch 3: 0.8985 (sigue bajando)
❌ Epoch 4: 0.8443 (falla total)
❌ Sin early stop (continúa empeorando)
❌ Test accuracy < 0.80 (no generaliza)
```

---

## 📌 Conclusión

| Problema | Causa | Solución |
|----------|-------|----------|
| Accuracy baja cada época | Overfitting | Regularización + Validación |
| Gradientes ruidosos | Batch pequeño | Batch size 32 |
| Sin detección de crisis | Sin validación | Train/Val split |
| Continúa empeorando | Sin early stop | EarlyStopping callback |
| Memoriza datos | Modelo débil | Dropout + L2 + más capas |

✅ **Todo implementado. Listo para ejecutar.**


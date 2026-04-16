# 📊 Resumen: Configuración de RNN para Análisis de Sentimientos de Amazon

## ✅ Cambios Realizados

Se ha modificado exitosamente el archivo `main.py` para:

### 1. **Cargar datos correctamente desde archivos CSV**
   - **Entrenamiento**: `sentiment.csv` (171,613 reviews)
   - **Test**: `RATIO.csv` (64,262 reviews)
   - Codificación ajustada a `latin-1` para evitar errores Unicode

### 2. **Procesamiento de datos**
   - Eliminación de filas con valores faltantes
   - Mapeo de sentimientos: `positive=1`, `negative=0`
   - Tokenización con vocabulario de 5,000 palabras
   - Padding de secuencias a longitud máxima

### 3. **Modelo RNN mejorado**
   ```
   Embedding (16 dimensiones)
   ↓
   SimpleRNN (32 unidades, activación tanh)
   ↓
   Dense (1 unidad, activación sigmoid)
   ```

### 4. **Evaluación completa**
   - Métricas en conjunto de entrenamiento
   - Métricas en conjunto de test
   - Classification Report (precisión, recall, F1-score)
   - Matriz de confusión

## 📈 Resultados de la Prueba Rápida

| Métrica | Entrenamiento | Test (RATIO.csv) |
|---------|---------------|-----------------|
| **Exactitud** | 95.25% | 89.00% |
| **Pérdida** | 0.1498 | 0.2695 |

### Distribución de datos en la prueba:
- **Entrenamiento**: 4,824 reviews (87.5% positivos, 12.5% negativos)
- **Test**: 2,000 reviews (100% positivos)

⚠️ **Nota**: RATIO.csv contiene solo opiniones positivas en la muestra.

## 🎯 Recomendaciones

### 1. **Usar Equal.csv como alternativa de test**
   - RATIO.csv tiene un desbalance completo (solo positivos)
   - **Sugerencia**: Considerar usar `Equal.csv` como dataset de test
   - Verificación: `wc -l` muestra 76,748 líneas

### 2. **Para entrenamiento completo**
   - El script `main.py` está diseñado para 30 épocas
   - Usará ~170K reviews para entrenamiento
   - Con datos completos tardará más tiempo

### 3. **Archivos disponibles**
   ```
   RNN/data/
   ├── sentiment.csv  (171,613 líneas) ← ENTRENAMIENTO
   ├── RATIO.csv      (64,262 líneas)  ← TEST (solo positivos)
   └── Equal.csv      (76,748 líneas)  ← ALTERNATIVA TEST
   ```

## 🚀 Cómo usar

### Opción 1: Ejecutar con datos completos (actual)
```bash
cd RNN/
python main.py
```
Esto entrenará con ~170K reviews y evaluará con RATIO.csv

### Opción 2: Usar la prueba rápida
```bash
python test_quick.py
```
Entrena con 5,000 reviews (5 épocas) - útil para depuración

## 📝 Predicciones de ejemplo

El código incluye ejemplos que predicen el sentimiento de nuevas frases:
```python
"excelente producto muy recomendado"      → POSITIVO
"terrible calidad no lo compren"           → NEGATIVO
"muy buena compra recomendado al 100%"    → POSITIVO
```

## 💡 Próximas mejoras sugeridas

1. **Explorar otras capas**: LSTM, GRU en lugar de SimpleRNN
2. **Aumentar vocabulario**: Cambiar `num_words` de 5,000 a 10,000
3. **Usar Equal.csv**: Para un conjunto de test balanceado
4. **Validación cruzada**: Implementar k-fold para mayor robustez
5. **Data augmentation**: Aumentar datos con técnicas de NLP

---
**Estado**: ✅ Listo para entrenar  
**Fecha**: 2025-04-16  
**Archivos modificados**: main.py  
**Archivos nuevos**: test_quick.py


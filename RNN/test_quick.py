#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script de prueba rápida para RNN con datos reducidos"""

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import classification_report, confusion_matrix

print("=" * 60)
print("RNN con datos de sentimiento de Amazon")
print("=" * 60)

# ==========================================
# 1. Cargar datasets desde CSV (muestra pequeña)
# ==========================================
print("\nCargando datasets...")
train_df = pd.read_csv('./data/sentiment.csv', encoding='latin-1', nrows=5000)
test_df = pd.read_csv('./data/Equal.csv', encoding='latin-1', nrows=2000)

# Limpiar datos
train_df = train_df.dropna(subset=['Review', 'Sentiment'])
test_df = test_df.dropna(subset=['Review', 'Sentiment'])

# Convertir sentimientos
train_df['Sentiment'] = train_df['Sentiment'].map({'positive': 1, 'negative': 0})
test_df['Sentiment'] = test_df['Sentiment'].map({'positive': 1, 'negative': 0})

train_df = train_df.dropna()
test_df = test_df.dropna()

frases = train_df['Review'].values.tolist()
etiquetas = train_df['Sentiment'].values.astype(int).tolist()

test_frases = test_df['Review'].values.tolist()
test_etiquetas = test_df['Sentiment'].values.astype(int).tolist()

print(f"Entrenamiento: {len(frases)} reviews")
print(f"Test: {len(test_frases)} reviews")
print(f"  - Positivos (train): {sum(etiquetas)}")
print(f"  - Negativos (train): {len(etiquetas) - sum(etiquetas)}")
print(f"  - Positivos (test): {sum(test_etiquetas)}")
print(f"  - Negativos (test): {len(test_etiquetas) - sum(test_etiquetas)}")

# ==========================================
# 2. Tokenización
# ==========================================
print("\n Tokenizando datos...")
tokenizer = Tokenizer(num_words=3000, oov_token="<OOV>")
tokenizer.fit_on_texts(frases)

secuencias = tokenizer.texts_to_sequences(frases)
test_secuencias = tokenizer.texts_to_sequences(test_frases)

max_len = max(len(seq) for seq in secuencias + test_secuencias)

X = pad_sequences(secuencias, maxlen=max_len, padding="post")
y = np.array(etiquetas)

X_test = pad_sequences(test_secuencias, maxlen=max_len, padding="post")
y_test = np.array(test_etiquetas)

print(f"✓ X (train): {X.shape}")
print(f"✓ X_test: {X_test.shape}")
print(f"✓ Longitud máx de secuencia: {max_len}")

# ==========================================
# 3. Definir modelo RNN
# ==========================================
print("\nConstruyendo modelo RNN...")
vocab_size = len(tokenizer.word_index) + 1

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=16, input_shape=(max_len,)),
    SimpleRNN(32, activation="tanh"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print(model.summary())

# ==========================================
# 4. Entrenamiento (5 épocas para prueba rápida)
# ==========================================
print("\nEntrenando modelo (5 épocas)...")
history = model.fit(
    X, y,
    epochs=5,
    batch_size=32,
    verbose=1
)

# ==========================================
# 5. Evaluación
# ==========================================
print("\nEVALUACIÓN")
print("=" * 60)

loss_train, acc_train = model.evaluate(X, y, verbose=0)
print(f"\nENTRENAMIENTO:")
print(f"  Pérdida: {loss_train:.4f}")
print(f"  Exactitud: {acc_train:.4f}")

loss_test, acc_test = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTEST (RATIO.csv):")
print(f"  Pérdida: {loss_test:.4f}")
print(f"  Exactitud: {acc_test:.4f}")

# Predicciones detalladas
y_pred_proba = model.predict(X_test, verbose=0)
y_pred = (y_pred_proba >= 0.5).astype(int).flatten()

print(f"\n MÉTRICAS DETALLADAS (Test Set):")
print(classification_report(y_test, y_pred, target_names=['Negativo', 'Positivo']))

print("\nMatriz de confusión:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# ==========================================
# 6. Predicciones con comentarios REALES del test
# ==========================================
print("\nPREDICCIONES CON REVIEWS REALES DEL CONJUNTO DE TEST:")
print("=" * 60)

import random
# Seleccionar 10 comentarios al azar del conjunto de test
indices_aleatorios = random.sample(range(len(test_frases)), min(10, len(test_frases)))

aciertos = 0
errores = 0

for idx in indices_aleatorios:
    review_real = test_frases[idx]
    sentimiento_real = y_test[idx]
    etiqueta_real = "POSITIVO" if sentimiento_real == 1 else "NEGATIVO"
    
    # Predicción
    secuencia = tokenizer.texts_to_sequences([review_real])
    secuencia = pad_sequences(secuencia, maxlen=max_len, padding="post")
    pred_prob = model.predict(secuencia, verbose=0)[0][0]
    pred_etiqueta = "POSITIVO" if pred_prob >= 0.5 else "NEGATIVO"
    
    # Verificar si acertó
    es_correcto = (sentimiento_real == 1 and pred_prob >= 0.5) or (sentimiento_real == 0 and pred_prob < 0.5)
    if es_correcto:
        aciertos += 1
        simbolo = "✓"
    else:
        errores += 1
        simbolo = "✗"
    
    print(f"\n{simbolo} Review: '{review_real[:75]}...'")
    print(f"   Sentimiento real: {etiqueta_real}")
    print(f"   Predicción: {pred_etiqueta} (confianza: {pred_prob:.4f})")

print(f"\n" + "=" * 60)
print(f"RESUMEN DE PREDICCIONES EN DATOS REALES:")
print(f"   Aciertos: {aciertos}/10")
print(f"   Errores: {errores}/10")
print(f"   Precisión: {(aciertos/10)*100:.1f}%")
print("=" * 60)
print("PRUEBA COMPLETADA EXITOSAMENTE")
print("=" * 60)


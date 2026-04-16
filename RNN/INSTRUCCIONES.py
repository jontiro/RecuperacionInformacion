#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INSTRUCCIONES PARA USAR EL MODELO RNN
======================================

El algoritmo RNN ha sido configurado para entrenar con opiniones de Amazon
desde el archivo sentiment.csv y validarse con RATIO.csv
"""

print("""
╔════════════════════════════════════════════════════════════════════════════╗
║           🤖 RNN PARA ANÁLISIS DE SENTIMIENTOS DE AMAZON 🤖               ║
╚════════════════════════════════════════════════════════════════════════════╝

📊 CONFIGURACIÓN ACTUAL:
─────────────────────────────────────────────────────────────────────────────

  📁 DATOS DE ENTRENAMIENTO:
    └─ RNN/data/sentiment.csv (171,613 reviews)
       • Contiene: Reviews, Sentimiento (positivo/negativo)
       • Codificación: latin-1

  📁 DATOS DE TEST:
    └─ RNN/data/RATIO.csv (64,262 reviews)
       • Codificación: latin-1
       • ⚠️  Nota: Contiene solo opiniones positivas

  📁 ALTERNATIVA DE TEST (balanceada):
    └─ RNN/data/Equal.csv (76,748 reviews)
       • Podría ser mejor para evaluación real

─────────────────────────────────────────────────────────────────────────────

🚀 CÓMO EJECUTAR:
─────────────────────────────────────────────────────────────────────────────

  1️⃣  ENTRENAMIENTO COMPLETO (30 épocas):
      $ cd ~/PycharmProjects/RecuperacionInformacion/RNN
      $ python main.py
      
      ⏱️  Tiempo estimado: 30-60 minutos (según CPU)
      📊 Genera métricas completas de evaluación

  2️⃣  PRUEBA RÁPIDA (5 épocas, datos reducidos):
      $ python test_quick.py
      
      ⏱️  Tiempo estimado: 2-3 minutos
      ✅ Verificación rápida que todo funciona

  3️⃣  USAR MODELO ENTRENADO:
      Agregar al final de main.py:
      ```python
      model.save('modelo_rnn.h5')
      ```
      
      Para cargar y usar:
      ```python
      from tensorflow.keras.models import load_model
      model = load_model('modelo_rnn.h5')
      ```

─────────────────────────────────────────────────────────────────────────────

📈 QUÉ ESPERAR:
─────────────────────────────────────────────────────────────────────────────

  PRUEBA RÁPIDA (test_quick.py):
  ✓ Exactitud en entrenamiento: ~95%
  ✓ Exactitud en test: ~89%
  ✓ Tiempo total: 2-3 minutos

  ENTRENAMIENTO COMPLETO (main.py):
  ✓ Será más preciso con más épocas
  ✓ Mejor generalización con más datos
  ✓ Incluye predicciones en nuevas frases

─────────────────────────────────────────────────────────────────────────────

🔧 PERSONALIZACIÓN:
─────────────────────────────────────────────────────────────────────────────

  En main.py, puedes modificar:

  • Tamaño del vocabulario:
    tokenizer = Tokenizer(num_words=5000)  # Cambiar 5000

  • Número de épocas:
    epochs=30  # Cambiar 30

  • Tamaño del batch:
    batch_size=4  # Cambiar 4

  • Dimensiones de embedding:
    output_dim=16  # Cambiar 16

  • Unidades del RNN:
    SimpleRNN(32)  # Cambiar 32

─────────────────────────────────────────────────────────────────────────────

⚠️  NOTAS IMPORTANTES:
─────────────────────────────────────────────────────────────────────────────

  1. El archivo RATIO.csv contiene SOLO opiniones positivas
     → La matriz de confusión mostrará pocas/ninguna predicción negativa
     → Considera usar Equal.csv para pruebas más realistas

  2. El encoding es latin-1, NO utf-8
     → Esto maneja correctamente caracteres especiales de Amazon

  3. Primero ejecuta test_quick.py para verificar que todo funciona
     → Luego corre main.py para el entrenamiento completo

  4. Requiere:
     • TensorFlow/Keras
     • Pandas
     • Scikit-learn
     • NumPy

─────────────────────────────────────────────────────────────────────────────

📚 ESTRUCTURA DEL MODELO:
─────────────────────────────────────────────────────────────────────────────

  Embedding (input_dim=vocab_size, output_dim=16)
      ↓
  SimpleRNN (units=32, activation='tanh')
      ↓
  Dense (units=1, activation='sigmoid')
      ↓
  SALIDA: Probabilidad de sentimiento positivo [0-1]

─────────────────────────────────────────────────────────────────────────────

✅ PRÓXIMOS PASOS:
─────────────────────────────────────────────────────────────────────────────

  □ Ejecutar test_quick.py para verificar
  □ Ejecutar main.py para entrenamiento completo
  □ Analizar métricas de classification_report
  □ Hacer predicciones con nuevas frases
  □ Guardar el modelo entrenado
  □ Considerar usar Equal.csv como test alternativo

╔════════════════════════════════════════════════════════════════════════════╗
║                     ¡Listo para entrenar tu modelo!                        ║
╚════════════════════════════════════════════════════════════════════════════╝
""")


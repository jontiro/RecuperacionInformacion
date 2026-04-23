# -*- coding: utf-8 -*-
"""
Script para visualizar el histórico de entrenamiento
Muestra gráficos de accuracy y loss en train/validación
"""

import matplotlib.pyplot as plt
import pickle
import os

def plot_training_history(history):
    """Visualiza loss y accuracy durante el entrenamiento"""
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfico 1: Accuracy
    axes[0].plot(history.history['accuracy'], label='Accuracy Entrenamiento', marker='o')
    axes[0].plot(history.history['val_accuracy'], label='Accuracy Validación', marker='s')
    axes[0].set_xlabel('Época')
    axes[0].set_ylabel('Accuracy')
    axes[0].set_title('Accuracy: Entrenamiento vs Validación')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Gráfico 2: Loss
    axes[1].plot(history.history['loss'], label='Loss Entrenamiento', marker='o')
    axes[1].plot(history.history['val_loss'], label='Loss Validación', marker='s')
    axes[1].set_xlabel('Época')
    axes[1].set_ylabel('Loss')
    axes[1].set_title('Loss: Entrenamiento vs Validación')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('training_history.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado como 'training_history.png'")
    
    # Análisis de overfitting
    train_acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    diff_acc = [train_acc[i] - val_acc[i] for i in range(len(train_acc))]
    
    print("\n=== ANÁLISIS DE OVERFITTING ===")
    print(f"Máxima diferencia Accuracy (train - val): {max(diff_acc):.4f}")
    print(f"Épocas: {len(train_acc)}")
    print(f"Mejor accuracy validación: {max(val_acc):.4f}")
    print(f"Mejor accuracy entrenamiento: {max(train_acc):.4f}")
    
    # Detectar si hay overfitting
    if max(diff_acc) > 0.1:
        print("⚠️  OVERFITTING DETECTADO: La diferencia entre train y val > 0.1")
    else:
        print("✓ Modelo generalizando bien")

if __name__ == "__main__":
    # Nota: Este script requiere que history sea guardado en main.py
    print("Script de visualización listo")
    print("Se ejecutará automáticamente después del entrenamiento")


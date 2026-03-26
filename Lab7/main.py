"""
Laboratorio 7: Recuperación de Información
Autores: Nava Campos Alejandro Dante, Ortega Pérez Andrea, y Tiro Cuanenemi Jonathan.

Objetivo:
Utilizar los juicios de relevancia de la colección CACM (qrels.text) y la salida
de la práctica 6 para calcular métricas de evaluación:
- Precisión
- Recuerdo
- Media F (F-measure)
- Precisión R (P@R)

Las métricas se calculan para los primeros Z documentos de cada consulta.
Z se lee de pantalla, y se guardan resultados con Z = 100.

Entrada:
  Lab6/output/CACM_tf_idf_rels.txt
  Lab3/resources/CACM/qrels.text

Salida:
  output/metricas_evaluacion_Z100.txt
"""

import os
from collections import defaultdict

# ---------------------------------------------------------
# Rutas
# ---------------------------------------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LAB6_DIR = os.path.join(BASE_DIR, 'Lab6', 'output')
LAB3_DIR = os.path.join(BASE_DIR, 'Lab3', 'resources', 'CACM')

RESULTS_FILE = os.path.join(LAB6_DIR, 'CACM_tf_idf_rels.txt')
QRELS_FILE = os.path.join(LAB3_DIR, 'qrels.text')

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')
OUTPUT_FILE_Z100 = os.path.join(OUTPUT_DIR, 'metricas_evaluacion_Z100.txt')


# ---------------------------------------------------------
# 1. Leer juicios de relevancia (qrels.text)
# ---------------------------------------------------------

def leer_qrels(ruta):
    """
    Lee el archivo qrels.text.
    Formato: QID DocID 0 0
    Retorna: dict[query_id] = set(relevant_doc_ids)
    """
    qrels = defaultdict(set)
    with open(ruta, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                partes = line.split()
                qid = int(partes[0])
                docid = int(partes[1])
                qrels[qid].add(docid)
    return dict(qrels)


# ---------------------------------------------------------
# 2. Leer resultados de recuperación (Lab 6)
# ---------------------------------------------------------

def leer_resultados(ruta):
    """
    Lee el archivo de resultados del Lab 6.
    Formato: QID DocID Similitud
    Retorna: dict[query_id] = list[(doc_id, similitud), ...]
    """
    resultados = defaultdict(list)
    with open(ruta, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                partes = line.split()
                qid = int(partes[0])
                docid = int(partes[1])
                sim = float(partes[2])
                resultados[qid].append((docid, sim))
    return dict(resultados)


# ---------------------------------------------------------
# 3. Calcular métricas para Z documentos
# ---------------------------------------------------------

def calcular_metricas1(qid, docs_recuperados_z, docs_relevantes):
    """
    Calcula las métricas para una consulta.
    
    Args:
        qid: ID de la consulta
        docs_recuperados_z: lista de doc_ids recuperados (primeros Z)
        docs_relevantes: set de doc_ids relevantes
    
    Returns:
        dict con las métricas:
        - precision_por_posicion: lista de precisiones en cada posición
        - precision: precisión final (en última posición)
        - recuerdo: documentos relevantes recuperados / total relevantes
        - medida_f: media armónica de precisión y recuerdo (2EP)/(P+E)
        - precision_r: documentos relevantes / posición R
    """
    
    # Total de documentos relevantes
    total_relevantes = len(docs_relevantes)
    
    # Número de documentos recuperados
    num_recuperados = len(docs_recuperados_z)
    
    # Calcular precisión iterativamente en cada posición
    precision_por_posicion = []
    rel_cnt = 0
    
    for pos, doc in enumerate(docs_recuperados_z, start=1):
        if doc in docs_relevantes:
            rel_cnt += 1
        precision_actual = rel_cnt / pos
        precision_por_posicion.append(precision_actual)
    
    # Precisión final (en la última posición)
    precision = precision_por_posicion[-1] if precision_por_posicion else 0.0
    
    # Recuerdo: relevantes_recuperados / total_relevantes
    # Se calcula con totales
    num_relevantes_recuperados = precision_por_posicion[-1] * num_recuperados if precision_por_posicion else 0
    recuerdo = num_relevantes_recuperados / total_relevantes if total_relevantes > 0 else 0.0
    
    # Media F: 2 * (precisión * recuerdo) / (precisión + recuerdo)
    if precision + recuerdo > 0:
        medida_f = 2 * (precision * recuerdo) / (precision + recuerdo)
    else:
        medida_f = 0.0
    
    # Precisión R: documentos relevantes / posición del último relevante encontrado
    # Si no hay relevantes recuperados, es 0
    if num_relevantes_recuperados > 0:
        # Posición del último relevante (1-indexed)
        ultima_pos_relevante = None
        for pos, p in enumerate(precision_por_posicion, start=1):
            if pos == 1 or precision_por_posicion[pos-2] < p:
                ultima_pos_relevante = pos
        precision_r = num_relevantes_recuperados / ultima_pos_relevante if ultima_pos_relevante else 0.0
    else:
        precision_r = 0.0
    
    return {
        'precision_por_posicion': precision_por_posicion,
        'precision': precision,
        'recuerdo': recuerdo,
        'medida_f': medida_f,
        'precision_r': precision_r
    }


def calcular_metricas(qid, docs_recuperados_z, docs_relevantes):
    """
    Calcula las métricas para una consulta.
    """
    # Total de documentos relevantes (R)
    total_relevantes = len(docs_relevantes)

    # Número de documentos recuperados (Z)
    num_recuperados = len(docs_recuperados_z)

    # Calcular precisión iterativamente en cada posición
    precision_por_posicion = []
    rel_cnt = 0

    for pos, doc in enumerate(docs_recuperados_z, start=1):
        if doc in docs_relevantes:
            rel_cnt += 1
        precision_actual = rel_cnt / pos
        precision_por_posicion.append(precision_actual)

    # Precisión final (en la última posición Z)
    precision = precision_por_posicion[-1] if precision_por_posicion else 0.0

    # Recuerdo: relevantes_recuperados (rel_cnt) / total_relevantes
    recuerdo = rel_cnt / total_relevantes if total_relevantes > 0 else 0.0

    # Medida F: Media armónica
    if precision + recuerdo > 0:
        medida_f = 2 * (precision * recuerdo) / (precision + recuerdo)
    else:
        medida_f = 0.0

    # Precisión R: Precisión calculada exactamente en la posición R (total_relevantes)
    if total_relevantes > 0:
        # Contamos cuántos de los primeros R documentos recuperados son relevantes
        relevantes_en_R = sum(1 for doc in docs_recuperados_z[:total_relevantes] if doc in docs_relevantes)
        precision_r = relevantes_en_R / total_relevantes
    else:
        precision_r = 0.0

    return {
        'precision_por_posicion': precision_por_posicion,
        'precision': precision,
        'recuerdo': recuerdo,
        'medida_f': medida_f,
        'precision_r': precision_r
    }

# ---------------------------------------------------------
# 4. Procesar todas las consultas
# ---------------------------------------------------------

def procesar_consultas(resultados, qrels, z):
    """
    Calcula las métricas para todas las consultas considerando Z documentos.
    
    Returns:
        dict[query_id] = {metricas}
    """
    metricas_por_consulta = {}
    
    # Obtener IDs de consultas (desde resultados, ya que hay más en qrels)
    query_ids = sorted(set(resultados.keys()))
    
    for qid in query_ids:
        # Obtener los primeros Z documentos recuperados para esta consulta
        docs_recuperados = resultados.get(qid, [])
        docs_recuperados_z = [doc for doc, _ in docs_recuperados[:z]]
        
        # Obtener documentos relevantes para esta consulta
        docs_relevantes = qrels.get(qid, set())
        
        # Si no hay documentos relevantes, saltar
        if not docs_relevantes:
            continue

        # Calcular métricas
        metricas = calcular_metricas(qid, docs_recuperados_z, docs_relevantes)
        metricas_por_consulta[qid] = metricas
    
    return metricas_por_consulta


# ---------------------------------------------------------
# 5. Guardar resultados
# ---------------------------------------------------------

def guardar_resultados(metricas_por_consulta, ruta_salida, z):
    """
    Guarda los resultados en el formato especificado.
    """
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        f.write(f"Métricas de Evaluación (Z={z})\n")
        f.write(f"\nConsulta  Precision  Recuerdo   Medida F   Precision R\n")
        f.write("-" * 57 + "\n")
        
        query_ids = sorted(metricas_por_consulta.keys())
        for qid in query_ids:
            metricas = metricas_por_consulta[qid]
            f.write(
                f"{qid:5d}    {metricas['precision']:7.4f}    "
                f"{metricas['recuerdo']:7.4f}    {metricas['medida_f']:7.4f}    "
                f"{metricas['precision_r']:7.4f}\n"
            )
    
    print(f"Resultados guardados en: {ruta_salida}")


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():
    print("=" * 60)
    print("Laboratorio 7: Evaluación de Recuperación de Información")
    print("=" * 60)
    
    # Leer datos de entrada
    print("\n1. Leyendo juicios de relevancia...")
    qrels = leer_qrels(QRELS_FILE)
    print(f"   Total de consultas en qrels: {len(qrels)}")
    
    print("\n2. Leyendo resultados del Lab 6...")
    resultados = leer_resultados(RESULTS_FILE)
    print(f"   Total de consultas en resultados: {len(resultados)}")
    
    # Procesar con Z=100
    print("\n3. Calculando métricas para Z=100...")
    z = 100
    metricas = procesar_consultas(resultados, qrels, z)
    print(f"   Total de consultas evaluadas: {len(metricas)}")
    
    # Guardar resultados
    print("\n4. Guardando resultados...")
    guardar_resultados(metricas, OUTPUT_FILE_Z100, z)
    
    # Opcionalmente, permitir al usuario ingresar otro valor de Z
    print("\n" + "=" * 60)
    print("Deseas evaluar con otro valor de Z? (s/n): ", end="")
    respuesta = input().strip().lower()
    
    if respuesta == 's':
        try:
            z_usuario = int(input("Ingresa el valor de Z: "))
            if z_usuario > 0:
                print(f"\nCalculando métricas para Z={z_usuario}...")
                metricas_z = procesar_consultas(resultados, qrels, z_usuario)
                output_file = os.path.join(
                    OUTPUT_DIR, f'metricas_evaluacion_Z{z_usuario}.txt'
                )
                guardar_resultados(metricas_z, output_file, z_usuario)
            else:
                print("El valor de Z debe ser mayor a 0.")
        except ValueError:
            print("Valor inválido. Por favor ingresa un número entero.")
    
    print("\n" + "=" * 60)
    print("¡Proceso completado!")
    print("=" * 60)


if __name__ == '__main__':
    main()

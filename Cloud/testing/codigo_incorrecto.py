# Este fichero (codigo_monstruoso.py) es un ejemplo deliberado de "mal código".
# No sigue PEP 8, mezcla responsabilidades, usa estado global, tiene dependencias
# hardcodeadas (requests, datetime) y efectos secundarios (print, escritura de ficheros),
# lo que lo hace casi imposible de testear de forma unitaria.

import os, sys, requests, datetime # Imports desordenados (para isort)

API_KEY_SECRETA = "sk-12345abcdefg_hardcoded_token" # Problema de seguridad (para bandit)

# Estado global: ¡muy mala práctica!
USUARIOS_PROCESADOS_GLOBALMENTE = []

def procesar_usuarios_y_reportar(lista_ids_usuarios: list, nombre_reporte: str):
    """
CUIDADO: Esta función es un monstruo de alta cohesión y alto acoplamiento.
1. Tiene alta complejidad ciclomática (muchos if/else anidados).
2. Mezcla responsabilidades (lógica de negocio, llamadas a API, escritura de fichero).
3. Está fuertemente acoplado (usa 'requests' y 'datetime' directamente).
4. Tiene efectos secundarios (escribe a disco, modifica estado global, imprime a consola).
5. Mal estilo (para flake8, black).
6. Problemas de seguridad (para bandit).
7. Tipos ambiguos (para mypy).
"""
    print("...Iniciando procesamiento masivo...")
    
    # Acoplamiento directo a datetime
    reporte_final = f"--- Reporte de {nombre_reporte} ({datetime.datetime.now()}) ---\n"
    
    if len(lista_ids_usuarios) == 0:
        print("No hay usuarios que procesar.")
        return # Salida temprana

    for user_id in lista_ids_usuarios:
        # 1. Dependencia Externa (Acoplamiento)
        try:
            # 2. Problema de Seguridad (API Key hardcodeada)
            url = f"https://api.ejemplo.com/v1/users/{user_id}?token={API_KEY_SECRETA}"
            
            # Acoplamiento directo a requests
            respuesta = requests.get(url, timeout=5) 
            
            if respuesta.status_code == 200:
                usuario = respuesta.json() # Asumimos que es JSON
                
                # 3. Alta Complejidad Ciclomática (Lógica de negocio mezclada)
                if usuario['edad'] > 18:
                    if usuario['pais'] == "ES":
                        usuario['descuento_aplicado'] = 0.2
                        reporte_final += f"INFO: Usuario {user_id} tiene descuento ES (20%).\n"
                    elif usuario['pais'] == "MX" and usuario['edad'] > 65:
                        usuario['descuento_aplicado'] = 0.3
                        reporte_final += f"INFO: Usuario {user_id} tiene descuento MX senior (30%).\n"
                    else:
                        usuario['descuento_aplicado'] = 0.05
                        reporte_final += f"INFO: Usuario {user_id} tiene descuento base (5%).\n"
                else:
                    usuario['descuento_aplicado'] = 0.0
                    reporte_final += f"WARN: Usuario {user_id} es menor de edad, sin descuento.\n"
                
                # 4. Efecto Secundario (Estado Global)
                USUARIOS_PROCESADOS_GLOBALMENTE.append(usuario)
            
            elif respuesta.status_code == 404:
                 reporte_final += f"ERROR: Usuario {user_id} no encontrado (404).\n"
            else:
                reporte_final += f"ERROR: No se pudo obtener usuario {user_id}. Status: {respuesta.status_code}\n"
        
        except requests.Timeout:
            reporte_final += f"ERROR: Timeout para usuario {user_id}.\n"
        except Exception as e:
            reporte_final += f"ERROR: Fallo inesperado para {user_id}: {e}\n"

    # 5. Efecto Secundario (Escritura a fichero)
    nombre_fichero = nombre_reporte + ".txt"
    try:
        with open(nombre_fichero, "w") as f:
            f.write(reporte_final)
    except IOError:
        print(f"Error fatal: no se pudo escribir el reporte {nombre_fichero}")


    print(f"Procesamiento finalizado. Reporte guardado en {nombre_fichero}")
    return reporte_final

if __name__ == "__main__":
    # Error de tipo: la función espera IDs (int) pero pasamos un string
    usuarios_a_procesar = [1, 2, 99, "diez"] 
    
    procesar_usuarios_y_reportar(usuarios_a_procesar, "reporte_diario")
    
    print(f"Total de usuarios procesados en el estado global: {len(USUARIOS_PROCESADOS_GLOBALMENTE)}")
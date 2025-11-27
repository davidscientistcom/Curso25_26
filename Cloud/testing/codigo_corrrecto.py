# Este es el resultado final de refactorizar 'codigo_monstruoso.py'.
# El código ahora está desacoplado, es cohesivo y completamente testeable.

import os
import sys
import requests
from datetime import datetime
from typing import List, Dict, Any, Tuple

# --- 1. Lógica Pura (Totalmente Testeable) ---

def calcular_descuento_usuario(usuario: Dict[str, Any]) -> Tuple[Dict[str, Any], str]:
    """
    Función pura. Recibe un usuario, devuelve el usuario actualizado
    con su descuento y un mensaje de log.
    No tiene efectos secundarios.
    """
    # Copiamos para evitar mutar el diccionario original
    usuario_actualizado = usuario.copy()
    user_id = usuario_actualizado.get('id', 'N/A') # Usamos .get para seguridad
    
    if usuario_actualizado.get('edad', 0) > 18:
        if usuario_actualizado.get('pais') == "ES":
            usuario_actualizado['descuento_aplicado'] = 0.2
            log = f"INFO: Usuario {user_id} tiene descuento ES (20%)."
        elif usuario_actualizado.get('pais') == "MX" and usuario_actualizado.get('edad', 0) > 65:
            usuario_actualizado['descuento_aplicado'] = 0.3
            log = f"INFO: Usuario {user_id} tiene descuento MX senior (30%)."
        else:
            usuario_actualizado['descuento_aplicado'] = 0.05
            log = f"INFO: Usuario {user_id} tiene descuento base (5%)."
    else:
        usuario_actualizado['descuento_aplicado'] = 0.0
        log = f"WARN: Usuario {user_id} es menor de edad, sin descuento."
        
    return usuario_actualizado, log

# --- 2. Abstracción de Dependencias (Testeable con Mocks) ---

class ClienteAPI:
    """
    Abstrae la dependencia directa de 'requests'.
    Ahora podemos "mockear" esta clase completa en nuestros tests.
    """
    def __init__(self, api_key: str, base_url: str = "https://api.ejemplo.com/v1"):
        # La API Key se inyecta, no está hardcodeada
        self.api_key = api_key
        self.base_url = base_url

    def obtener_usuario(self, user_id: int) -> Dict[str, Any]:
        """
        Obtiene un usuario. Lanza excepciones en caso de error.
        Este es el *único* lugar en el código que usa 'requests'.
        """
        url = f"{self.base_url}/users/{user_id}?token={self.api_key}"
        
        # 'requests' sigue aquí, pero aislado en un solo método.
        respuesta = requests.get(url, timeout=5)
        
        # Lanza una excepción (ej. HTTPError) si el status es 4xx o 5xx
        respuesta.raise_for_status() 
        return respuesta.json()

# --- 3. Orquestador (Testeable con Mocks) ---

def procesar_usuarios_y_reportar_refactorizado(
    lista_ids_usuarios: List[int],
    cliente_api: ClienteAPI, # Inyección de Dependencia
    fecha_actual: datetime, # Inyección de Dependencia
) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Función orquestadora. Ahora es testeable porque sus dependencias
    (cliente_api, fecha_actual) son inyectadas.
    
    NO tiene efectos secundarios:
    - No usa 'print'
    - No escribe ficheros
    - No usa estado global
    - No llama a 'datetime.now()'
    """
    reporte_final = f"--- Reporte de ({fecha_actual.isoformat()}) ---\n"
    usuarios_procesados = [] # Estado local, no global

    for user_id in lista_ids_usuarios:
        try:
            # 1. Usa la dependencia inyectada (mockeable)
            usuario = cliente_api.obtener_usuario(user_id)
            
            # 2. Llama a la lógica pura (testeable)
            usuario_actualizado, log = calcular_descuento_usuario(usuario)
            
            reporte_final += log + "\n"
            usuarios_procesados.append(usuario_actualizado)
        
        # Errores de API (lanzados por raise_for_status())
        except requests.HTTPError as e:
            if e.response and e.response.status_code == 404:
                reporte_final += f"ERROR: Usuario {user_id} no encontrado (404).\n"
            else:
                reporte_final += f"ERROR: HTTP para {user_id}: {e}\n"
        except requests.Timeout:
            reporte_final += f"ERROR: Timeout para usuario {user_id}.\n"
        except Exception as e:
            # Captura cualquier otro error (ej. JSONDecodeError)
            reporte_final += f"ERROR: Fallo inesperado para {user_id}: {e}\n"

    # Devuelve los resultados en lugar de escribirlos
    return reporte_final, usuarios_procesados

# --- 4. Bloque de Ejecución (El único lugar "sucio") ---

if __name__ == "__main__":
    
    print("Iniciando proceso de reporte...")
    
    # 1. Carga la configuración (el único sitio que lee 'os')
    # Soluciona el problema de seguridad de 'bandit'
    API_KEY = os.environ.get("MI_API_KEY")
    if not API_KEY:
        print("Error: La variable de entorno 'MI_API_KEY' no está definida.")
        sys.exit(1)

    # 2. Crea las dependencias ("sucias")
    cliente_real = ClienteAPI(api_key=API_KEY)
    fecha_real = datetime.now()
    usuarios_a_procesar = [1, 2, 99, 10] # Soluciona el problema de 'mypy'

    # 3. Llama a la lógica limpia (orquestador)
    reporte_str, procesados = procesar_usuarios_y_reportar_refactorizado(
        usuarios_a_procesar, cliente_real, fecha_real
    )

    # 4. Ejecuta los efectos secundarios (print, escritura)
    try:
        with open("reporte_diario.txt", "w") as f:
            f.write(reporte_str)
        print(f"Reporte generado: reporte_diario.txt")
        print(f"Total de usuarios procesados: {len(procesados)}")
    except IOError as e:
        print(f"Error fatal al escribir el fichero: {e}")
import requests
import time
import random

def send_traffic():
    print("🚀 Generando tráfico para el dashboard... (CTRL+C para parar)")
    while True:
        try:
            # Petición normal
            requests.get("http://0.0.0.0:8000/")
            
            # 10% de probabilidad de generar un error 500 (si el caos está activo)
            if random.random() < 0.1:
                requests.get("http://0.0.0.0:8000/health")
            
            time.sleep(0.5) # 2 peticiones por segundo
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    send_traffic()

from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ejecutar_comando/{comando}")
async def ejecutar_comando(comando: str):
    try:
        # Ejecutar el comando en la consola y capturar la salida
        resultado = subprocess.run(comando.split(), capture_output=True, text=True)
        if resultado.returncode == 0:
            return {"output": resultado.stdout}
        else:
            return {"error": resultado.stderr}
    except Exception as e:
        return {"error": str(e)}

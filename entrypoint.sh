#!/bin/bash
set -e

MODEL="${OLLAMA_MODEL:-mistral}"

# Iniciar Ollama en segundo plano
ollama serve &

# Esperar a que Ollama esté listo
echo "Waiting for Ollama to start..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 2
done

# Descargar el modelo si no existe en el volumen
if ! ollama list | grep -q "$MODEL"; then
  echo "Model $MODEL not found. Downloading..."
  ollama pull "$MODEL"
else
  echo "Model $MODEL already downloaded."
fi

# Mantener el proceso
wait -n

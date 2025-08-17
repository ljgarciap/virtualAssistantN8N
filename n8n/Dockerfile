FROM node:20-bookworm

RUN npm install -g n8n@1.105.4 --unsafe-perm

RUN apt-get update && apt-get install -y \
    python3 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

USER node
WORKDIR /home/node

ENTRYPOINT ["n8n", "start"]
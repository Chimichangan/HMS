FROM node:20-alpine

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* frontend/pnpm-lock.yaml* ./
RUN npm install || true

COPY frontend /app/frontend
EXPOSE 5173
# Vite dev server must listen on 0.0.0.0 to be reachable from host
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

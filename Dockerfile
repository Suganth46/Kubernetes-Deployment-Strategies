FROM node:20-alpine AS build
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY src ./src
COPY static ./static
COPY tailwind.config.js ./

RUN npm run build:css

FROM nginx:alpine
COPY --from=build /app/static /usr/share/nginx/html

EXPOSE 80

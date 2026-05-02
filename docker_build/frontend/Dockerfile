FROM nginx:1.29.8-alpine3.23-slim

RUN apk add --no-cache curl

RUN rm -f /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY frontend/static /usr/share/nginx/html

COPY docker_build/frontend/nginx.conf /etc/nginx/nginx.conf
COPY docker_build/frontend/proxy-headers.conf /etc/nginx/proxy-headers.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

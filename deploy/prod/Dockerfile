FROM nginx:latest
RUN apt-get update && apt-get install nginx -y
COPY deploy/prod/nginx/docker_playground.conf /etc/nginx/conf.d/default.conf

FROM node:alpine

WORKDIR /usr/src/app

COPY rollup.config.js ./
COPY package*.json ./

RUN npm install

# # copy only in case of production.
# # for development, use mounted volumes instead.

COPY ./src ./src
COPY ./public ./public

RUN npm run-script build

# EXPOSE 5000

# ENV HOST=0.0.0.0

# CMD [ "npm", "start" ]
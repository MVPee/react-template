FROM nginx:alpine

RUN apk add --no-cache openssl

RUN mkdir /etc/nginx/ssl && \
    openssl req -x509 -nodes -days 365 \
    -newkey rsa:2048 -keyout /etc/nginx/ssl/ssl.key \
    -out /etc/nginx/ssl/ssl.crt \
    -subj   "/C=${COUNTRY}/ST=${STATE}/L=${LOCALITY} \
            /O=${ORGANISATION}/OU=${ORGANISATION2}/CN=${COMMON_NAME}"

COPY ./conf/nginx.conf /etc/nginx/templates/default.conf.template
RUN envsubst < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf

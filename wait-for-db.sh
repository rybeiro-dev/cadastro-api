#!/bin/bash
set -e

# Espera até o MySQL estar disponível
until mysqladmin ping -h db_server --silent; do
  >&2 echo "MySQL não está disponível - aguardando..."
  sleep 2
done

>&2 echo "MySQL está disponível - iniciando o servidor web"
exec "$@"

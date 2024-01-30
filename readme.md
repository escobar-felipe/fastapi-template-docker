# FASTAPI - TEMPLATE
 Fluxo GIT

![alt text](https://www.alura.com.br/artigos/assets/git-flow-o-que-e-como-quando-utilizar/imagem3.png)

## ENV
Criar .env mesmo diretório do compose.

## Requirements
Quando instalar nova depenência atualizar requirements
```Bash
pip freeze > src/requirements.txt
```

## Criar network
```Bash
docker network create --driver=bridge --subnet=172.35.0.0/24 --gateway=172.35.0.254 net-host
```

## Como rodar
```bash
docker compose up -d --build
```

## Logs
Lembre-se de talvez adicionar o parametro --tail
```bash
docker compose logs --tail 100 -f 
```

## Precommit
```bash
pre-commit run --all-files
```

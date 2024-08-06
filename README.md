# Cadastro API

Bem-vindo ao projeto Cadastro API! Esta é uma API RESTful construída com FastAPI, que permite realizar operações 
de cadastro. Utiliza Docker para facilitar o ambiente de desenvolvimento e produção. O projeto emprega várias 
tecnologias modernas, incluindo SQLAlchemy para ORM, Alembic para migrações de banco de dados, e Pydantic para 
validação de dados.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construir APIs rápidas e eficientes.
- **SQLAlchemy**: ORM para manipulação de banco de dados.
- **Alembic**: Ferramenta para migrações de banco de dados.
- **Uvicorn**: Servidor ASGI para execução da aplicação.
- **MySQL**: Sistema de gerenciamento de banco de dados.
- **Pydantic**: Biblioteca para validação e definição de dados.
- **requests**: Biblioteca para fazer requisições HTTP.
- **Docker**: Plataforma para criar e gerenciar containers.

## Pré-requisitos

Para rodar este projeto, você precisará ter o Docker instalado na sua máquina. 
Se ainda não tiver o Docker instalado, você pode [baixá-lo aqui](https://www.docker.com/get-started).

## Estrutura do Projeto

- `./`: Código fonte da aplicação FastAPI.
- `alembic/`: Configurações e scripts de migração de banco de dados.
- `docker-compose.yml`: Configuração para orquestrar containers Docker.
- `Dockerfile`: Instruções para construir a imagem Docker da aplicação.
- `requirements.txt`: Dependências do projeto.

## Configuração do Projeto

### 1. Configurar o Banco de Dados

Certifique-se de configurar as credenciais e o endereço do banco de dados MySQL no arquivo `docker-compose.yml` e nas
variáveis de ambiente da aplicação.

### 2. Construir e Rodar a Aplicação

1. **Construa a imagem Docker e inicie os containers**:
    ```bash
    docker-compose up --build
    ```

    Este comando criará a imagem Docker com base no `Dockerfile` e iniciará os containers definidos no 
`docker-compose.yml`. Inclui o container da aplicação e o container do banco de dados MySQL.

2. **Rodar as migrações do banco de dados**:
    Após iniciar os containers, execute as migrações para criar as tabelas necessárias no banco de dados:
    ```bash
    docker-compose exec cadastro-api alembic upgrade head
    ```

3. **Acessar a API**:
    A aplicação estará disponível em `http://localhost:8000`. 
Você pode acessar a documentação interativa da API em `http://localhost:8000/docs` ou `http://localhost:8000/redoc`.

## Uso da API

A API possui endpoints para realizar operações de cadastro. Aqui estão alguns exemplos de como usar a API:

- **Criar um novo cadastro**:
    - Método: `POST`
    - URL: `/usuarios/`
    - Corpo da Requisição:
      ```json
      {
        "nome": "João da Silva",
        "email": "joao@example.com",
      }
      ```

- **Listar todos os cadastros**:
    - Método: `GET`
    - URL: `/usuarios/`

- **Buscar um cadastro por ID**:
    - Método: `GET`
    - URL: `/usuarios/{id}`

- **Atualizar um cadastro**:
    - Método: `PUT`
    - URL: `/usuarios/{id}`
    - Corpo da Requisição:
      ```json
      {
        "nome": "João da Silva Atualizado",
        "email": "joao.novo@example.com",
      }
      ```

- **Excluir um cadastro**:
    - Método: `DELETE`
    - URL: `/usuarios/{id}`

## Testes

Para rodar testes, você pode adicionar um serviço de testes no Docker Compose ou executar os testes diretamente no 
seu ambiente local.

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir issues ou pull requests. 
Siga as práticas padrão de contribuição e certifique-se de que todas as alterações sejam bem testadas.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

>
> Start on September 5, 2024. Developed by Fabio Ribeiro
> 
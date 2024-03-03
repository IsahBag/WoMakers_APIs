
# WoMakers_APIs_Module

*HTTP:* HyperText Transfer Protocol
*HTTPS:* HyperText Transfer Protocol Secure (criptografia)

Client -> Proxy -> Server

*Proxy:* 'representante'responsável por ajudar a operar as camadas de comunicação entre o pedido e a resposta

**Métodos de Requisição:**

* **GET:** consulta um registro/coleção do servidor
* **POST:** envia dados para criar um novo registro no servidor
* **PUT:** envia dados para atualizar um registro existente
* **DELETE:** excluir registros do servidor
* **PATCH:** envia dados para atualizar parcialmente um registro

**Elementos presentes em todas etapas de comunicação:**

* **CONNECT:** abre conexão com o servidor remoto (link) - "end point"
* **OPTIONS:** descreve opções/critérios de comunicação para um recurso
* **TRACE:** diagnóstico durante o desenvolvimento
* **HEAD:** cabeçalho da requisição, retorna os códigos da requisição

**API - Application Programming Interface:**

* interfaces que permitem a comunicação e a integração entre diferentes aplicações de software

**Método CRUD:**

Create ----> POST
Read ----> GET
Update ----> PUT
Delete ----> DELETE

**REST - Representational State Transfer:**

* REST request -> faz a solicitação
* REST response -> traz o resultado
* endpoin -> (URI - destino)
* headers -> informações com relação ao cliente e ao servidor
* body  -> recebe o conteúdo como resposta
* response -> XML ou JSON

**WSGI (Web Server Gateway Interface):**

* é uma camada que fica entre o servidor web da aplicação

**Instalando o Flask no VS Code:**

    1.Criar o ambiente virtual pelo terminal:
      py -3 -m venv .venv
    2.Ativar o ambiente virtual:
      .\.venv\Scripts\activate
    3.Instalação do Flask
      pip install Flask

**Executando a função:**

    flask --app [nome_app] run

**Componentização:** layout padrão

*'ASGI' Asynchronous Server Getway Interface*.

**Método síncrono:** tarefas são executadas uma de cada vez

**Método assíncrono:** executa múltiplas tarefas

**Instalando o Fast API no VS Code:**

    1.Criar o ambiente virtual pelo terminal:
      py -3 -m venv .venv
    2.Ativar o ambiente virtual:
      .\.venv\Scripts\activate
    3.Instalação do Flask
      pip install "fastapi[all]"
    4.Instalação do Uvicorn
      pip install uvicorn

**Inicialização do servidor:**

    uvicorn [nome_app]:app --reload

*Biblioteca from typing import Union:* ajuda a trabalhar com funções com único argumento, o qual pode ser de mais de um tipo

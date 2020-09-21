# Base A

Destina-se ao dados pessoais. Estes estão criptografados e usando a autenticação AUTHBasic para acessa-las

## Funcionamento

O cadastro é feito através de uma requisão POST, com o conteúdo/json. Este conteúdo possui as informações que serão cadastradas na base A e também informações que serão encaminhadas
para a base B;

A descoberta dos micros serviços esta disponível pelo servidor eureka. Cada micro-serviço se registra nesse servidor.

### Modelo de requisição

O formato de requisição é JSON e abaixo a estrutura nescessária para um cadastro bem sucedido:

\\TODO fazer estrutura da requisição de cadastro
```json
  {
    "teste": "teste"
  }
```

## Ojetivos:

* [ ] - Armazenar no banco de dados através de requisição POST;
* [ ] - Processar dados financeiro para encaminhar à Base B;
* [x] - Disponibilizar as informações através do cpf;
* [x] - Proteger acesso as infrmações com algum tipo de autênticação;
* [x] - Criptografar dados do banco de dados. Esta tratativa deve ser feita na aplicação;

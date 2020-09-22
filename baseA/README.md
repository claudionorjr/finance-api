# Base A

Destina-se ao dados pessoais. Estes estão criptografados e usando a autenticação AUTHBasic para acessa-las

## Funcionamento

O cadastro é feito através de uma requisão POST, com o conteúdo/json. Este conteúdo possui as informações que serão cadastradas na base A e também informações que serão encaminhadas
para a base B;

A descoberta dos micros serviços esta disponível pelo servidor eureka. Cada micro-serviço se registra nesse servidor.

### Modelo de requisição

O formato de requisição é JSON, abaixo segue as estruturas nescessárias:

#### Cadastro

* Método: __POST__
* Path: __/api/v1/personal/register__

```json
    {
    "cpf": "88.888.888-89",
    "rg" : "5.555.555-8",
    "dataNascimento": "2020-02-02",
    "nomeCompleto" : "Nome Completo",
    "endereco" : "Rua da Pessoa",
    "listaDividas" : [
      {
        "estabelecimento" : "Nome do estabelecimento",
        "data_divida" : "Data do vencimento da divida",
        "valor" : "valor da dívida: Float"
      }
    ],
    "listaAtivos" : [
      {
        "tipo" : "nome do tipo; exemplo: Apartamento",
        "valor" : "valor do ativo: Float"
      }
    ],
    "listaRendas" : [
      {
        "tipo" : "tipo da renda",
        "valor" : "valor da renda: Float"
      }
    ] 
  }
```
#### Consulta por CPF

* Método: __GET__
* URL: __/api/v1/personal/{cpf}__

Retorno:
```json
  {
    "dadosPessoais": {
        "cpf": "88.888.888-89",
        "data_nascimento": "2020-02-02",
        "endereco": "Rua da Pessoa",
        "nome_completo": "Nome Completo",
        "rg": "5.555.555-8"
    },
    "rendas": [
        {
          "tipo": "tipo da renda",
          "valor": 2500
        }
      ],
  }
```

## Ojetivos:

* [x] - Armazenar no banco de dados através de requisição POST;
* [x] - Processar dados financeiros para encaminhar à Base B;
* [ ] - Registrar micro-serviço no eureka server
* [x] - Disponibilizar as informações através do cpf;
* [x] - Proteger acesso as infrmações com algum tipo de autênticação;
* [x] - Criptografar dados do banco de dados. Esta tratativa deve ser feita na aplicação;;

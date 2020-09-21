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
* URL: __http://hostname:5000/api/v1/cadastro__

```json
  {
    "cpf": "88.888.888-88",
    "nomeCompleto" : "Nome Completo",
    "endereco" : "Rua da Pessoa",
    "dividas" : [
      {
        "estabelecimento" : "Nome do estabelecimento",
        "data_divida" : "Data do vencimento da divida",
        "valor" : "valor da dívida: Float",
      }
    ],
    "idade" : "idade da pessoa",
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
    ], 
  }
```
#### Consulta por CPF

* Método: __GET__
* URL: __http://hostname:5000/api/v1/infocpf/{cpf}__

Retorno:
```json
  {
    "cpf" : "88.888.888-88",
    "nome" : "Nome da pessoa",
    "endereco" : "Endereço da Pessoa",
    "rendas": [
      "tipo" : "Nome do tipo da renda",
      "valor" : "Valor da Renda: Float"
    ]
  }
```

## Ojetivos:

* [ ] - Armazenar no banco de dados através de requisição POST;
* [ ] - Processar dados financeiros para encaminhar à Base B;
* [x] - Disponibilizar as informações através do cpf;
* [x] - Proteger acesso as infrmações com algum tipo de autênticação;
* [x] - Criptografar dados do banco de dados. Esta tratativa deve ser feita na aplicação;;

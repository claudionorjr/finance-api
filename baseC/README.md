# Base C

Serve como consulta em um determinado cpf. Basicamente são as transações realizadas.

## Funcionamento

Os dados disponíveis nesta base, dependem das informações que serão encaminhadas pela Base B.

A descoberta dos micros serviços está disponivel pelo servidor eureka. Cada micro-serviço se registra nesse servidor.

### Modelos de requisições:

o formato de requisição é json, abaixo segue as estruturas nescessárias:
a
#### Cadastro

TODO fazer estrutura da requisição de cadastro
```json
  {
    "teste": "teste"
  }
```

#### Informações de consultas realizadas no CPF 

#### Informações de compra realizadas no CPF

#### Movimentações financeiras no CPF

## Ojetivos:

* [ ] - Armazenar no banco de dados através de requisição POST com os dados de origem da base B;
* [ ] - Armazenar no banco de dados através de requisição POST transações terceiros;
* [ ] - Disponibilizar consultas feitas no cpf;
* [x] - Disponibilizar as informações de compras no cartão de crédito através do cpf;
* [x] - Disponibilizar as informações de movimentações através do cpf; 

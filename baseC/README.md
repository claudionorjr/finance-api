# Base C

Serve como consulta em um determinado cpf. Basicamente são as transações realizadas.

## Funcionamento

Os dados disponíveis nesta base, dependem das informações que serão encaminhadas pela Base B.

A descoberta dos micros serviços está disponivel pelo servidor eureka. Cada micro-serviço se registra nesse servidor.

### Modelos de requisições:

o formato de requisição é json, abaixo segue as estruturas nescessárias:

#### Cadastro consultas

* Método: __POST__
* Path: __/api/v1/register/cpf/query__

```json
  {
  
  }
```


#### Informações de consultas realizadas no CPF 

* Método: __GET__
* Path: __/api/v1/query/cpf/info/<cpf>__

```json
  {
  
  }
```

#### Informações de compra realizadas no CPF

* Método: __GET__
* Path: __/api/v1/transaction/cpf/info/<cpf>__

```json
  {
  
  }
```

#### Movimentações financeiras no CPF

* Método: __GET__
* Path: __/api/v1/moviment/cpf/info/<cpf>__

```json
  {
  
  }
```

## Ojetivos:

* [ ] - Armazenar no banco de dados através de requisição POST com os dados de origem da base B;
* [ ] - Armazenar no banco de dados através de requisição POST transações terceiros;
* [ ] - Disponibilizar consultas feitas no cpf;
* [x] - Disponibilizar as informações de compras no cartão de crédito através do cpf;
* [x] - Disponibilizar as informações de movimentações através do cpf; 

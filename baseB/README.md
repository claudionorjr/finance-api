# Base B

Destina-se ao dados usados no calculo de analise de risco usado em instituições financeiras. Estes estão criptografados e usando a autenticação AUTHBasic para acessa-las

## Funcionamento

Os dados disponíveis nesta base, dependem das informações que serão encaminhadas pela Base A. Disponibiliza a consulta de outras empresas para verificar o risco envolvido em uma operação de crédito.

A cada requisição de consulta pelo cpf, é encaminhado as informações de origem da consulta e data para a base C;

Tem possibilidade de extrair todos os dados para Machine Learn;

A descoberta dos micros serviços está disponivel pelo servidor eureka. Cada micro-serviço se registra nesse servidor.

### Modelos de requisições:

o formato de requisição é json, abaixo segue as estruturas nescessárias:

#### Cadastro


* Método: __POST__
* URL: __http://hostname:5001/api/v1/cadastro__

```json
  {
  
  }
```

#### Informações por CPF


* Método: __GET__
* URL: __http://hostname:5001/api/v1/infocpf/{cpf}__

Retorno:
```json
  {
    
  }
```

#### Todas as Informações


* Método: __GET__
* URL: __http://hostname:5001/api/v1/allinfo

Retorno:
```json
  {
    
  }
```

## Ojetivos:

* [ ] - Armazenar no banco de dados através de requisição POST com os dados de origem da base A;
* [ ] - Processar dados de consulta como origem e data para encaminhar à Base C servindo como relatório a cada requisição;
* [ ] - Disponibilizar as informações através do cpf;
* [ ] - Disponibilizar todas as informações; 
* [x] - Proteger acesso as infrmações com algum tipo de autênticação;
* [x] - Criptografar dados do banco de dados. Esta tratativa deve ser feita na aplicação;

# Finance API

O objetivo é trabalhar a interação de micro-serviços, armazenando, processando e disponibilizando os dados. É considerado trabalhar com as melhores praticas de TI.

O repositório esta dividido em três micro-serviços. Estes interagem entre si, através do uso de API. Cada serviço lida com dados pessoais financeiros.

## Descrições dos Projetos
### Projeto Base A:
Os dados disponibilizado neste projeto, lida com informações pessoais, como:

* Nome Completo
* CPF
* RG
* Data de Nascimento
* As principais Rendas

Como são dados críticos, é de extrema importanção que a aplicação tenha a preocupação com essas informações trabalhando com a segurança e a integridade. Seguindo esta linha, foi utilizado a crytptografia dos dados, esta feita na aplicação, possibilitando a troca do banco de dados posteriormente. A forma de autenticação é com AUTHBasic, sabendo que não é a melhor forma de proteção. A solução seria gerar tokens a cada requisição, com tempo de expiração.

## Projeto Base B:

Da mesma maneira que o projeto Base A, o projeto Base B, também lida com dados críticos. Foi seguido a mesma linha de raciocinio na parte de segurança e integridade dos dados. Este dados são:

* Idade
* Lista de Bens
* Endereço
* Fontes de Renda
* Dívidas

Este serviço seria para integrações de empresas que queiram utilizar destes dados, para analizar financeiramente seus clientes.

Os dados Pessoais, fazem requisições para a Base A, a fim de obter estas informações. Este vinculo entre os dados, é feito pelo id da pessoa na base A, com isso, este projeto disponibiliza os dados, com o intuido de utilizar o aprendizado de maquina(Machine Learn). Estes dados são disponibilizado de forma que, não seja possível identificar de qual é a pessoa. Todas as requisições exigem a autenticação conforme o projeto Base A.

A cada consulta de empresas, é feita uma requisição para o projeto Base C, que informa qual empresa fez a consulta nos dados fornecidos.

## Projeto Base C
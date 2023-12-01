# Documentação para reserva de Hotéis usando REST APIs

Este projeto abrange a implementação prática de recursos fornecidos pelo REST API para Reserva e Comparação de Hotéis, destacando exemplos claros do uso desses recursos. O desenvolvimento foi conduzido de maneira abrangente, utilizando diversas ferramentas essenciais, como REST API, SQLite3, SQLAlchemy, Gunicorn, Nginx, e aproveitando os recursos da Cloud AWS. O teste completo e bem-sucedido foi conduzido através do Postman.

O fluxo do projeto inicia com o registro no servidor, seguido por uma confirmação por e-mail, realização do login, e, posteriormente, a obtenção de um token que concede a autorização necessária para realizar operações CRUD. A aplicação demonstra de forma simulada a criação, remoção e atualização de cadastros de hotéis no servidor designado.

Essa abordagem assegura a robustez e segurança do sistema, uma vez que cada etapa do processo é validada antes de conceder autorizações significativas. O uso efetivo de ferramentas como SQLite3 e SQLAlchemy garante uma gestão eficiente do banco de dados, enquanto Gunicorn e Nginx aprimoram a performance e a escalabilidade da aplicação.

O sucesso no teste conduzido pelo Postman valida a eficácia do projeto, garantindo que todas as operações CRUD possam ser realizadas de maneira segura e eficiente. Este projeto não apenas destaca a implementação prática de recursos do REST API, mas também reflete as melhores práticas em termos de segurança, desempenho e escalabilidade.

O processo pode ser observado abaixo:

# 1. Cadastro de Usuário
### Requisição e Resposta
Exemplo de Requisição para cadastrar um novo usuário e status code 201 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/85942856-1b2a-489b-9952-2e72d54a0e06.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Cadastrando o mesmo email duas vezes e status code 400 como insucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/61300db4-fa7e-42fb-9631-492fcd88f292" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Conferindo email
Após cadastrar usuário, precisamos confirmar o cadastro no email.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/1d4c9b6a-ece5-4fc8-88c7-2e8d71d7ad48" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Conferindo cadastro
Após confirmar o cadastro, será encaminhando para um link com a seguinte mensagem abaixo:

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/2e7d18d0-70e0-4b6a-ac9d-138a887c1901" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>



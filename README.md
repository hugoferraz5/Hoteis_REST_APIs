# Documentação para reserva de Hotéis usando REST APIs

Este projeto abrange a implementação prática de recursos fornecidos pelo REST API para Reserva e Comparação de Hotéis, destacando exemplos claros do uso desses recursos. O desenvolvimento foi conduzido de maneira abrangente, utilizando diversas ferramentas essenciais, como **REST API, SQLite3, SQLAlchemy, Gunicorn, Nginx**, e aproveitando os recursos da **Cloud AWS**. O teste completo e bem-sucedido foi conduzido através do **Postman**.

O fluxo do projeto inicia com o registro no servidor, seguido por uma confirmação por e-mail, realização do login, e, posteriormente, a obtenção de um **token** que concede a autorização necessária para realizar operações CRUD. A aplicação demonstra de forma simulada a criação, remoção e atualização de cadastros de hotéis no servidor designado.

Essa abordagem assegura a robustez e segurança do sistema, uma vez que cada etapa do processo é validada antes de conceder autorizações significativas. O uso efetivo de ferramentas como SQLite3 e SQLAlchemy garante uma gestão eficiente do banco de dados, enquanto Gunicorn e Nginx aprimoram a performance e a escalabilidade da aplicação.

O sucesso no teste conduzido pelo Postman valida a eficácia do projeto, garantindo que todas as operações CRUD possam ser realizadas de maneira segura e eficiente. Este projeto não apenas destaca a implementação prática de recursos do REST API, mas também reflete as melhores práticas em termos de segurança, desempenho e escalabilidade.

- Parâmetros para consulta
  - cidade ⇒ Filtrar hotéis pela cidade escolhida. Padrão: Nulo
  - estrelas_min ⇒ Avaliações mínimas de hotéis de 0 a 5. Padrão: 0
  - estrelas_max ⇒ Avaliações máximas de hotéis de 0 a 5. Padrão: 5
  - diaria_min ⇒ Valor mínimo da diária do hotel de R$ 0 a R$ 10.000,00. Padrão: 0
  - diaria_max ⇒ Valor máximo da diária do hotel de R$ 0 a R$ 10.000,00. Padrão: 10000
  - limit ⇒ Quantidade máxima de elementos exibidos por página. Padrão: 50
  - offset ⇒ Quantidade de elementos pular (geralmente múltiplo de limit). Padrão: 0

A API pode ser acessada por esse link:  <a href="http://ec2-204-236-199-247.compute-1.amazonaws.com/">RedeHoteis</a>

Podemos observar abaixo as requisições:

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

# 2. Login de Usuário
### Requisição e Resposta
Exemplo de Requisição para logar o usuário e status code 400 como insucesso, pois o usuário não confirmou cadastro por email.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/2b73e77a-4eeb-40c8-a1e6-9bd18cf72c3c" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Exemplo de Requisição para logar o usuário e status code 200 como sucesso, após o usuário confirmar cadastro por email. Então, é gerado um token de acesso à API.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/3fe28184-28b4-4abc-9af4-78960cc1ace6" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Exemplo de Requisição para logar um novo usuário que não foi cadastrado ainda e status code 401 como insucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/001b0014-220f-46cd-ac5e-2f36b6ad5776" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 3. Loggout de Usuário
### Requisição e Resposta
Exemplo de Requisição para deslogar o usuário  e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/adc8aaf3-787d-4a59-928c-51733201eba8" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 4. Criar Hotel
### Requisição e Resposta
Exemplo de Requisição para criar um novo hotel e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/3b7cd30e-4a69-4b80-a3b9-1253cb79796f" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Exemplo de Requisição para criar um novo hotel associado à um site que não existe e status code 400 como insucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/5dfc84d5-7b19-4e6c-8c96-45d1e045ff08" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 5. Atualizar Hotel
### Requisição e Resposta
Exemplo de Requisição para atualizar um hotel e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/8716928b-e2b0-4a08-a56e-93f4026d2146" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 6. Deletar Hotel
### Requisição e Resposta
Exemplo de Requisição para deletar um hotel criado e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/a05513c8-56e3-4339-90bf-1d036d1ee0c1" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 7. Consultar Hotéis
### Requisição e Resposta
Exemplo de Requisição para consultar todos os hotéis criados e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/b73808dd-1d24-4286-969e-0dc0d9a8f2cf" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Exemplo de Requisição para consultar um determinado hotel e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/a4a952b1-3e96-41b7-b5f4-adf4634ae461" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Exemplo de Requisição para consultar um determinado hotel que não existe e status code 404 como insucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/c2f6c62a-e411-4b62-952e-6583d38ea915" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Exemplo de Requisição para consultar hotéis com filtros e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/08870b85-4234-4f54-93c7-c83a0f1a1c2c" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 8. Criar Site
### Requisição e Resposta
Exemplo de Requisição para criar um novo site para ser associado à um hotel e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/3821f222-9473-47de-ac42-e7f9c68849c6" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 9. Consultar Dados de Usuário
### Requisição e Resposta
Exemplo de Requisição para consultar dados do usuário cadastrado e que ja confirmaram cadastros nos emails(**ativado = true**), e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/03918943-3c59-48c3-b18f-46e263a546b0" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

### Requisição e Resposta
Exemplo de Requisição para consultar dados do usuários cadastrados, mas que não confirmaram cadastros nos emails(**ativado = false**), e status code 200 como sucesso.

<img src="https://github.com/hugoferraz5/Hoteis_REST_APIs/assets/91911052/9d571498-9050-4716-8efc-55eebd2b9e0d" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>











# M5 - Kenzie Buster

## Instalação dos pacotes de teste

-   Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:

```shell
pip list
```

-   Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

## A partir disso, prossiga com os passos:

### 1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows(powershell):
.\venv\Scripts\activate

# windows(git bash):
source venv/Scripts/activate
```

### 3. Instale o pacote `pytest-testdox`:

```shell
pip install -r requirements.txt
```

### 4. Agora é só rodar os testes no diretório principal do projeto:

```shell
pytest --testdox -vvs
```

## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

-   Rodando testes da Tarefa 1:

```python
pytest --testdox -vvs tests/tarefas/t1/
```

-   Rodando testes da Tarefa 2:

```python
pytest --testdox -vvs tests/tarefas/t2/
```

-   Rodando testes da Tarefa 3:

```python
pytest --testdox -vvs tests/tarefas/t3/
```

-   Rodando testes da Tarefa 4:

```python
pytest --testdox -vvs tests/tarefas/t4/
```

### Para iniciar o servidor:

```
python manage.py runserver
```

### Rotas:

## url: http://127.0.0.1:8000/

```
Endpoint: api/users/
Verbo HTTP: POST
Objetivo: Cadastrar usuário
```

![body_user](https://user-images.githubusercontent.com/103224186/230800426-50b7f0f9-a06c-4479-9354-16dde200da91.png)

```
Endpoint: api/users/login/
Verbo HTTP: POST
Objetivo: Login usuário
```

![body_login](https://user-images.githubusercontent.com/103224186/230800532-556e3226-e930-4258-a5ee-94780613f685.png)

```
Endpoint: api/users/<user_id>/
Verbo HTTP: GET
Objetivo: Filtragem de usuário
```

```
Endpoint: api/users/<user_id>/
Verbo HTTP: PATCH
Objetivo: Atualização de pet
```

Movies

```
Endpoint: api/movies/
Verbo HTTP: POST
Objetivo: Cadastrar filmes
```

![body_create_movie](https://user-images.githubusercontent.com/103224186/230801297-fdf34671-f9cf-4bdb-9dba-74f4fa42b9fa.png)

```
Endpoint: api/movies/
Verbo HTTP: GET
Objetivo: Listagem de livros
```

```
Endpoint: api/movies/<movie_id>/
Verbo HTTP: GET
Objetivo: Filtragem de filme
```

```
Endpoint: api/movies/<movie_id>/
Verbo HTTP: DELETE
Objetivo: Deleção de filme
```

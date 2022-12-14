# Seazone-Code-Challenge-Back-End-Python
API para gerenciar a locaΓ§Γ£o de imΓ³veis

---

# Tecnologias a ser utilizadas

  * Docker;
  * Python;
  * Django;
  * Django Rest Framework;
  * PostegreSQL.

---

<details>
  <summary><strong>π€·π½ββοΈ Como rodar o projeto</strong></summary><br />
  1. Clone o repositΓ³rio - `git@github.com:Murilo-Carrijo/Seazone-Code-Challenge-Back-End-Python.git`
  
  2. Entre na pasta do repositΓ³rio que vocΓͺ acabou de clonar - `cd Seazone-Code-Challenge-Back-End-Python`

  3. Verifique se a porta 8000 estΓ‘ disponΓ­vel, pois o projeto estΓ‘ configurado para todar nesta porta;

  4. O porjeto foi desenvolvido utilizando Docker - rode o comando `docker-compose up`;

  5. Abra o navegador e acesse: `http://127.0.0.1:8000/api/docs`;

  6. Pronto, agora vocΓͺ pode testar os endpoints criados para esse projeto.
</details>

<details>
  <summary><strong>π§± Estrutura do Projeto</strong></summary><br />

  ```
  .
  βββ .github
  βΒ Β  βββ workflows
  βΒ Β      βββchecks.yml
  βββ app
  βΒ Β  βββ app
  β   β   βββ __init__.py
  β   β   βββ asgi.py
  β   β   βββ settings.py
  β   β   βββ urls.py
  β   β   βββ wsgi.py 
  βΒ Β  βββ core
  β   β   βββ management
  |   |   |   βββ commands
  |   |   |   |    βββ __init__.py
  |   |   |   |    βββ  wait_for_db.py
  |   |   |   βββ __init__.py
  β   β   βββ migrarions
  |   |   |   βββ __init__.py
  |   |   |   βββ 0001_initial.py
  |   |   |   βββ 0002_advertisement.py
  β   β   βββ tests
  |   |   |   βββ __init__.py
  |   |   |   βββ test_commands.py
  |   |   |   βββ test_models.py
  β   β   βββ __init__.py
  β   β   βββ admin.py
  β   β   βββ apps.py
  β   β   βββ models.py
  βΒ Β  βββ properties
  β   β   βββ tests
  |   |   |   βββ __init__.py
  |   |   |   βββ test_advertisement_api.py
  |   |   |   βββ test_properties_api.py
  β   β   βββ __init__.py
  β   β   βββ apps.py
  β   β   βββ serializers.py
  β   β   βββ urls.py
  β   β   βββ views.py
  βββ .docker-compose.yml
  βββ Dockerfile
  βββ README.md
  βββ requirements.dev.txt
  βββ requirements.txt
  ```
</details>

<details>
  <summary><strong>π  Testes UnitΓ‘rios</strong></summary><br />
  O porjeto foi desenvolvido utilizando o metodo TDD (Test Driven Development), ou seja, foram desenvovidos testes antes da implementaΓ§Γ£o das funΓ§Γ΅es.
  Esse metodo tem como objetivo grarantir a qualidade do projeto e reduzir a quantidade de 'bugs'.

  Para rodar os testes localmente basta realizar o comando abaixo:  
  ```bash
  docker-compose run --rm app sh -c "python manage.py test"
  ```
</details>

<details>
  <summary><strong>π Linter</strong></summary><br />

  Para garantir a qualidade do cΓ³digo, foi utilizado neste projeto o linter `Flake8`.
  Assim o cΓ³digo estarΓ‘ alinhado com as boas prΓ‘ticas de desenvolvimento, sendo mais legΓ­vel
  e de fΓ‘cil manutenΓ§Γ£o! Para rodΓ‘-lo localmente no projeto, execute o comando abaixo:

  ```bash
  python3 -m flake8
  ```
</details>

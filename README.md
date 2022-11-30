# Seazone-Code-Challenge-Back-End-Python
API para gerenciar a locação de imóveis

---

# Tecnologias a ser utilizadas

  * Docker;
  * Python;
  * Django;
  * Django Rest Framework;
  * PostegreSQL.

---

<details>
  <summary><strong>🤷🏽‍♀️ Como rodar o projeto</strong></summary><br />
  1. Clone o repositório - `git@github.com:Murilo-Carrijo/Seazone-Code-Challenge-Back-End-Python.git`
  
  2. Entre na pasta do repositório que você acabou de clonar - `cd Seazone-Code-Challenge-Back-End-Python`

  3. Verifique se a porta 8000 está disponível, pois o projeto está configurado para todar nesta porta;

  4. O porjeto foi desenvolvido utilizando Docker - rode o comando `docker-compose up`;

  5. Abra o navegador e acesse: `http://127.0.0.1:8000/api/docs`;

  6. Pronto, agora você pode testar os endpoints criados para esse projeto.
</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />

  ```
  .
  ├── .github
  │   └── workflows
  │       └──checks.yml
  ├── app
  │   ├── app
  │   │   ├── __init__.py
  │   │   ├── asgi.py
  │   │   ├── settings.py
  │   │   ├── urls.py
  │   │   └── wsgi.py 
  │   ├── core
  │   │   ├── management
  |   |   |   ├── commands
  |   |   |   |    ├── __init__.py
  |   |   |   |    └──  wait_for_db.py
  |   |   |   └── __init__.py
  │   │   ├── migrarions
  |   |   |   ├── __init__.py
  |   |   |   ├── 0001_initial.py
  |   |   |   └── 0002_advertisement.py
  │   │   ├── tests
  |   |   |   ├── __init__.py
  |   |   |   ├── test_commands.py
  |   |   |   └── test_models.py
  │   │   ├── __init__.py
  │   │   ├── admin.py
  │   │   ├── apps.py
  │   │   └── models.py
  │   ├── properties
  │   │   ├── tests
  |   |   |   ├── __init__.py
  |   |   |   ├── test_advertisement_api.py
  |   |   |   └── test_properties_api.py
  │   │   ├── __init__.py
  │   │   ├── apps.py
  │   │   ├── serializers.py
  │   │   ├── urls.py
  │   │   └── views.py
  ├── .docker-compose.yml
  ├── Dockerfile
  ├── README.md
  ├── requirements.dev.txt
  └── requirements.txt
  ```
</details>

<details>
  <summary><strong>🛠 Testes Unitários</strong></summary><br />
  O porjeto foi desenvolvido utilizando o metodo TDD (Test Driven Development), ou seja, foram desenvovidos testes antes da implementação das funções.
  Esse metodo tem como objetivo grarantir a qualidade do projeto e reduzir a quantidade de 'bugs'.

  Para rodar os testes localmente basta realizar o comando abaixo:  
  ```bash
  docker-compose run --rm app sh -c "python manage.py test"
  ```
</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, foi utilizado neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comando abaixo:

  ```bash
  python3 -m flake8
  ```
</details>

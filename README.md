# Flask Login System

Este é um exemplo básico de um sistema de login usando Flask e Flask-Login. O projeto inclui autenticação de usuário simples com funcionalidades de login e logout.

## Funcionalidades

- **Login**: Usuários podem fazer login usando um nome de usuário e senha.
- **Logout**: Usuários logados podem se desconectar.
- **Proteção de Rota**: A rota principal é protegida e só pode ser acessada por usuários autenticados.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python.
- **Flask-Login**: Extensão do Flask para gerenciar sessões de usuário.

## Como Executar o Projeto

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/LucasRialx/Flask_Login_System.git
    ```

2. **Navegue até o diretório do projeto**:

    ```bash
    cd Flask_Login_System
    ```

3. **Crie um ambiente virtual** (opcional, mas recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. **Instale as dependências**:

    ```
    pip install Flask Flask-Login
    ```

5. **Execute o servidor Flask**:

    ```
    python app.py
    ```

6. **Acesse o sistema de login**:

    Abra seu navegador e vá para `http://127.0.0.1:5000/login`.

## Estrutura do Projeto

- `app.py`: Contém a lógica principal do servidor Flask.
- `templates/`: Diretório contendo o template HTML para a página de login.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

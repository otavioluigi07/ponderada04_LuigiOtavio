# ponderadaSemana7_04

# Descrição
Este projeto faz parte do Módulo 6 do curso de Engenharia de Software. Ele consiste em um sistema de gerenciamento de usuários, onde é possível criar, listar, atualizar e excluir usuários do sistema.

# Configuração do Ambiente de Desenvolvimento
Para configurar o ambiente de desenvolvimento, siga as instruções abaixo:
- Clone o repositório
- Crie um ambiente virtual
- Ative o ambiente virtual

# Bibliotecas Utilizadas
Este projeto utiliza as seguintes bibliotecas Python:
sqlalchemy: Utilizada para interagir com o banco de dados SQL.
pytest: Utilizada para escrever e executar testes automatizados.
pytest-asyncio: Plugin para teste assíncrono com o Pytest.
pytest-anyio: Plugin para teste assíncrono com o Pytest.

# Pip install
pip install sqlalchemy
pip install pytest
pip install pytest-asyncio
pip install pytest-anyio
pip install pytest pytest-asyncio httpx
pip install openai
pip install --upgrade pydantic
pip install fastapi uvicorn[standard] sqlalchemy

# Testes
Para rodar os testes, entre na pasta TESTS, escolha a entidade de teste e dê o comando "pytest".
Obs: A entidade das histórias está completa e funcional, mas infelizmente a dos usuários está com alguns problemas que não consegui concertar.

# Nota sobre a Integração com a API do ChatGPT/OpenAI
Devido a limitações técnicas ou outras restrições, não foi possível integrar a API do ChatGPT/OpenAI neste projeto. No entanto, outras funcionalidades foram implementadas conforme especificado nos requisitos.

# Rodar o projeto
Na raiz do projeto, no terminal, digite: uvicorn main:app --reload

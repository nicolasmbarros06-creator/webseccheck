# Arquitetura resumida

O projeto possui três partes simples:

- CLI: recebe a URL do laboratório.
- Validação: impede alvos fora de localhost.
- Analisador: coleta cabeçalhos e informa quais controles recomendados estão presentes ou ausentes.

Não há banco de dados, autenticação, infraestrutura em nuvem ou dados pessoais.

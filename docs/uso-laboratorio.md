# Laboratório rápido

1. Crie um servidor HTTP local, por exemplo:
   `python -m http.server 8000`
2. Em outro terminal, instale o projeto em modo editável:
   `pip install -e ".[dev]"`
3. Execute:
   `webseccheck http://127.0.0.1:8000`
4. Observe os cabeçalhos ausentes.
5. Para estudar a correção, use um servidor de laboratório que permita adicionar cabeçalhos de resposta e compare os resultados.

O objetivo é entender a relação entre configuração HTTP e controles básicos de segurança, sem explorar sistemas externos.

# WebSecCheck

Ferramenta educacional simples para praticar conceitos iniciais de **hacking ético / segurança web**.

## Objetivo
Verificar, em um laboratório local, a presença de cabeçalhos HTTP relacionados à segurança.

## Escopo e uso autorizado
O programa aceita somente `localhost`, `127.0.0.1` ou `::1`. Ele não executa exploração, brute force, enumeração ou varredura de terceiros.

Exemplo:
```bash
python -m webseccheck http://127.0.0.1:8000
```

## Desenvolvimento
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -e ".[dev]"
pytest -q
ruff check .
```

## Estrutura
- `src/` código
- `tests/` testes automatizados
- `.github/workflows/` pipeline CI
- `docs/` documentação
- `pyproject.toml` configuração e versão

## Pipeline
O GitHub Actions executa lint, testes e uma verificação de dependências. A etapa SCA não falha o pipeline neste protótipo porque o projeto está em fase educacional; a evolução prevista é transformar vulnerabilidades críticas/altas em bloqueio.

## Limitação importante
Este projeto é destinado a laboratório próprio. Testes de segurança em sistemas de terceiros dependem de autorização explícita do responsável pelo sistema.

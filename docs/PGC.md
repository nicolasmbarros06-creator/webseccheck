# Plano de Gerenciamento de Configuração de Software (PGC)

**Projeto:** WebSecCheck  
**Responsável:** Nicolas M. de Barros  
**Repositório:** https://github.com/nicolasmbarros06-creator/webseccheck  
**Versão do documento:** 1.0  
**Data:** 28/10/2026

## 1. Objetivo

Este documento define as práticas de Gerenciamento de Configuração de Software (GCS) adotadas no projeto WebSecCheck, visando garantir organização, rastreabilidade, controle de alterações e qualidade do código.

O projeto tem como objetivo realizar verificações de segurança em aplicações web, utilizando ferramentas e práticas de desenvolvimento que auxiliam na identificação de possíveis problemas.

## 2. Itens de configuração

São considerados itens de configuração do projeto:

- Código-fonte da aplicação;
- Testes automatizados;
- Arquivos de configuração e dependências;
- Workflows de integração contínua;
- Documentação técnica, incluindo este plano;
- Regras de proteção de branches e configurações dos ambientes do GitHub.

Esses itens devem ser versionados ou documentados de forma que suas alterações possam ser rastreadas.

## 3. Controle de versão e branches

O projeto utiliza Git para controle de versão e GitHub para hospedagem do repositório.

A branch `main` representa a versão principal do projeto. Novas funcionalidades, correções e alterações na documentação devem ser desenvolvidas em branches separadas, seguindo a convenção:

- `feature/descricao`: novas funcionalidades;
- `fix/descricao`: correções;
- `docs/descricao`: alterações na documentação;
- `test/descricao`: inclusão ou alteração de testes.

As alterações devem ser submetidas por meio de Pull Requests, evitando mudanças diretas na branch principal.

## 4. Revisão e integração de alterações

Antes de integrar alterações à `main`, deve-se:

1. Criar uma branch específica para a mudança;
2. Implementar e testar a alteração;
3. Abrir um Pull Request com descrição do objetivo e das modificações;
4. Solicitar revisão de outro colaborador;
5. Verificar os resultados dos testes e das verificações automatizadas;
6. Realizar o merge somente após o cumprimento das regras configuradas no repositório.

A branch principal deve permanecer em estado estável, com alterações rastreáveis e revisadas.

## 5. Integração contínua (CI)

O projeto utiliza GitHub Actions para automatizar verificações do código.

As ferramentas previstas no processo de qualidade incluem:

- **pytest:** execução de testes automatizados;
- **Ruff:** análise estática e verificação de estilo do código Python;
- **pip-audit:** identificação de vulnerabilidades conhecidas em dependências Python.

Os resultados dessas verificações devem ser consultados antes da integração de alterações. A obrigatoriedade de aprovação dos testes para o merge depende das regras de status checks configuradas no repositório.

## 6. Ambientes

O projeto utiliza os GitHub Environments para representar as etapas de validação e liberação.

### 6.1 Staging

Ambiente destinado à validação de alterações antes da liberação. Pode ser utilizado por workflows para executar verificações e testes de homologação.

### 6.2 Production

Ambiente destinado a representar a etapa de liberação da versão considerada estável.

O ambiente deve possuir proteção de implantação com revisor obrigatório, conforme a configuração do repositório. A implantação efetiva depende da existência de um workflow que utilize esse ambiente.

## 7. Segurança e dependências

As dependências devem ser mantidas sob controle de versão, e suas atualizações devem ser avaliadas antes da integração.

A ferramenta pip-audit auxilia na identificação de vulnerabilidades conhecidas nas dependências Python. As credenciais e os segredos utilizados em automações não devem ser publicados no código-fonte.

Alterações relacionadas à segurança devem ser documentadas e verificadas antes de serem integradas à branch principal.

## 8. Versionamento e releases

As versões do projeto poderão seguir o Versionamento Semântico (SemVer), no formato `MAJOR.MINOR.PATCH`.

- **MAJOR:** alterações incompatíveis;
- **MINOR:** inclusão de funcionalidades compatíveis;
- **PATCH:** correções compatíveis.

As versões estáveis devem ser identificadas por tags Git, permitindo relacionar uma versão publicada ao respectivo estado do código.

## 9. Controle de mudanças

Toda alteração relevante deve possuir descrição clara, histórico no Git e, quando aplicável, referência a uma Issue ou Pull Request.

Mudanças nas regras de proteção, workflows, dependências e documentação devem seguir o mesmo processo de revisão adotado para o código-fonte.

## 10. Responsabilidades

O responsável pelo projeto deve manter o repositório organizado, revisar as configurações de GCS, acompanhar as verificações automatizadas e garantir que as alterações sejam rastreáveis.

Os colaboradores com permissão de escrita podem contribuir por meio de branches e Pull Requests, respeitando as regras de revisão e integração estabelecidas.

## 11. Revisão do plano

Este documento deve ser atualizado quando houver mudanças significativas na estrutura do projeto, nas ferramentas utilizadas, no fluxo de desenvolvimento ou nas regras de proteção do repositório.

**Histórico de revisão**

## Histórico de alterações

- 28/10/2026 — Revisão do plano de gestão e configuração do projeto.
| Versão | Data | Descrição |
|---|---|---|
| 1.0 | 28/10/2026 | Elaboração inicial do PGC do WebSecCheck |


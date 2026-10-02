# Mapa inicial de usos de IA

**Rodrigo Immaginario** · Material da apresentação sobre Shadow AI no Fórum de Canais e Inovação.

Um instrumento para conhecer usos declarados de IA no trabalho, preservar dúvidas e definir encaminhamentos. **Não é sistema de avaliação, auditoria, ranking ou teste de maturidade.**

- **[Orientações e metodologia](https://rodrigoimmaginario.github.io/shadow-ai-mapa-de-usos/)**
- **[Baixar a planilha v1.0](https://rodrigoimmaginario.github.io/shadow-ai-mapa-de-usos/downloads/mapa-usos-ia-v1.xlsx)**
- [Arquivo XLSX neste repositório](docs/downloads/mapa-usos-ia-v1.xlsx)
- [Perfil do autor](https://www.linkedin.com/in/rodrigoimmaginario/)

## O modelo é público. Suas respostas, não.

Baixe o arquivo e preencha em local autorizado pela sua organização. **Não envie o inventário preenchido ao autor, ao GitHub, a comentários, pull requests ou mensagens de suporte.** Não copie logs, código, nomes de clientes, contratos, senhas ou credenciais. Registre somente categorias de dados e referências internas necessárias.

O exemplo distribuído é inteiramente fictício. A planilha não transmite respostas, não tem macros, fórmulas, conexões de dados ou coleta automática. Isso não substitui as regras do aplicativo e do ambiente em que o arquivo for aberto.

## Conteúdo

Quatro abas:

1. **Comece aqui:** objetivo, cobertura e cuidados.
2. **Mapa de usos:** 80 linhas em branco, uma por uso, com 13 campos e listas de apoio.
3. **Exemplo fictício:** três registros sintéticos, separados do inventário real.
4. **Guia de campos:** orientação para cada coluna.

Ferramenta aprovada não significa qualquer uso aprovado. Registrar um uso não o autoriza. “A confirmar” é uma informação válida e diferente de “não existe”. Suspeitas de incidente seguem o processo de segurança da empresa, sem esperar a próxima revisão desta planilha.

## Publicação e privacidade

A página estática está em `docs/`, com download local do XLSX. Não há JavaScript, formulários, analytics ou recursos externos incorporados pelo autor. O GitHub Pages pode manter registros de acesso próprios da hospedagem: ausência de coleta de respostas não equivale a ausência de logs do site.

Issues e discussões não são canais de coleta de diagnósticos. Sugestões sobre a estrutura do material podem ser conversadas com o autor no LinkedIn, usando somente exemplos fictícios. Nunca envie dados internos para demonstrar uma sugestão.

## Reproduzir e testar

Requer Python 3.12 ou posterior.

```sh
python -m pip install -r requirements.txt
python src/build_workbook.py
python src/build_page.py
python -m unittest discover -s tests -v
```

Os geradores sobrescrevem somente os derivados distribuídos em `docs/`. Não execute sobre um arquivo preenchido; guarde o inventário interno fora deste repositório. As dependências são usadas na geração local, não no navegador de quem lê a página.

## Distribuição

Versão 1.0. O modelo é disponibilizado pelo autor para download e preenchimento interno. Não foi atribuída uma licença open-source ou Creative Commons nesta versão; outras permissões de redistribuição devem ser confirmadas com o autor. Repositório público, por si só, não é uma licença irrestrita de reutilização.

O material organiza perguntas e próximos passos. Não foi validado como escala científica de maturidade e não promete conformidade, segurança ou retorno financeiro.

````markdown
# ClearBank - Análise de Transações Bancárias

O objetivo do projeto é ler um arquivo CSV contendo transações bancárias, validar os dados, gerar métricas financeiras mensais, identificar transações suspeitas e exportar os resultados para um arquivo JSON.

## Funcionalidades

- Leitura de arquivos CSV utilizando o módulo nativo `csv`;
- Validação e limpeza dos dados;
- Tratamento de erros utilizando `try/except`;
- Manipulação de datas com `datetime`;
- Agrupamento das transações por mês;
- Cálculo das seguintes métricas:
  - Quantidade de transações;
  - Total de créditos;
  - Total de débitos;
  - Saldo mensal;
  - Valor médio das transações;
  - Maior transação do mês;
  - Menor transação do mês;
- Identificação de transações suspeitas (acima de R$ 10.000,00);
- Exibição de um relatório formatado no terminal;
- Exportação do relatório em `relatorio.json`.

## Requisitos opcionais implementados

- Versão alternativa utilizando **Pandas** (`analise_pandas.py`);
- Geração de gráfico com **Matplotlib** (`grafico.png`) apresentando o saldo mensal.

## Estrutura do projeto

```text
clearbank-analise/
│
├── desafio-final.ipynb      # Solução principal
├── analise_pandas.py        # Implementação utilizando Pandas
├── transacoes.csv           # Arquivo de entrada
├── relatorio.json           # Arquivo gerado após a execução
├── grafico.png              # Gráfico do saldo mensal
└── README.md
````

## Tecnologias utilizadas

* Python 3
* csv
* json
* datetime
* pandas
* matplotlib

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/clearbank-analise.git
```

### 2. Acesse a pasta

```bash
cd clearbank-analise
```

### 3. Instale as dependências opcionais

```bash
pip install pandas matplotlib
```

### 4. Execute o projeto

* Abra o notebook `desafio-final.ipynb` no Jupyter Notebook ou Google Colab e execute todas as células em ordem.

ou

* Execute a versão utilizando Pandas:

```bash
python analise_pandas.py
```

## Arquivos gerados

Após a execução do projeto são gerados:

* `relatorio.json` contendo o resumo das análises;
* `grafico.png` contendo o gráfico do saldo mensal.

## Autor

Projeto desenvolvido como parte do desafio final do módulo de Python para Análise de Dados.

```
```

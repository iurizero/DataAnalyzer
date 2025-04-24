# DataAnalyzer

Analisador de dados de cancelamento de clientes com visualizações automáticas.

## Descrição

Este projeto analisa dados de cancelamento de clientes, gerando automaticamente visualizações e análises estatísticas. O script processa um conjunto de dados de clientes e cria diversos gráficos para ajudar na compreensão dos padrões de cancelamento.

## Estrutura do Projeto

```
DataAnalyzer/
│
├── inicial.py           # Script principal de análise
├── requirements.txt     # Dependências do projeto
├── cancelamentos_sample.csv    # Arquivo de dados
└── graficos/           # Diretório com as visualizações geradas
    ├── correlacao.png
    ├── distribuicao_*.png
    └── cancelamento_*.png
```

## Funcionalidades

- Análise descritiva completa dos dados
- Mapa de correlação entre variáveis numéricas
- Distribuições de todas as variáveis numéricas
- Análise de cancelamento por categorias
- Distribuição de variáveis categóricas
- Tratamento automático de valores ausentes

## Requisitos

- Python 3.x
- pandas
- matplotlib
- seaborn

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/DataAnalyzer.git
cd DataAnalyzer
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal:
```bash
python inicial.py
```

O script irá:
1. Ler o arquivo de dados
2. Gerar análises estatísticas
3. Criar visualizações na pasta 'graficos'
4. Mostrar informações relevantes no console

## Variáveis Analisadas

- CustomerID: Identificador único do cliente
- idade: Idade do cliente
- sexo: Gênero do cliente
- tempo_como_cliente: Tempo como cliente em meses
- frequencia_uso: Frequência de uso do serviço
- ligacoes_callcenter: Número de ligações ao call center
- dias_atraso: Dias de atraso em pagamentos
- assinatura: Tipo de assinatura
- duracao_contrato: Duração do contrato
- total_gasto: Total gasto pelo cliente
- meses_ultima_interacao: Meses desde a última interação
- cancelou: Indicador de cancelamento (0 = não, 1 = sim)

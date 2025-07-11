# CBPAY Token Hodlers - Website

Este é um website desenvolvido para exibir a lista completa de hodlers do token CBPAY na rede XDB Chain.

## Características

- **Lista Completa de Hodlers**: Exibe todos os 50 hodlers do token CBPAY
- **Pesquisa por Endereço**: Permite pesquisar hodlers por endereço de carteira
- **Filtros Avançados**: Filtros por quantidade de tokens (Top 100, Top 500, acima de 1M, acima de 100K)
- **Estatísticas em Tempo Real**: Mostra total de hodlers, supply total e maior hodler
- **Design Responsivo**: Funciona perfeitamente em desktop e mobile
- **Interface Moderna**: Design elegante com gradientes e animações suaves
- **Paginação**: Navegação fácil através dos resultados
- **Links para Explorer**: Links diretos para o explorer da XDB Chain

## Estrutura dos Arquivos

```
cbpay-hodlers-website/
├── index.html          # Página principal do website
├── cbpay_holders.json   # Dados dos hodlers em formato JSON
└── README.md           # Esta documentação
```

## Como Usar

### Opção 1: Servidor Local
1. Abra um terminal na pasta do projeto
2. Execute: `python3 -m http.server 8080`
3. Acesse: `http://localhost:8080`

### Opção 2: GitHub Pages
1. Faça upload dos arquivos para um repositório no GitHub
2. Ative o GitHub Pages nas configurações do repositório
3. Configure para usar a pasta raiz como fonte
4. O website estará disponível no seu domínio do GitHub Pages

### Opção 3: Qualquer Servidor Web
1. Faça upload dos arquivos para qualquer servidor web
2. Certifique-se de que o servidor suporta arquivos HTML e JSON
3. Acesse o `index.html` através do navegador

## Funcionalidades

### Pesquisa
- Digite qualquer parte do endereço de carteira no campo de pesquisa
- A pesquisa é feita em tempo real conforme você digita
- Não diferencia maiúsculas de minúsculas

### Filtros
- **Todos os Hodlers**: Mostra todos os 50 hodlers
- **Top 100**: Mostra os primeiros 100 hodlers (limitado a 50 neste caso)
- **Top 500**: Mostra os primeiros 500 hodlers (limitado a 50 neste caso)
- **Acima de 1M CBPAY**: Mostra apenas hodlers com mais de 1 milhão de tokens
- **Acima de 100K CBPAY**: Mostra apenas hodlers com mais de 100 mil tokens

### Estatísticas
- **Total de Hodlers**: Número total de carteiras com tokens CBPAY
- **Supply Total**: Soma total de todos os tokens CBPAY em circulação
- **Maior Hodler**: Quantidade de tokens do maior hodler

## Dados

Os dados são carregados do arquivo `cbpay_holders.json` que contém:
- Endereço da carteira
- Saldo em tokens CBPAY

O website calcula automaticamente:
- Ranking dos hodlers
- Percentagem de posse em relação ao supply total
- Estatísticas gerais

## Atualização dos Dados

Para atualizar os dados dos hodlers:
1. Substitua o arquivo `cbpay_holders.json` pelos dados mais recentes
2. Mantenha o mesmo formato JSON:
```json
[
    {
        "address": "ENDEREÇO_DA_CARTEIRA",
        "balance": 123456789.0
    }
]
```

## Tecnologias Utilizadas

- **HTML5**: Estrutura da página
- **CSS3**: Estilização com gradientes, animações e design responsivo
- **JavaScript**: Lógica de pesquisa, filtros e paginação
- **JSON**: Formato de dados para os hodlers

## Compatibilidade

- Navegadores modernos (Chrome, Firefox, Safari, Edge)
- Dispositivos móveis e tablets
- Não requer bibliotecas externas

## Personalização

### Cores
As cores podem ser alteradas no CSS:
- Gradientes principais: `#6a11cb` e `#2575fc`
- Cor de destaque: `#4299e1`
- Fundo escuro: `#1a1a2e`

### Paginação
O número de itens por página pode ser alterado na variável `itemsPerPage` no JavaScript.

### Auto-refresh
O website recarrega automaticamente a cada hora. Este comportamento pode ser alterado ou removido no JavaScript.

## Suporte

Para questões ou sugestões relacionadas ao website, consulte a documentação da XDB Chain ou a comunidade CBPAY.

## Links Úteis

- [XDB Chain Explorer](https://explorer.xdbchain.com)
- [XDB Chain Horizon API](https://horizon.livenet.xdbchain.com)
- [Repositório Original CBPAY Stats](https://github.com/CBPAY-stats/CBPAY_stats)

---

Website desenvolvido para a comunidade CBPAY • Dados fornecidos pela XDB Chain Horizon API


# Event-Driven Calculator (Calculadora baseada em Eventos)

## Mas, porque?

Este é um projeto pessoal, construído com a finalidade de ser uma fonte de
aprendizado de diversos tópicos que, na minha opinião, possuem alguma
importância ou são interessantes.

> Este projeto será palco para os seguintes temas:
> - Orientação a objetos
> - Arquitetura baseada em eventos
> - Acoplamento de código
> - Interface gráfica
> - Design Patterns
> - Legibilidade e manutenção de código
> - Testes automatizados

No mais, espero que se divirtam tanto quanto eu me divirto enquanto tento
expandir este projeto, adicionando mais funcionalidades e melhorando o código.

---

## Documentação e idioma

Tentarei documentar o máximo possível.

Manterei toda a documentação do projeto (dentro e fora do código) em português,
por motivos de preguiça, e para que brasileiros interessados no projeto que
possuam menor domínio do inglês se sintam mais a vontade com a leitura.
Porém, aconselho fortemente o aprendizado e prática do inglês.

Os nomes dos elementos que compõem a aplicação (classes, funções, etc) estarão
em inglês, por uma questão estética, para que fique mais agradável a leitura do
código, evitando misturar português e inglês. Me causaria arrepios escrever um
trecho como este:

````py
for pessoa in lista_funcionarios:
    yield pessoa.get('sobrenome').lower()
````

---

## Itens a serem implementados

### Interface gráfica
- Dimensionamento automático da janela
- Tamanho padrão para os botões
- Pop-up de erro
- Histórico de operações
- Entrada de números negativos
- Entrada de números fracionários
- Entrada em notação científica

### Operações
#### Elementares e extensões
- ~~Adição~~
- ~~Subtração~~
- ~~Multiplicação~~
- ~~Divisão~~
- Fatorial
- Porcentagem
- Radiciação
- Potenciação
- Logaritmação

#### Sequências e progressões
- Somatório
- Produtório
- Fibonacci
- Progressão Aritmética
- Progressão Geométrica

#### Análise combinatória
- Arranjos
- Combinações
- Permutações
- Números Binomiais

### Arquitetura baseada em Eventos
- Barramento de eventos: Broker/Mediador
- Modelo de entrega: Fila/Tópico
- Assíncronia entre componentes
- Transferência de estado
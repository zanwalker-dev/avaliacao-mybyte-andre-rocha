# README - Desafio MyByte

## 📝 Sobre o Desafio

Este repo contém minha solução para o desafio técnico proposto pela MyByte, formado por dois testes:

1. **Teste 1**: Formulário estilizado (Front-end)
2. **Teste 2**: Cálculos financeiros (Back-end/Python)

## ✨ Teste 1 - Formulário Estilizado

### Objetivo
Cirar um formulario visualmente agradável com os seguintes criterios:

- ✅ Fundo da página na cor preta
- ✅ Campos de texto e botões com cantso arredondados
- ✅ Fonte clara e contraste apropriado para leitura
- ✅ O formulário não precisa funcionar (sem envio de dados)
- ✅ Desenvolvido apenas com HTML, CSS e JavaScript puro
- ✅ Código bem estruturado, limpo e organizado

### Tecnologias Utlizadas
- HTML5
- CSS3
- JavaScript Vanilla

### Como Visualizar
1. Abra o arquivo `index.html` em qualquer navegador moderno
2. Não é necessário servidor - funciona com file://

## 🧮 Teste 2 - Cálculos Financeiros (Python)

### Objetivo
Criar um script em Python que resolva três cálculos básicos de matemática financeira:

1. **Juros Simples**
   - Fórmulas:
     - J = C × i × t
     - M = C + J
   - Onde:
     - C = capital inicial
     - i = taxa de juros (ao mês)
     - t = tempo (em meses)
     - J = valor dos juros
     - M = montante final

2. **Juros Compostos**
   - Fórmulas:
     - M = C × (1 + i)ᵗ
     - J = M − C

3. **Valor Presente de uma Parcela Futura**
   - Fórmula:
     - VP = VF / (1 + i)ᵗ

### Requisitos Implementados
- ✅ Usar Python 3
- ✅ Funções separadas para cada cálculo
- ✅ Código organizado para execução via terminal
- ✅ Comentários para facilitar a leitura

### Como Executar
1. Certifique-se de ter Python 3 instalado
2. Execute no terminal:
   ```bash
   python3 main.py
   ```
3. Siga as instruções no menu interativo

## 📂 Estrutura do Repositório
```
/
├── Teste1-Formulario/       # Pasta do Teste 1
│   ├── index.html           # Arquivo principal do formulário
│   ├── style.css            # Estilos do formulário
│   └── script.js            # Comportamentos do formulário
│
├── Teste2-Python/           # Pasta do Teste 2
│   ├── main.py              # Menu  interativo com script dos calculos
│   └── calculos_testes.ipynb  # TEstes que realizei com as funções isoladas
│
└── README.md                # Este arquivo
```

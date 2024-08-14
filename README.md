# TrackNOW
Este é um simples programa que rastreia gastos.

# Instalar
> tenha o python instalado (;

Clone o repositório pelo terminal:
```fish
git clone https://github.com/imalisoon/tracknow-cli.git
```

Navegue pelo diretório e execute o programa:
```fish
cd tracknow-cli/

python main.py
```

# Fotos

# Sobre o projeto
Esse pequeno programa foi desenvolvido seguindo o padrão arquitetural **MVC**.

> *MVC* instiga a divisão de responsabilidades de um programa separando-o em camadas. model(M) camada de manipulação de dados, view(V) camada de apresentação e controller(C) camada de controle que intermedeia os relacionamentos.

## Modelo dos dados
Os modelos tem uma classe *Manager* que se encarrega de armazenar e gerenciar os dados.

- Categoria(*CategoryModel*)
    - Nome: *str*

- Fatura(*IncomeModel* ou *ExpenseModel*)
    - Nome: *str*
    - Valor: *float*
    - Categoria: *CategoryModel*
    - Tipo (Renda ou Despesa)

## Funcionalidades
- Criar, listar e deletar *categorias*.
- Criar, listar e deletar *faturas*

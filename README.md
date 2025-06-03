# 🤖 Automação de Cadastro de Produtos com PyAutoGUI | Intensivão Python Hashtag Programação

Este projeto foi desenvolvido durante o **Intensivão de Python da Hashtag Programação (2025)**. Ele realiza uma automação completa do processo de login e cadastro de produtos em um sistema online, utilizando dados de um arquivo CSV e a simulação de ações humanas com **PyAutoGUI**.

## 🧠 O que o projeto faz?

- Abre automaticamente o navegador **Opera**.
- Acessa a página de login do sistema de cadastro de produtos.
- Realiza o **login automático** com e-mail e senha.
- Lê os dados do arquivo `produtos.csv`.
- Realiza o **cadastro automatizado** de todos os produtos da planilha, preenchendo os campos um por um.

> A planilha deve estar no mesmo diretório do script Python.

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pandas](https://pandas.pydata.org/)
- [Time (módulo nativo)](https://docs.python.org/3/library/time.html)

## 💻 Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/isaaczinrs2/PythonPowerUp.git
cd PythonPowerUp
````

2. **Instale as dependências:**

```bash
pip install pyautogui pandas
```

3. **Tenha o navegador Opera instalado e posicionado como o navegador padrão.**

4. **Coloque o arquivo `produtos.csv` no mesmo diretório do script.**

5. **Execute o script Python:**

```bash
python codigo.py
```

⚠️ **Importante:**

* Não mexa no mouse ou teclado durante a execução do script.
* Verifique as posições do clique (`pyautogui.click(x, y)`) e ajuste para a resolução da sua tela, se necessário.

## 📌 O que aprendi com este projeto

* Como automatizar tarefas repetitivas com **PyAutoGUI**.
* Manipulação de dados com **Pandas**.
* Simulação de teclas e mouse.
* A importância da precisão em automações com interface gráfica.

## 👨‍💻 Projeto criado por Isaac durante o Intensivão de Python da [Hashtag Programação](https://www.hashtagtreinamentos.com/).


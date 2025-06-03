# 🧩 Projeto Flask Colaborativo - Cards da Equipe

Este é um projeto colaborativo baseado em **Flask**, onde cada integrante da equipe terá um **card personalizado** na página principal. Ao clicar em um card, o usuário será redirecionado para uma rota específica desenvolvida por esse integrante.

> 💡 Este repositório será gerenciado por um responsável (líder) que aprovará as contribuições via *pull requests*. Os demais integrantes devem seguir os passos abaixo para colaborar corretamente.

---

## ✅ Pré-requisitos

Antes de começar, você precisa ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- Uma conta no [GitHub](https://github.com/)

---

## 📦 1. Fork do repositório

1. Acesse o repositório original no GitHub (link fornecido pelo líder).
2. Clique em **"Fork"** (canto superior direito da página).
3. Isso criará uma cópia do repositório no seu próprio GitHub.

---

## 💻 2. Clonar o seu fork para sua máquina

Abra o terminal e execute:

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

---

## 🧰 3. Instalar as dependências com o `requirements.txt`

Após clonar o projeto, crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate.bat  # Windows
```

Instale as dependências com:

```bash
pip install -r requirements.txt
```

> 📄 O arquivo `requirements.txt` contém todas as bibliotecas necessárias para rodar o projeto Flask corretamente.

---

## 🔁 4. Configurar o repositório original como "upstream"

Para manter seu fork sincronizado com o repositório original:

```bash
git remote add upstream https://github.com/lucianolpsf/flask_colaborativo.git
```

---

## 🌱 5. Criar uma branch para sua contribuição

Crie uma nova branch com um nome identificador (ex: `card-ana-silva`):

```bash
git checkout -b card-seu-nome
```

---

## ✍️ 6. Adicionar sua rota e card

Você deve:

- Criar um **arquivo Python com uma rota Flask personalizada** (ex: `@app.route('/ana')`).
- Adicionar um **card na página principal (`templates/home.html`)** com um link para sua rota.

> 🧪 Teste o funcionamento local executando o app com `flask run` ou `python app.py`.

---

## ✅ 7. Commit e Push

Após finalizar sua parte, envie as alterações para o seu fork:

```bash
git add .
git commit -m "Adiciona card e rota para Ana Silva"
git push origin card-seu-nome
```

---

## 📬 8. Criar um Pull Request

1. Vá até seu fork no GitHub.
2. Clique em **"Compare & pull request"**.
3. Escreva um título e descrição claros.
4. Envie para revisão. O líder do projeto irá analisar e aceitar (ou pedir ajustes).

---

## 🔄 9. Manter seu fork atualizado

Periodicamente, sincronize seu repositório com o original:

```bash
git checkout main
git pull upstream main
git push origin main
```

---

## 📏 Regras para contribuir

- ✅ Cada pessoa **cria apenas um card e uma rota**.
- ⚠️ Não edite ou apague arquivos de outros colegas.
- 🧼 Mantenha o código limpo e funcional.
- 🚫 Nunca edite diretamente a branch `main`.
- 💬 Utilize Pull Requests para colaborar.

---

## 👨‍💻 Gerente do Projeto

- Todas as contribuições serão analisadas por **[@lucianolpsf](https://github.com/lucianolpsf)**.
- Em caso de dúvidas, entre em contato ou abra uma Issue.

---

## 📎 Exemplo de estrutura esperada

```text
/
├── app.py                # Arquivo principal do Flask
├── requirements.txt      # Lista de dependências
├── templates/
│   └── home.html         # Página principal com todos os cards
├── rotas/
│   ├── __init__.py       # Registro automático das rotas
│   └── ana.py            # Arquivo com rota personalizada da Ana
```

---

## ✨ Obrigado por colaborar!

Juntos construiremos uma aplicação web simples e organizada, aprendendo a usar Git/GitHub em equipe! 🚀

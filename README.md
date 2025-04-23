# 🎲 Sistema de Geração de Cartelas de Bingo - V1

Este é um sistema em **Python** para gerar cartelas de bingo em formato PDF, com layout organizado para impressão em folhas A4 (4 cartelas por página).




> ⚠️ **Aviso Legal**: Este projeto é de caráter exclusivamente educacional, sem fins lucrativos e **não** tem o objetivo de incentivar a prática de jogos de azar.

---

## ✨ Funcionalidades

- Geração automática de cartelas únicas, com numeração identificadora.
- Impressão em folhas A4 com 4 cartelas por página.
- Layout personalizável, com título no topo da página.
- Centralização e espaçamento inteligente entre cartelas.
- Suporte a configuração da quantidade de cartelas no arquivo.

---

## 🧰 Requisitos

- Python 3.6+
- Biblioteca `reportlab`

---

## 💾 Instalação

> No macOS, você pode instalar as dependências com o comando:

```bash
python3 -m pip install reportlab
Caso não tenha o pip instalado, você pode instalar com:


sudo easy_install pip

🚀 Como Usar

Clone o repositório:


git clone https://github.com/seu-usuario/sistema-cartelas-bingo.git
cd sistema-cartelas-bingo

Execute o script principal para gerar as cartelas:


python3 main.py
Será gerado um arquivo cartelas_bingo.pdf no mesmo diretório, pronto para ser impresso.

🛠 Personalizações
Você pode alterar os seguintes parâmetros dentro do script main.py:


gerar_pdf_com_cartelas("cartelas_bingo.pdf", total_cartelas=20, titulo="BINGO ESCOLAR 2025")

total_cartelas: define quantas cartelas serão geradas.

titulo: define o título que aparece no topo da página.

🚧 Aviso sobre a Versão
Esta é a versão 1 (V1) do projeto e pode conter bugs ou limitações. Contribuições, sugestões e correções são muito bem-vindas!

📄 Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

📬 Para dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request!

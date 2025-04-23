import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def gerar_cartela_bingo():
    cartela = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    cartela['N'][2] = 'LARI'
    return cartela

def desenhar_cartela(c, cartela, x, y, numero_cartela, tamanho=28):
    largura_celula = tamanho
    altura_celula = tamanho
    colunas = ['B', 'I', 'N', 'G', 'O']

    # Cabeçalho da cartela (letras BINGO)
    c.setFont("Helvetica-Bold", 12)
    for i, letra in enumerate(colunas):
        c.rect(x + i * largura_celula, y + 5 * altura_celula, largura_celula, altura_celula)
        c.drawCentredString(x + i * largura_celula + largura_celula / 2, y + 5 * altura_celula + 8, letra)

    # Números
    c.setFont("Helvetica", 10)
    for linha in range(5):
        for coluna in range(5):
            valor = cartela[colunas[coluna]][linha]
            texto = str(valor)
            c.rect(x + coluna * largura_celula, y + (4 - linha) * altura_celula, largura_celula, altura_celula)
            c.drawCentredString(
                x + coluna * largura_celula + largura_celula / 2,
                y + (4 - linha) * altura_celula + 8,
                texto
            )

    # Número da cartela (abaixo da cartela)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(x + (largura_celula * 5) / 2, y - 10, f"Cartela nº {numero_cartela}")

def gerar_pdf_com_cartelas(nome_arquivo, total_cartelas=100, titulo="BINGO DA LARI 2025"):
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura_pagina, altura_pagina = A4

    cartelas_por_pagina = 4
    margem_lateral = 15 * mm
    margem_superior = 20 * mm
    espacamento_horizontal = 10 * mm

    
    espacamento_vertical_linha_1 = 20 * mm
    espacamento_vertical_linha_2 = 40 * mm  

    # Tamanho das células
    cartela_largura_total = (largura_pagina - (2 * margem_lateral) - espacamento_horizontal) / 2
    celula_tamanho = cartela_largura_total / 5

    for i in range(total_cartelas):
        cartela = gerar_cartela_bingo()
        posicao_na_pagina = i % cartelas_por_pagina

        coluna = posicao_na_pagina % 2
        linha = posicao_na_pagina // 2

        x_offset = margem_lateral + coluna * (cartela_largura_total + espacamento_horizontal)

        if linha == 0:
            y_offset = altura_pagina - margem_superior - (celula_tamanho * 5 + espacamento_vertical_linha_1)
        else:
            y_offset = altura_pagina - margem_superior - (celula_tamanho * 5 + espacamento_vertical_linha_1) \
                       - (celula_tamanho * 5 + espacamento_vertical_linha_2)

        desenhar_cartela(c, cartela, x_offset, y_offset, numero_cartela=i + 1, tamanho=celula_tamanho)

        # Título da página
        if posicao_na_pagina == 0:
            c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(largura_pagina / 2, altura_pagina - 10 * mm, titulo)

        if (i + 1) % cartelas_por_pagina == 0 or i == total_cartelas - 1:
            c.showPage()

    c.save()
    print(f"PDF gerado com sucesso: {nome_arquivo}")

# Gerar cartelas espacadas em um único PDF
gerar_pdf_com_cartelas("cartelas_bingo_espacadas.pdf", total_cartelas=100, titulo="BINGO DA LARI 2025")

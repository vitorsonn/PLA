import streamlit as st
import numpy as np

st.set_page_config(page_title="Trabalho de Matrizes", layout="wide")

st.title("📘 Trabalho de Matrizes em Python")
st.subheader("Álgebra Linear — Operações com Matrizes, Determinantes e Método de Gauss")

st.divider()

# =====================================
# SOMA DE MATRIZES
# =====================================

st.header("1) Soma de Matrizes")

st.write("As matrizes precisam possuir a mesma ordem.")

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

resultado = A + B

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Matriz A")
    st.write(A)

with col2:
    st.subheader("Matriz B")
    st.write(B)

with col3:
    st.subheader("Resultado")
    st.write(resultado)

st.code('''
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

resultado = A + B

print(resultado)
''', language='python')

st.divider()

# =====================================
# SUBTRAÇÃO
# =====================================

st.header("2) Subtração de Matrizes")

A = np.array([
    [8, 7],
    [6, 5]
])

B = np.array([
    [1, 2],
    [3, 4]
])

resultado = A - B

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Matriz A")
    st.write(A)

with col2:
    st.subheader("Matriz B")
    st.write(B)

with col3:
    st.subheader("Resultado")
    st.write(resultado)

st.code('''
import numpy as np

A = np.array([
    [8, 7],
    [6, 5]
])

B = np.array([
    [1, 2],
    [3, 4]
])

resultado = A - B

print(resultado)
''', language='python')

st.divider()

# =====================================
# ESCALAR
# =====================================

st.header("3) Multiplicação por Escalar")

A = np.array([
    [1, 2],
    [3, 4]
])

escalar = 3
resultado = A * escalar

col1, col2 = st.columns(2)

with col1:
    st.subheader("Matriz Original")
    st.write(A)

with col2:
    st.subheader("Resultado")
    st.write(resultado)

st.code('''
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

escalar = 3

resultado = A * escalar

print(resultado)
''', language='python')

st.divider()

# =====================================
# PRODUTO MATRIZES
# =====================================

st.header("4) Produto de Matrizes")

st.write("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

resultado = np.dot(A, B)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(A)

with col2:
    st.write(B)

with col3:
    st.write(resultado)

st.code('''
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

resultado = np.dot(A, B)

print(resultado)
''', language='python')

st.divider()

# =====================================
# DETERMINANTES
# =====================================

st.header("5) Determinantes")

st.subheader("Determinante 2x2")
st.latex(r"det(A)=ad-bc")

A = np.array([
    [2, 3],
    [1, 4]
])

resultado = np.linalg.det(A)

st.write("Matriz:")
st.write(A)

st.write("Determinante:")
st.success(resultado)


st.code('''
import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

resultado = np.linalg.det(A)

print(resultado)
''', language='python')

st.subheader("Determinante 3x3")

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

resultado = np.linalg.det(A)

st.write(A)
st.success(resultado)

st.code('''
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

resultado = np.linalg.det(A)

print(resultado)
''', language='python')



st.divider()

# =====================================
# GAUSS
# =====================================

st.header("6) Método de Gauss")

st.write("O método de Gauss transforma a matriz em forma escalonada.")

aba1, aba2, aba3 = st.tabs(["SPD", "SPI", "SI"])

# SPD
with aba1:
    st.subheader("Sistema Possível e Determinado")

    matriz = np.array([
        [2, 1, 5],
        [4, -6, -2]
    ], dtype=float)

    st.write("Matriz:")
    st.write(matriz)

    st.code('''
    import numpy as np

    matriz = np.array([
        [2, 1, 5],
        [4, -6, -2]
    ], dtype=float)

    print(matriz)
    ''', language='python')    

# SPI
with aba2:
    st.subheader("Sistema Possível e Indeterminado")

    matriz = np.array([
        [1, 1, 2],
        [2, 2, 4]
    ], dtype=float)

    st.write("Matriz:")
    st.write(matriz)

    st.code('''
    import numpy as np

    matriz = np.array([
        [1, 1, 2],
        [2, 2, 4]
    ], dtype=float)

    print(matriz)
    ''', language='python')    



# SI
with aba3:
    st.subheader("Sistema Impossível")

    matriz = np.array([
        [1, 1, 2],
        [1, 1, 3]
    ], dtype=float)

    st.write("Matriz:")
    st.write(matriz)

    st.code('''
    import numpy as np

    matriz = np.array([
        [1, 1, 2],
        [1, 1, 3]
    ], dtype=float)

    print(matriz)
    ''', language='python')    

st.divider()

# =====================================
# CONCLUSÃO
# =====================================

st.header("✅ Conclusão")

st.write(
    "Neste trabalho foram apresentados conceitos de Álgebra Linear utilizando Python, "
    "incluindo operações com matrizes, determinantes e resolução de sistemas lineares."
)

st.info("Projeto desenvolvido para apresentação acadêmica.")

# =====================================
# RODAR O PROJETO
# =====================================

st.sidebar.title("▶ Como Rodar")

st.sidebar.code('''
pip install streamlit numpy

stre    amlit run app.py
''')

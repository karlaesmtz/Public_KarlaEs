import streamlit as st

# Título de la aplicación
st.title("Calculadora de Cuadrados")

# Ingreso de un número por parte del usuario
numero = st.number_input("Ingresa un número:", value=0)

# Cálculo del cuadrado
cuadrado = numero ** 2

# Mostrar el resultado
st.write(f"El cuadrado de {numero} es: {cuadrado}")

# Sección adicional para mostrar un gráfico
st.subheader("Gráfico del Cuadrado")
st.line_chart([numero, cuadrado])

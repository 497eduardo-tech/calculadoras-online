import datetime
import random
import string
import streamlit as st

st.set_page_config(
    page_title="Central de Calculadoras Online",
    page_icon="🧮",
    layout="wide",
)

st.title("🧮 Central de Calculadoras Online")
st.write(
    "As ferramentas de cálculo mais buscadas da internet, reunidas em um só"
    " lugar."
)

# Menu lateral com as categorias principais
categoria = st.sidebar.selectbox(
    "Escolha a Categoria",
    [
        "Financeiras",
        "💪 Saúde e Bem-Estar",
        "📐 Matemática e Pessoal",
        "⚡ Utilidades e Dia a Dia",
    ],
)

# --- 1. CATEGORIA: FINANCEIRAS ---
if categoria == "Financeiras":
  st.header("Calculadoras Financeiras")

  aba_fin = st.tabs([
      "Juros Compostos",
      "Conversor de Moedas",
      "Salário Líquido (CLT)",
      "Desconto / Porcentagem",
      "Financiamento / Empréstimo",
      "ROI e Margem de Lucro",
  ])

  with aba_fin[0]:
    st.subheader("Calculadora de Juros Compostos")
    cap = st.number_input("Capital Inicial (R$)", value=1000.0, key="j_cap")
    aporte = st.number_input(
        "Aportes Mensais (R$)", value=200.0, key="j_aporte"
    )
    tax = st.number_input("Taxa de Juros Mensal (%)", value=1.0, key="j_tax")
    meses = st.number_input("Tempo (meses)", value=12, key="j_meses")
    if st.button("Calcular Juros Compostos", key="b_juros"):
      montante = cap
      for _ in range(int(meses)):
        montante = (montante + aporte) * (1 + (tax / 100))
      st.success(f"Montante Final Acumulado: R$ {montante:.2f}")

  with aba_fin[1]:
    st.subheader("Conversor de Moedas (Simulador)")
    valor_brl = st.number_input("Valor em Reais (R$)", value=100.0, key="m_brl")
    cotacao_usd = st.number_input(
        "Cotação do Dólar (R$)", value=5.0, key="m_usd"
    )
    if st.button("Converter para Dólar", key="b_moeda"):
      st.success(f"Valor equivalente: US$ {valor_brl / cotacao_usd:.2f}")

  with aba_fin[2]:
    st.subheader("Estimativa de Salário Líquido")
    bruto = st.number_input("Salário Bruto (R$)", value=3500.0, key="s_bruto")
    if st.button("Calcular Líquido", key="b_sal"):
      desconto = bruto * 0.11 if bruto <= 4000 else bruto * 0.20
      liquido = bruto - desconto
      st.success(f"Salário Líquido Estimado: R$ {liquido:.2f}")

  with aba_fin[3]:
    st.subheader("Cálculo de Desconto Comercial")
    preco = st.number_input("Preço Original (R$)", value=150.0, key="d_preco")
    desc = st.number_input("Desconto (%)", value=15.0, key="d_desc")
    if st.button("Calcular Desconto", key="b_desc"):
      final = preco * (1 - desc / 100)
      economia = preco - final
      st.success(
          f"Preço Final: R$ {final:.2f} (Você economiza R$ {economia:.2f})"
      )

  with aba_fin[4]:
    st.subheader("Simulação Básica de Empréstimo")
    val_emp = st.number_input("Valor do Empréstimo (R$)", value=10000.0, key="e_v")
    juros_emp = st.number_input("Taxa de Juros Mensal (%)", value=2.0, key="e_j")
    meses_emp = st.number_input("Parcelas (meses)", value=12, key="e_m")
    if st.button("Calcular Parcelas", key="b_emp"):
      i = juros_emp / 100
      pmt = val_emp * (i * (1 + i) ** meses_emp) / (((1 + i) ** meses_emp) - 1)
      st.success(
          f"Valor da Parcela Mensal: R$ {pmt:.2f} | Total pago:"
          f" R$ {pmt * meses_emp:.2f}"
      )

  with aba_fin[5]:
    st.subheader("ROI e Margem de Lucro")
    custo = st.number_input("Custo de Produção (R$)", value=40.0, key="l_c")
    venda = st.number_input("Preço de Venda (R$)", value=100.0, key="l_v")
    if st.button("Calcular Lucratividade", key="b_lucro"):
      lucro = venda - custo
      margem = (lucro / venda) * 100
      st.success(f"Lucro Unitário: R$ {lucro:.2f} | Margem: {margem:.2f}%")

# --- 2. CATEGORIA: SAÚDE E BEM-ESTAR ---
elif categoria == "💪 Saúde e Bem-Estar":
  st.header("Calculadoras de Saúde (As mais procuradas)")

  aba_saude = st.tabs([
      "IMC (Massa Corporal)",
      "Gasto Calórico (TMB)",
      "Consumo de Água",
      "Frequência Cardíaca",
      "Peso Ideal",
  ])

  with aba_saude[0]:
    st.subheader("Índice de Massa Corporal (IMC)")
    peso = st.number_input("Peso (kg)", value=70.0, key="imc_p")
    altura = st.number_input("Altura (m)", value=1.75, key="imc_a")
    if st.button("Calcular IMC", key="b_imc"):
      imc = peso / (altura**2)
      classificacao = (
          "Abaixo do peso"
          if imc < 18.5
          else "Peso normal"
          if imc < 25
          else "Sobrepeso"
          if imc < 30
          else "Obesidade"
      )
      st.success(f"Seu IMC é {imc:.2f} ({classificacao})")

  with aba_saude[1]:
    st.subheader("Gasto Calórico Basal (TMB)")
    p = st.number_input("Peso (kg)", value=70.0, key="tmb_p")
    a = st.number_input("Altura (cm)", value=175.0, key="tmb_a")
    i = st.number_input("Idade (anos)", value=30, key="tmb_i")
    sexo = st.selectbox("Sexo Biológico", ["Masculino", "Feminino"], key="tmb_s")
    if st.button("Calcular TMB", key="b_tmb"):
      if sexo == "Masculino":
        tmb = 88.36 + (13.4 * p) + (4.8 * a) - (5.7 * i)
      else:
        tmb = 447.6 + (9.2 * p) + (3.1 * a) - (4.3 * i)
      st.success(f"Gasto Calórico Basal: {tmb:.1f} kcal/dia")

  with aba_saude[2]:
    st.subheader("Água Diária Recomendada")
    peso_agua = st.number_input("Seu peso (kg)", value=70.0, key="agua_p")
    if st.button("Calcular Água", key="b_agua"):
      total_ml = peso_agua * 35
      st.success(
          "Você deve consumir aproximadamente"
          f" **{(total_ml / 1000):.2f} litros** de água por dia."
      )

  with aba_saude[3]:
    st.subheader("Frequência Cardíaca Máxima")
    idade_fc = st.number_input("Sua idade", value=30, key="fc_i")
    if st.button("Calcular Frequência", key="b_fc"):
      fc_max = 220 - idade_fc
      st.success(
          f"Frequência Cardíaca Máxima: {fc_max} bpm (Ideal para treinos: "
          f"{int(fc_max * 0.6)} a {int(fc_max * 0.85)} bpm)"
      )

  with aba_saude[4]:
    st.subheader("Peso Ideal Estimado")
    alt_pi = st.number_input("Altura (m)", value=1.75, key="pi_a")
    sexo_pi = st.selectbox("Sexo", ["Masculino", "Feminino"], key="pi_s")
    if st.button("Calcular Peso Ideal", key="b_pi"):
      pi = (72.7 * alt_pi) - 58 if sexo_pi == "Masculino" else (62.1 * alt_pi) - 44.7
      st.success(f"Peso ideal estimado: {pi:.2f} kg")

# --- 3. CATEGORIA: MATEMÁTICA E PESSOAL ---
elif categoria == "📐 Matemática e Pessoal":
  st.header("Matemática Prática")

  aba_mat = st.tabs([
      "Regra de Três",
      "Porcentagem Básica",
      "Média Aritmética",
      "Equação 2º Grau (Bhaskara)",
      "Teorema de Pitágoras",
  ])

  with aba_mat[0]:
    st.subheader("Regra de Três Simples")
    col_a1 = st.number_input("A1", value=10.0, key="r3_1")
    col_b1 = st.number_input("B1", value=20.0, key="r3_2")
    col_a2 = st.number_input("A2", value=30.0, key="r3_3")
    if st.button("Calcular X", key="b_r3"):
      x = (col_b1 * col_a2) / col_a1
      st.success(f"O valor de X é: {x}")

  with aba_mat[1]:
    st.subheader("Cálculo de Porcentagem")
    val_p = st.number_input("Quanto é", value=25.0, key="p_v")
    tot_p = st.number_input("de (%)", value=200.0, key="p_t")
    if st.button("Calcular Porcentagem", key="b_p"):
      st.success(f"Resultado: {(val_p / 100) * tot_p}")

  with aba_mat[2]:
    st.subheader("Média Simples")
    numeros_str = st.text_input(
        "Insira os números separados por vírgula", "7.5, 8.0, 9.2", key="med_s"
    )
    if st.button("Calcular Média", key="b_med"):
      try:
        nums = [float(n.strip()) for n in numeros_str.split(",")]
        st.success(f"Média Aritmética: {sum(nums) / len(nums):.2f}")
      except:
        st.error("Digite apenas números separados por vírgula.")

  with aba_mat[3]:
    st.subheader("Fórmula de Bhaskara")
    a_b = st.number_input("Valor de a", value=1.0, key="bh_a")
    b_b = st.number_input("Valor de b", value=-5.0, key="bh_b")
    c_b = st.number_input("Valor de c", value=6.0, key="bh_c")
    if st.button("Calcular Raízes", key="b_bh"):
      delta = (b_b**2) - (4 * a_b * c_b)
      if delta < 0:
        st.error("Delta negativo: não existem raízes reais.")
      else:
        r1 = (-b_b + (delta**0.5)) / (2 * a_b)
        r2 = (-b_b - (delta**0.5)) / (2 * a_b)
        st.success(f"Raízes: x1 = {r1:.2f} | x2 = {r2:.2f}")

  with aba_mat[4]:
    st.subheader("Teorema de Pitágoras")
    cat1 = st.number_input("Cateto A", value=3.0, key="pit_1")
    cat2 = st.number_input("Cateto B", value=4.0, key="pit_2")
    if st.button("Calcular Hipotenusa", key="b_pit"):
      hip = ((cat1**2) + (cat2**2)) ** 0.5
      st.success(f"Hipotenusa (c): {hip:.2f}")

# --- 4. CATEGORIA: UTILIDADES E DIA A DIA ---
elif categoria == "⚡ Utilidades e Dia a Dia":
  st.header("Conversores e Utilidades Populares")

  aba_util = st.tabs([
      "Dias entre Datas",
      "Temperatura",
      "Gorjeta (Garçom)",
      "Gasto de Combustível",
      "Gerador de Senhas",
      "Distância e Peso",
  ])

  with aba_util[0]:
    st.subheader("Diferença de Dias entre Datas")
    d1 = st.date_input("Data inicial", datetime.date(2026, 1, 1), key="d_ini")
    d2 = st.date_input("Data final", datetime.date(2026, 12, 31), key="d_fim")
    if st.button("Calcular Dias", key="b_dias"):
      diff = (d2 - d1).days
      st.success(f"Total de dias entre as datas: {abs(diff)} dias")

  with aba_util[1]:
    st.subheader("Conversor de Temperatura")
    c_temp = st.number_input("Temperatura em Celsius (°C)", value=25.0, key="t_c")
    if st.button("Converter para Fahrenheit", key="b_temp"):
      f_temp = (c_temp * 9 / 5) + 32
      st.success(f"Temperatura em Fahrenheit: {f_temp:.1f} °F")

  with aba_util[2]:
    st.subheader("Calculadora de Gorjeta")
    conta = st.number_input("Valor da Conta (R$)", value=120.0, key="g_conta")
    porc = st.slider("Porcentagem de Gorjeta (%)", 0, 30, 10, key="g_porc")
    if st.button("Calcular Total", key="b_gorg"):
      gorjeta = conta * (porc / 100)
      st.success(
          f"Gorjeta: R$ {gorjeta:.2f} | Total com gorjeta: R$"
          f" {conta + gorjeta:.2f}"
      )

  with aba_util[3]:
    st.subheader("Custo de Combustível por Viagem")
    distancia_v = st.number_input(
        "Distância da viagem (km)", value=250.0, key="cb_d"
    )
    consumo_carro = st.number_input(
        "Consumo médio do carro (km/l)", value=12.0, key="cb_c"
    )
    preco_comb = st.number_input(
        "Preço do litro do combustível (R$)", value=5.89, key="cb_p"
    )
    if st.button("Calcular Custo", key="b_cb"):
      litros = distancia_v / consumo_carro
      custo_total = litros * preco_comb
      st.success(
          f"Você vai gastar ~{litros:.1f} litros, totalizando R$"
          f" {custo_total:.2f}"
      )

  with aba_util[4]:
    st.subheader("Gerador de Senhas Seguras")
    tamanho = st.slider("Tamanho da senha", 6, 32, 12, key="s_tam")
    if st.button("Gerar Senha", key="b_senha"):
      chars = string.ascii_letters + string.digits + string.punctuation
      senha = "".join(random.choice(chars) for _ in range(tamanho))
      st.code(senha)

  with aba_util[5]:
    st.subheader("Conversores Rápidos")
    tipo_conv = st.selectbox(
        "Selecione a conversão",
        ["Quilômetros para Milhas", "Quilogramas para Libras"],
    )
    val_conv = st.number_input("Valor a converter", value=10.0, key="vc_v")
    if st.button("Converter Unidade", key="b_conv"):
      if tipo_conv == "Quilômetros para Milhas":
        st.success(f"{val_conv} km = {val_conv * 0.621371:.2f} milhas")
      else:
        st.success(f"{val_conv} kg = {val_conv * 2.20462:.2f} libras")
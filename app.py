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
        "Saúde e Bem-Estar",
        "Matemática e Pessoal",
        "Utilidades e Dia a Dia",
    ],
)

# --- 1. CATEGORIA: FINANCEIRAS ---
if categoria == "Financeiras":
  st.header("Calculadoras Financeiras")

  aba_fin = st.tabs([
      "Juros Compostos",
      "Conversor de Moedas",
      "Salário Líquido (CLT)",
      "Imposto de Renda (IRPF)",
      "Desconto / Porcentagem",
      "Empréstimo (Tabela Price)",
      "Financiamento Imobiliário",
      "Cálculo de Férias / Rescisão",
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
    st.subheader("Simulador Rápido de Imposto de Renda (IRPF)")
    sal_irpf = st.number_input(
        "Rendimento Tributável Mensal (R$)", value=4500.0, key="ir_sal"
    )
    if st.button("Calcular IRPF", key="b_irpf"):
      # Tabela progressiva simplificada de referência
      if sal_irpf <= 2259.20:
        imposto = 0.0
        aliquota = "Isento"
      elif sal_irpf <= 2826.65:
        imposto = (sal_irpf * 0.075) - 169.44
        aliquota = "7.5%"
      elif sal_irpf <= 3751.05:
        imposto = (sal_irpf * 0.15) - 381.44
        aliquota = "15%"
      elif sal_irpf <= 4664.68:
        imposto = (sal_irpf * 0.225) - 662.77
        aliquota = "22.5%"
      else:
        imposto = (sal_irpf * 0.275) - 896.00
        aliquota = "27.5%"

      imposto = max(0.0, imposto)
      st.success(
          f"Alíquota efetiva: {aliquota} | Imposto Retido Estimado: R$"
          f" {imposto:.2f}"
      )

  with aba_fin[4]:
    st.subheader("Cálculo de Desconto Comercial")
    preco = st.number_input("Preço Original (R$)", value=150.0, key="d_preco")
    desc = st.number_input("Desconto (%)", value=15.0, key="d_desc")
    if st.button("Calcular Desconto", key="b_desc"):
      final = preco * (1 - desc / 100)
      economia = preco - final
      st.success(
          f"Preço Final: R$ {final:.2f} (Você economiza R$ {economia:.2f})"
      )

  with aba_fin[5]:
    st.subheader("Simulação de Empréstimo (Tabela Price)")
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

  with aba_fin[6]:
    st.subheader("Simulador de Financiamento Imobiliário")
    imovel = st.number_input("Valor do Imóvel (R$)", value=300000.0, key="fin_im")
    entrada = st.number_input(
        "Valor da Entrada (R$)", value=60000.0, key="fin_ent"
    )
    anos = st.number_input("Prazo (anos)", value=30, key="fin_ano")
    taxa_anual = st.number_input(
        "Taxa de Juros Anual (%)", value=10.0, key="fin_tx"
    )
    if st.button("Calcular Financiamento", key="b_fin"):
      valor_fin = imovel - entrada
      meses_f = anos * 12
      i_m = (taxa_anual / 100) / 12
      pmt_im = (
          valor_fin * (i_m * (1 + i_m) ** meses_f) / (((1 + i_m) ** meses_f) - 1)
      )
      st.success(
          f"Valor financiado: R$ {valor_fin:.2f} | 1ª Parcela estimada:"
          f" R$ {pmt_im:.2f}"
      )

  with aba_fin[7]:
    st.subheader("Cálculo Estimado de Férias")
    sal_ferias = st.number_input(
        "Salário Bruto Mensal (R$)", value=3000.0, key="f_sal"
    )
    dias_ferias = st.number_input(
        "Dias de Férias a gozar", value=30, key="f_dias"
    )
    if st.button("Calcular Férias", key="b_ferias"):
      proporcao = dias_ferias / 30
      terco = (sal_ferias * proporcao) / 3
      total_ferias = (sal_ferias * proporcao) + terco
      st.success(
          f"Valor Bruto das Férias (com 1/3 constitucional): R$"
          f" {total_ferias:.2f}"
      )

  with aba_fin[8]:
    st.subheader("ROI e Margem de Lucro")
    custo = st.number_input("Custo de Produção (R$)", value=40.0, key="l_c")
    venda = st.number_input("Preço de Venda (R$)", value=100.0, key="l_v")
    if st.button("Calcular Lucratividade", key="b_lucro"):
      lucro = venda - custo
      margem = (lucro / venda) * 100
      st.success(f"Lucro Unitário: R$ {lucro:.2f} | Margem: {margem:.2f}%")

# --- 2. CATEGORIA: SAÚDE E BEM-ESTAR ---
elif categoria == "Saúde e Bem-Estar":
  st.header("Calculadoras de Saúde (As mais procuradas)")

  aba_saude = st.tabs([
      "IMC (Massa Corporal)",
      "Gasto Calórico Avançado",
      "Consumo de Água",
      "Frequência Cardíaca",
      "Percentual de Gordura",
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
    st.subheader("Gasto Calórico Total (com Nível de Atividade)")
    p = st.number_input("Peso (kg)", value=70.0, key="tmb_p")
    a = st.number_input("Altura (cm)", value=175.0, key="tmb_a")
    i = st.number_input("Idade (anos)", value=30, key="tmb_i")
    sexo = st.selectbox("Sexo Biológico", ["Masculino", "Feminino"], key="tmb_s")
    atividade = st.selectbox(
        "Nível de Atividade",
        [
            "Sedentário (pouco ou nenhum exercício)",
            "Levemente ativo (exercício leve 1-3 dias/sem)",
            "Moderadamente ativo (exercício moderado 3-5 dias/sem)",
            "Altamente ativo (exercício pesado 6-7 dias/sem)",
        ],
        key="tmb_ativ",
    )
    if st.button("Calcular Gasto Total", key="b_tmb"):
      if sexo == "Masculino":
        tmb = 88.36 + (13.4 * p) + (4.8 * a) - (5.7 * i)
      else:
        tmb = 447.6 + (9.2 * p) + (3.1 * a) - (4.3 * i)

      fator = 1.2
      if "Levemente" in atividade:
        fator = 1.375
      elif "Moderadamente" in atividade:
        fator = 1.55
      elif "Altamente" in atividade:
        fator = 1.725

      gasto_total = tmb * fator
      st.success(
          f"Gasto Basal: {tmb:.1f} kcal | Gasto Total Diário:"
          f" **{gasto_total:.1f} kcal**"
      )

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
    st.subheader("Percentual de Gordura Corporal (Estimativa IMC)")
    peso_g = st.number_input("Peso (kg)", value=70.0, key="g_p")
    altura_g = st.number_input("Altura (m)", value=1.75, key="g_a")
    idade_g = st.number_input("Idade", value=30, key="g_id")
    sexo_g = st.selectbox("Sexo", ["Masculino", "Feminino"], key="g_sex")
    if st.button("Calcular Gordura", key="b_gordura"):
      imc_g = peso_g / (altura_g**2)
      f_sexo = 1 if sexo_g == "Masculino" else 0
      pGC = (1.20 * imc_g) + (0.23 * idade_g) - (10.8 * f_sexo) - 5.4
      st.success(f"Percentual de Gordura Estimado: {pGC:.1f}%")

  with aba_saude[5]:
    st.subheader("Peso Ideal Estimado")
    alt_pi = st.number_input("Altura (m)", value=1.75, key="pi_a")
    sexo_pi = st.selectbox("Sexo", ["Masculino", "Feminino"], key="pi_s")
    if st.button("Calcular Peso Ideal", key="b_pi"):
      pi = (72.7 * alt_pi) - 58 if sexo_pi == "Masculino" else (62.1 * alt_pi) - 44.7
      st.success(f"Peso ideal estimado: {pi:.2f} kg")

# --- 3. CATEGORIA: MATEMÁTICA E PESSOAL ---
elif categoria == "Matemática e Pessoal":
  st.header("Matemática Prática")

  aba_mat = st.tabs([
      "Regra de Três",
      "Porcentagem Básica",
      "Média Aritmética",
      "Equação 2º Grau (Bhaskara)",
      "Teorema de Pitágoras",
      "Área de Círculo",
      "Bases Numéricas",
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

  with aba_mat[5]:
    st.subheader("Área e Perímetro de Círculo")
    raio_c = st.number_input("Raio do círculo", value=5.0, key="rc_r")
    if st.button("Calcular Círculo", key="b_circ"):
      import math

      area = math.pi * (raio_c**2)
      perimetro = 2 * math.pi * raio_c
      st.success(f"Área: {area:.2f} | Perímetro (Circunferência): {perimetro:.2f}")

  with aba_mat[6]:
    st.subheader("Conversor de Bases Numéricas (Decimal)")
    dec_val = st.number_input("Número Decimal", value=42, key="bn_dec")
    if st.button("Converter Base", key="b_base"):
      st.success(
          f"Binário: {bin(int(dec_val))} | Hexadecimal:"
          f" {hex(int(dec_val)).upper()}"
      )

# --- 4. CATEGORIA: UTILIDADES E DIA A DIA ---
elif categoria == "Utilidades e Dia a Dia":
  st.header("Conversores e Utilidades Populares")

  aba_util = st.tabs([
      "Calculadora de Churrasco",
      "Medidas Culinárias",
      "Dias entre Datas",
      "Temperatura",
      "Gorjeta (Garçom)",
      "Gasto de Combustível",
      "Velocidade Média",
      "Armazenamento (MB / GB)",
      "Gerador de Senhas",
      "Distância e Peso",
  ])

  with aba_util[0]:
    st.subheader("Calculadora de Churrasco por Pessoas")
    adultos = st.number_input("Número de Adultos", value=10, key="ch_ad")
    criancas = st.number_input("Número de Crianças", value=4, key="ch_cr")
    if st.button("Calcular Suprimentos", key="b_churras"):
      carne = (adultos * 400 + criancas * 200) / 1000
      cerveja = adultos * 3  # latas de 350ml média
      refrigerante = (adultos + criancas) * 0.5  # litros
      st.success(
          f"🥩 Carne necessária: {carne:.1f} kg | 🍺 Cerveja:"
          f" {cerveja} latas | 🥤 Refrigerante: {refrigerante:.1f} litros"
      )

  with aba_util[1]:
    st.subheader("Conversor de Medidas Culinárias (Aproximado)")
    ingrediente = st.selectbox(
        "Ingrediente / Base", ["Água / Leite (ml)", "Açúcar (g)", "Farinha (g)"]
    )
    xicaras = st.number_input("Quantidade em Xícaras", value=1.0, key="cul_x")
    if st.button("Converter para Gramas/ml", key="b_cul"):
      if "Água" in ingrediente:
        res = xicaras * 240
        st.success(f"{xicaras} xícara(s) = {res:.0f} ml")
      elif "Açúcar" in ingrediente:
        res = xicaras * 180
        st.success(f"{xicaras} xícara(s) = {res:.0f} g")
      else:
        res = xicaras * 120
        st.success(f"{xicaras} xícara(s) = {res:.0f} g")

  with aba_util[2]:
    st.subheader("Diferença de Dias entre Datas")
    d1 = st.date_input("Data inicial", datetime.date(2026, 1, 1), key="d_ini")
    d2 = st.date_input("Data final", datetime.date(2026, 12, 31), key="d_fim")
    if st.button("Calcular Dias", key="b_dias"):
      diff = (d2 - d1).days
      st.success(f"Total de dias entre as datas: {abs(diff)} dias")

  with aba_util[3]:
    st.subheader("Conversor de Temperatura")
    c_temp = st.number_input("Temperatura em Celsius (°C)", value=25.0, key="t_c")
    if st.button("Converter para Fahrenheit", key="b_temp"):
      f_temp = (c_temp * 9 / 5) + 32
      st.success(f"Temperatura em Fahrenheit: {f_temp:.1f} °F")

  with aba_util[4]:
    st.subheader("Calculadora de Gorjeta")
    conta = st.number_input("Valor da Conta (R$)", value=120.0, key="g_conta")
    porc = st.slider("Porcentagem de Gorjeta (%)", 0, 30, 10, key="g_porc")
    if st.button("Calcular Total", key="b_gorg"):
      gorjeta = conta * (porc / 100)
      st.success(
          f"Gorjeta: R$ {gorjeta:.2f} | Total com gorjeta: R$"
          f" {conta + gorjeta:.2f}"
      )

  with aba_util[5]:
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

  with aba_util[6]:
    st.subheader("Cálculo de Velocidade Média")
    d_vm = st.number_input("Distância percorrida (km)", value=150.0, key="vm_d")
    t_vm = st.number_input("Tempo gasto (horas)", value=2.5, key="vm_t")
    if st.button("Calcular Velocidade", key="b_vm"):
      vm = d_vm / t_vm
      st.success(f"Velocidade Média: {vm:.2f} km/h")

  with aba_util[7]:
    st.subheader("Conversor de Armazenamento Digital")
    val_gb = st.number_input("Valor em Gigabytes (GB)", value=50.0, key="st_gb")
    if st.button("Converter para MB", key="b_stor"):
      st.success(
          f"{val_gb} GB equivalem a {val_gb * 1024:.0f} MB ou"
          f" {val_gb / 1024:.2f} TB"
      )

  with aba_util[8]:
    st.subheader("Gerador de Senhas Seguras")
    tamanho = st.slider("Tamanho da senha", 6, 32, 12, key="s_tam")
    if st.button("Gerar Senha", key="b_senha"):
      chars = string.ascii_letters + string.digits + string.punctuation
      senha = "".join(random.choice(chars) for _ in range(tamanho))
      st.code(senha)

  with aba_util[9]:
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
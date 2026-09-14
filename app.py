import streamlit as st
from datetime import datetime, date
import random
import string

# Configuração da página com foco em SEO (Título rico e descritivo)
st.set_page_config(
    page_title="Central de Calculadoras Online Grátis | Ferramentas Práticas",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização profissional e limpa
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 1.15rem;
        color: #4B5563;
        margin-bottom: 25px;
    }
    .seo-box {
        background-color: #F8FAFC;
        border-left: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
        margin-bottom: 20px;
        font-size: 0.95rem;
        color: #334155;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Principal otimizado para palavras-chave
st.markdown('<p class="main-title">🧮 Central de Calculadoras Online e Ferramentas Práticas</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Resolva cálculos do dia a dia, conversões e formatações de texto de forma rápida, gratuita e sem precisar instalar nada.</p>', unsafe_allow_html=True)

# Menu Lateral Organizacional
categoria = st.sidebar.selectbox(
    "📂 Escolha a Categoria de Ferramentas:",
    [
        "Matemática & Proporção",
        "Texto & Formatação",
        "Segurança & Utilidades",
        "Datas & Horas",
        "Saúde & Corpo",
        "Conversão de Medidas"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Dica de SEO:** Sites rápidos, responsivos e com explicações detalhadas rankeiam mais rápido no Google!")

# ==========================================
# 1. MATEMÁTICA & PROPORÇÃO
# ==========================================
if categoria == "Matemática & Proporção":
    st.header("📐 Calculadoras de Matemática & Proporção")
    ferramenta = st.selectbox("Selecione a ferramenta específica:", [
        "Calculadora de Porcentagem", 
        "Regra de Três Simples", 
        "Média Aritmética", 
        "Cálculo de Frações"
    ])
    
    if ferramenta == "Calculadora de Porcentagem":
        st.subheader("Calculadora de Porcentagem Online")
        st.write("Calcule acréscimos, descontos e o valor percentual de qualquer quantia instantaneamente.")
        
        col1, col2 = st.columns(2)
        with col1:
            valor = st.number_input("Valor base (Ex: 150):", value=100.0)
        with col2:
            porcentagem = st.number_input("Porcentagem % (Ex: 15):", value=15.0)
            
        if st.button("Calcular Porcentagem", type="primary"):
            res = (valor * porcentagem) / 100
            st.success(f"O valor correspondente a {porcentagem}% de {valor} é: **{res:.2f}**")
            st.info(f"✨ **Valores Finais:** Com acréscimo: **{valor + res:.2f}** | Com desconto: **{valor - res:.2f}**")
            
        st.markdown("""
        <div class="seo-box">
        <b>Como usar esta calculadora de porcentagem para SEO:</b><br>
        Esta ferramenta ajuda estudantes, comerciantes e profissionais a resolver cálculos financeiros e de vendas do dia a dia. 
        Basta inserir o valor base e a porcentagem desejada para obter o resultado exato na hora.
        </div>
        """, unsafe_allow_html=True)

    elif ferramenta == "Regra de Três Simples":
        st.subheader("Calculadora de Regra de Três Simples")
        st.write("Resolva problemas de proporção matemática de forma simples e direta.")
        st.markdown("*Se **A** está para **B**, assim como **C** está para **X***")
        
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Valor A:", value=10.0)
            c = st.number_input("Valor C (proporção):", value=50.0)
        with col2:
            b = st.number_input("Valor B:", value=20.0)
            
        if st.button("Calcular Regra de Três", type="primary"):
            if a != 0:
                x = (b * c) / a
                st.success(f"O resultado de X é: **{x:.4f}**")
            else:
                st.error("O valor de 'A' não pode ser zero.")

    elif ferramenta == "Média Aritmética":
        st.subheader("Calculadora de Média Escolar e Aritmética")
        st.write("Calcule a média de notas, pontuações ou números informando os valores separados por vírgula.")
        
        numeros_str = st.text_input("Digite os números separados por vírgula:", value="7.0, 8.5, 9.0, 10.0")
        if st.button("Calcular Média", type="primary"):
            try:
                nums = [float(n.strip()) for n in numeros_str.split(",")]
                media = sum(nums) / len(nums)
                st.success(f"A média aritmética é: **{media:.2f}** (Total de elementos: {len(nums)})")
            except:
                st.error("Por favor, insira apenas números válidos separados por vírgula (ex: 7, 8, 9).")

    elif ferramenta == "Cálculo de Frações":
        st.subheader("Calculadora de Operações com Frações")
        col1, col2 = st.columns(2)
        with col1:
            n1 = st.number_input("Numerador 1", value=1, step=1)
            d1 = st.number_input("Denominador 1", value=2, step=1)
        with col2:
            n2 = st.number_input("Numerador 2", value=1, step=1, key="n2")
            d2 = st.number_input("Denominador 2", value=4, step=1, key="d2")
            
        operacao = st.selectbox("Escolha a operação:", ["Soma (+)", "Subtração (-)", "Multiplicação (×)", "Divisão (÷)"])
        
        if st.button("Calcular Fração", type="primary"):
            if d1 == 0 or d2 == 0:
                st.error("O denominador não pode ser zero.")
            else:
                if "Soma" in operacao:
                    num_res = (n1 * d2) + (n2 * d1)
                    den_res = d1 * d2
                elif "Subtração" in operacao:
                    num_res = (n1 * d2) - (n2 * d1)
                    den_res = d1 * d2
                elif "Multiplicação" in operacao:
                    num_res = n1 * n2
                    den_res = d1 * d2
                else:
                    num_res = n1 * d2
                    den_res = d1 * n2
                
                st.success(f"Resultado simplificado/fração: **{num_res}/{den_res}** (Valor decimal: {num_res/den_res:.4f})")

# ==========================================
# 2. TEXTO & FORMATAÇÃO
# ==========================================
elif categoria == "Texto & Formatação":
    st.header("📝 Ferramentas de Texto & Formatação")
    ferramenta = st.selectbox("Selecione a ferramenta:", [
        "Contador de Palavras e Caracteres", 
        "Remover Espaços Extras", 
        "Conversor Maiúsculas / Minúsculas"
    ])
    
    texto = st.text_area("Digite ou cole seu texto aqui:", value="Exemplo de texto para testar as ferramentas de formatação e contagem online.")
    
    if ferramenta == "Contador de Palavras e Caracteres":
        palavras = len(texto.split()) if texto.strip() else 0
        caracteres = len(texto)
        caracteres_sem_espaco = len(texto.replace(" ", ""))
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Palavras", palavras)
        col2.metric("Caracteres (com espaços)", caracteres)
        col3.metric("Caracteres (sem espaços)", caracteres_sem_espaco)

    elif ferramenta == "Remover Espaços Extras":
        if st.button("Remover Espaços Desnecessários", type="primary"):
            texto_limpo = " ".join(texto.split())
            st.subheader("Texto Limpo:")
            st.code(texto_limpo)

    elif ferramenta == "Conversor Maiúsculas / Minúsculas":
        col1, col2, col3 = st.columns(3)
        if col1.button("TUDO MAIÚSCULO"):
            st.code(texto.upper())
        if col2.button("tudo minúsculo"):
            st.code(texto.lower())
        if col3.button("Primeira Letra Maiúscula"):
            st.code(texto.title())

# ==========================================
# 3. SEGURANÇA & UTILIDADES
# ==========================================
elif categoria == "Segurança & Utilidades":
    st.header("🔒 Segurança & Utilidades Comerciais")
    ferramenta = st.selectbox("Selecione a ferramenta:", [
        "Gerador de Senhas Seguras", 
        "Calculadora de Desconto / Acréscimo Comercial"
    ])
    
    if ferramenta == "Gerador de Senhas Seguras":
        st.subheader("Gerador de Senhas Fortes Online")
        tamanho = st.slider("Tamanho da senha:", min_value=6, max_value=32, value=12)
        inc_maiusc = st.checkbox("Incluir Letras Maiúsculas (A-Z)", value=True)
        inc_nums = st.checkbox("Incluir Números (0-9)", value=True)
        inc_simbolos = st.checkbox("Incluir Símbolos Especiais (!@#$)", value=True)
        
        if st.button("Gerar Senha Segura", type="primary"):
            chars = string.ascii_lowercase
            if inc_maiusc: chars += string.ascii_uppercase
            if inc_nums: chars += string.digits
            if inc_simbolos: chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            senha = "".join(random.choice(chars) for _ in range(tamanho))
            st.success("Senha gerada com sucesso:")
            st.code(senha)

    elif ferramenta == "Calculadora de Desconto / Acréscimo Comercial":
        st.subheader("Calculadora de Preço com Desconto ou Aumento")
        preco_inicial = st.number_input("Valor original do produto (R$):", value=150.0)
        porcentagem_com = st.number_input("Percentual (%):", value=10.0)
        tipo = st.radio("Selecione a operação:", ["Desconto", "Aumento / Acréscimo"])
        
        if st.button("Calcular Preço Final", type="primary"):
            ajuste = (preco_inicial * porcentagem_com) / 100
            if tipo == "Desconto":
                final = preco_inicial - ajuste
                st.success(f"Desconto aplicado: R$ {ajuste:.2f} | **Preço Final com Desconto: R$ {final:.2f}**")
            else:
                final = preco_inicial + ajuste
                st.success(f"Acréscimo aplicado: R$ {ajuste:.2f} | **Preço Final com Aumento: R$ {final:.2f}**")

# ==========================================
# 4. DATAS & HORAS
# ==========================================
elif categoria == "Datas & Horas":
    st.header("📅 Calculadoras de Datas & Horas")
    ferramenta = st.selectbox("Selecione a ferramenta:", [
        "Calculadora de Idade Exata", 
        "Diferença de Dias entre Datas", 
        "Soma de Horas e Minutos"
    ])
    
    if ferramenta == "Calculadora de Idade Exata":
        st.subheader("Calculadora de Idade em Anos")
        nasc = st.date_input("Data de nascimento:", value=date(1995, 1, 1))
        if st.button("Calcular Idade", type="primary"):
            hoje = date.today()
            idade_anos = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
            st.success(f"Você possui **{idade_anos} anos** completos até hoje.")

    elif ferramenta == "Diferença de Dias entre Datas":
        st.subheader("Calculadora de Intervalo de Dias")
        col1, col2 = st.columns(2)
        with col1:
            data1 = st.date_input("Data Inicial:", value=date.today())
        with col2:
            data2 = st.date_input("Data Final:", value=date.today())
            
        if st.button("Calcular Diferença de Dias", type="primary"):
            diferenca = abs((data2 - data1).days)
            st.success(f"O intervalo entre as duas datas é de **{diferenca} dias** (cerca de {diferenca/30:.1f} meses).")

    elif ferramenta == "Soma de Horas e Minutos":
        st.subheader("Somador de Jornada de Trabalho (Horas)")
        st.write("Insira os horários no formato HH:MM para somá-los (Ex: 08:30 e 02:15).")
        h1 = st.text_input("Horário 1 (HH:MM):", value="08:00")
        h2 = st.text_input("Horário 2 (HH:MM):", value="02:30")
        
        if st.button("Somar Horas", type="primary"):
            try:
                def para_minutos(h_str):
                    partes = h_str.split(":")
                    return int(partes[0]) * 60 + int(partes[1])
                
                total_min = para_minutos(h1) + para_minutos(h2)
                horas_res = total_min // 60
                min_res = total_min % 60
                st.success(f"Total somado: **{horas_res}h {min_res:02d}min**")
            except:
                st.error("Formato inválido. Certifique-se de usar o padrão HH:MM (ex: 07:30).")

# ==========================================
# 5. SAÚDE & CORPO
# ==========================================
elif categoria == "Saúde & Corpo":
    st.header("💪 Saúde & Bem-Estar")
    ferramenta = st.selectbox("Selecione a ferramenta:", [
        "Calculadora de IMC (Índice de Massa Corporal)", 
        "Gasto Calórico Diário (TMB)"
    ])
    
    if ferramenta == "Calculadora de IMC (Índice de Massa Corporal)":
        st.subheader("Calculadora de IMC Online")
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("Seu Peso (kg):", value=70.0)
        with col2:
            altura = st.number_input("Sua Altura (m):", value=1.75)
            
        if st.button("Calcular IMC", type="primary"):
            if altura > 0:
                imc = peso / (altura ** 2)
                st.success(f"O seu Índice de Massa Corporal (IMC) é: **{imc:.2f}**")
                if imc < 18.5: st.warning("Classificação: Abaixo do peso")
                elif 18.5 <= imc < 25: st.info("Classificação: Peso normal (Saudável)")
                elif 25 <= imc < 30: st.warning("Classificação: Sobrepeso")
                else: st.error("Classificação: Obesidade")

    elif ferramenta == "Gasto Calórico Diário (TMB)":
        st.subheader("Taxa Metabólica Basal e Gasto Diário")
        peso = st.number_input("Peso (kg):", value=70.0, key="tmb_p")
        altura_cm = st.number_input("Altura (cm):", value=175.0)
        idade = st.number_input("Idade (anos):", value=30, step=1)
        genero = st.radio("Gênero biológico:", ["Masculino", "Feminino"])
        
        if st.button("Calcular Gasto Calórico", type="primary"):
            if genero == "Masculino":
                tmb = 88.36 + (13.4 * peso) + (4.8 * altura_cm) - (5.7 * idade)
            else:
                tmb = 447.6 + (9.2 * peso) + (3.1 * altura_cm) - (4.3 * idade)
                
            st.success(f"Sua TMB (Gasto Calórico em Repouso): **{tmb:.0f} calorias/dia**")
            st.info(f"💡 Para manter o peso (atividade leve): **{tmb * 1.375:.0f} kcal** | Para ganho de massa: **{(tmb * 1.375) + 400:.0f} kcal**")

# ==========================================
# 6. CONVERSÃO DE MEDIDAS
# ==========================================
elif categoria == "Conversão de Medidas":
    st.header("🔄 Conversão de Medidas Práticas")
    ferramenta = st.selectbox("Selecione a conversão:", ["Temperatura", "Comprimento", "Peso"])
    
    if ferramenta == "Temperatura":
        st.subheader("Conversor de Temperatura (Celsius ⇄ Fahrenheit)")
        val = st.number_input("Valor da temperatura:", value=25.0)
        direcao = st.radio("Direção da conversão:", ["Celsius para Fahrenheit", "Fahrenheit para Celsius"])
        if st.button("Converter Temperatura", type="primary"):
            if "Celsius para" in direcao:
                res = (val * 9/5) + 32
                st.success(f"{val} °C equivale a **{res:.2f} °F**")
            else:
                res = (val - 32) * 5/9
                st.success(f"{val} °F equivale a **{res:.2f} °C**")

    elif ferramenta == "Comprimento":
        st.subheader("Conversor de Metros para Centímetros e Quilômetros")
        val = st.number_input("Valor em metros (m):", value=100.0)
        if st.button("Converter Comprimento", type="primary"):
            st.success(f"**{val} metros** correspondem a:")
            st.write(f"- {val / 1000} Quilômetros (km)")
            st.write(f"- {val * 100} Centímetros (cm)")
            st.write(f"- {val * 1000} Milímetros (mm)")

    elif ferramenta == "Peso":
        st.subheader("Conversor de Quilogramas para Gramas")
        val = st.number_input("Valor em Quilogramas (kg):", value=1.0)
        if st.button("Converter Peso", type="primary"):
            st.success(f"**{val} kg** equivalem a **{val * 1000:,.0f} gramas (g)**.")
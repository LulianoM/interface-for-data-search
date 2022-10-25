import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

st.header("Mapeamento de utilitários na Cidade Universitária (UFRJ - Ilha do Fundão)")
st.text(" Discentes: Débora Mendes e Fernanda Faria \nDocente: Rafael Barros \nLaboratório de Geoprocessamento 2022.2 ")


# Nome do Estabelecimento
st.text_input("Nome do Estabelecimento")

# Categoria do Estabelecimento:
category_place = st.multiselect("Categoria do Estabelecimento:", ["Chaveiro","Correios","Papelaria",
"Farmácia","Gráfica","Livraria","Material de Construção","Xerox","Clube","Academia","Outro"])

if "Outro" in category_place:   
    st.text_input("Caso em outro escreva aqui:")

# Dias de Funcionamento
days_of_working_place = st.multiselect("Dias de Funcionamento", ["Seg. a Sex.", "Seg. a Sab.", "Todos os dias", "Outro"])
if "Outro" in days_of_working_place:   
    st.text_input("Caso em outro escreva aqui:")

# Horário de abertura (dias de semana)
st.time_input("Horário de abertura (dias de semana)")

# Horário de fechamento (dias de semana)
st.time_input("Horário de fechamento (dias de semana)")

# Outros horários de funcionamento (final de semana)
st.text_input("Outros horários de funcionamento (final de semana)")

# Horário de funcionamento e dias para atendimento gerencial (exclusivo para bancos)
st.text_input("Horário de funcionamento e dias para atendimento gerencial (exclusivo para bancos)")

# Localização com ponto de referência (ex.: CCMN perto do Bloco F, em frente a X lugar)
st.text_input("Localização com ponto de referência (ex.: CCMN perto do Bloco F, em frente a X lugar)")

# Coordenadas Geográficas (ex.: -22.5664, -43.6695)
st.text("Coordenadas Geográficas (ex.: -22.5664, -43.6695)")
loc_button = Button(label="Get Location")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)
st.info(result)

# Local
st.selectbox("Selecione o Local:", ["Letras - FL","CCMN","FAU","CT","CCS","EEFD","EBA","Vila Residencial",])

# Foto para reconhecimento
photo =  st.selectbox("Deseja tirar foto do local ou subir um arquivo imagem?", [ "Subir Arquivo", "Foto"])
if photo == 'Foto':
    st.camera_input("Foto do local de reconhecimento")
elif photo == "Subir Arquivo":
    st.file_uploader("Suba seu arquivo aqui")

# Contato (telefone, ex.: (21) 9xxxxxxxx)
st.text_input("Contato (telefone, ex.: (21) 9xxxxxxxx)")

# Atendimento oferecido no Banco
atend_offer_bank = st.multiselect("Atendimento oferecido no Banco", ["Atendimento ao cliente presencial","Saque e depósito","Saques","Outro",])
if "Outro" in atend_offer_bank:   
    st.text_input("Caso em outro escreva aqui:")
    
# Forma de pagamento (Exclusivo para estabelecimentos de compra e venda)
payment_form = st.multiselect("Forma de pagamento (Exclusivo para estabelecimentos de compra e venda)", ["Cartão de crédito","Cartão de débito","Dinheiro","Pix", "Outro"])
if "Outro" in payment_form:   
    st.text_input("Caso em outro escreva aqui:")

# Envio e recebimento de encomendas? (exclusivo para a categoria "Correios")
st.text_input("Envio e recebimento de encomendas? (exclusivo para a categoria Correios)")

# Entrega dentro da UFRJ? (exclusivo para a categoria "Farmácia")
st.selectbox("Entrega dentro da UFRJ? (exclusivo para a categoria Farmácia)", ["SIM", "NÃO"])

if st.button("ENVIAR"):
    st.balloons()

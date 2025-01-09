import streamlit as st

# Título da página
st.title("Plano de Aula Interativo - Xadrez e Método Hipotético-Dedutivo")

# Informações básicas
st.header("Informações Básicas")
professor = st.text_input("Nome do Professor")
disciplina = st.text_input("Disciplina")
duracao = st.text_input("Duração da Aula")
numero_alunos = st.number_input("Número de Alunos", min_value=1, step=1)
tema = st.text_input("Tema")

# Competências e Habilidades
st.header("Competências e Habilidades")
competencias = st.text_area("Competências de Área")
habilidades = st.text_area("Habilidades")

# Conteúdo e Recursos
st.header("Conteúdo e Recursos")
conteudo = st.text_area("Conteúdo")
recursos = st.text_area("Recursos")

# Organização dos Espaços
st.header("Organização dos Espaços")
st.subheader("Espaço 1")
atividade_espaco1 = st.text_area("Atividade no Espaço 1")
duracao_espaco1 = st.text_input("Duração do Espaço 1")
papel_aluno1 = st.text_area("Papel do Aluno no Espaço 1")
papel_professor1 = st.text_area("Papel do Professor no Espaço 1")

st.subheader("Espaço 2")
atividade_espaco2 = st.text_area("Atividade no Espaço 2")
duracao_espaco2 = st.text_input("Duração do Espaço 2")
papel_aluno2 = st.text_area("Papel do Aluno no Espaço 2")
papel_professor2 = st.text_area("Papel do Professor no Espaço 2")

st.subheader("Espaço 3")
atividade_espaco3 = st.text_area("Atividade no Espaço 3")
duracao_espaco3 = st.text_input("Duração do Espaço 3")
papel_aluno3 = st.text_area("Papel do Aluno no Espaço 3")
papel_professor3 = st.text_area("Papel do Professor no Espaço 3")

# Avaliação
st.header("Avaliação")
avaliacao_objetivos = st.text_area("O que pode ser feito para observar se os objetivos da aula foram cumpridos?")
avaliacao_feedback = st.text_area("Como foi sua avaliação da aula? (Aspectos positivos e negativos)")

# **Objetivo Específico para o Método Hipotético-Dedutivo**
st.header("Objetivo Específico para o Método Hipotético-Dedutivo")
objetivo_mhd = st.text_area("Defina o objetivo específico para a utilização do MHD na aula")

# **Etapas do Método Hipotético-Dedutivo**
st.header("Etapas do Método Hipotético-Dedutivo")
observacao = st.text_area("Observação")
hipotese = st.text_area("Hipótese")
deducao = st.text_area("Dedução")
teste_experimental = st.text_area("Teste Experimental")
analise_consolidacao = st.text_area("Análise e Consolidação")

# Registro e Reflexão
st.header("Registro e Reflexão")
registro_alunos = st.text_area("Registro dos Alunos")
questionamentos = st.text_area("Questionamentos Norteadores")
reflexao_final = st.text_area("Reflexão Final")

# Botão para salvar o plano
if st.button("Gerar Plano de Aula"):
    st.success("Plano de aula gerado com sucesso!")
    st.write("### Resumo do Plano de Aula:")
    st.write(f"**Nome do Professor:** {professor}")
    st.write(f"**Disciplina:** {disciplina}")
    st.write(f"**Duração da Aula:** {duracao}")
    st.write(f"**Número de Alunos:** {numero_alunos}")
    st.write(f"**Tema:** {tema}")
    st.write("**Competências de Área:**", competencias)
    st.write("**Habilidades:**", habilidades)
    st.write("**Conteúdo:**", conteudo)
    st.write("**Recursos:**", recursos)
    st.write("**Organização dos Espaços:**")
    st.write("- **Espaço 1:**", atividade_espaco1, "| Duração:", duracao_espaco1)
    st.write("- **Espaço 2:**", atividade_espaco2, "| Duração:", duracao_espaco2)
    st.write("- **Espaço 3:**", atividade_espaco3, "| Duração:", duracao_espaco3)
    st.write("**Avaliação:**", avaliacao_objetivos)
    st.write("**Objetivo Específico para o Método Hipotético-Dedutivo:**", objetivo_mhd)
    st.write("**Etapas do Método Hipotético-Dedutivo:**")
    st.write("- **Observação:**", observacao)
    st.write("- **Hipótese:**", hipotese)
    st.write("- **Dedução:**", deducao)
    st.write("- **Teste Experimental:**", teste_experimental)
    st.write("- **Análise e Consolidação:**", analise_consolidacao)
    st.write("**Reflexão Final:**", reflexao_final)

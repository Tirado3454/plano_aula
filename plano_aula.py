import streamlit as st

# Título da página
st.title("Plano de Aula Interativo - Xadrez e Método Hipotético-Dedutivo")

# Informações básicas
st.header("Informações Básicas")
professor = st.text_input("Nome do Professor")
disciplina = st.text_input("Disciplina")
duracao = st.text_input("Duração da Aula")
numero_alunos = st.number_input("Número de Alunos", min_value=1, step=1)
tema = st.text_input("Tema", help="Descreva o tema central da aula, como 'Estratégias de Xadrez' ou 'Método Hipotético-Dedutivo no Xadrez'.")

# Competências e Habilidades
st.header("Competências e Habilidades")
competencias = st.text_area("Competências de Área", help="Liste as competências gerais que serão desenvolvidas, como 'Análise crítica' ou 'Raciocínio lógico'.")
habilidades = st.text_area("Habilidades", help="Defina as habilidades específicas, como 'Formular hipóteses estratégicas' ou 'Testar ideias no tabuleiro'.")

# Conteúdo e Recursos
st.header("Conteúdo e Recursos")
conteudo = st.text_area("Conteúdo", help="Detalhe os conteúdos abordados na aula, como 'Etapas do método hipotético-dedutivo' ou 'Fundamentos do xadrez'.")
recursos = st.text_area("Recursos", help="Liste os materiais e ferramentas necessários, como 'Tabuleiros físicos', 'Aplicativo Xadrez e Ciência' ou 'Computadores'.")

# Organização dos Espaços
st.header("Organização dos Espaços")
st.subheader("Espaço 1")
atividade_espaco1 = st.text_area("Atividade no Espaço 1", help="Descreva a atividade inicial da aula, como 'Introdução ao método hipotético-dedutivo'.")
duracao_espaco1 = st.text_input("Duração do Espaço 1")
papel_aluno1 = st.text_area("Papel do Aluno no Espaço 1", help="Indique o que os alunos farão neste momento, como 'Observar e discutir as posições no tabuleiro'.")
papel_professor1 = st.text_area("Papel do Professor no Espaço 1", help="Descreva a função do professor, como 'Orientar e explicar os conceitos'.")
    
st.subheader("Espaço 2")
atividade_espaco2 = st.text_area("Atividade no Espaço 2", help="Defina a atividade intermediária, como 'Utilizar o aplicativo para testar hipóteses'.")
duracao_espaco2 = st.text_input("Duração do Espaço 2")
papel_aluno2 = st.text_area("Papel do Aluno no Espaço 2", help="Indique o que os alunos farão neste momento, como 'Testar estratégias e registrar resultados'.")
papel_professor2 = st.text_area("Papel do Professor no Espaço 2", help="Descreva a função do professor, como 'Acompanhar os testes e fornecer feedback'.")
    
st.subheader("Espaço 3")
atividade_espaco3 = st.text_area("Atividade no Espaço 3", help="Descreva a atividade final da aula, como 'Discutir os resultados obtidos e consolidar o aprendizado'.")
duracao_espaco3 = st.text_input("Duração do Espaço 3")
papel_aluno3 = st.text_area("Papel do Aluno no Espaço 3", help="Explique a participação dos alunos, como 'Compartilhar reflexões e aprender com os colegas'.")
papel_professor3 = st.text_area("Papel do Professor no Espaço 3", help="Defina o papel do professor, como 'Medir e conduzir as discussões'.")
    
# Avaliação
st.header("Avaliação")
avaliacao_objetivos = st.text_area("O que pode ser feito para observar se os objetivos da aula foram cumpridos?", help="Liste os indicadores ou critérios para avaliar se os objetivos da aula foram alcançados.")
avaliacao_feedback = st.text_area("Como foi sua avaliação da aula? (Aspectos positivos e negativos)", help="Reflexão sobre o que funcionou bem e o que pode ser melhorado na aula.")

# Objetivo Específico para o Método Hipotético-Dedutivo
st.header("Objetivo Específico para o Método Hipotético-Dedutivo")
objetivo_mhd = st.text_area("Defina o objetivo específico para a utilização do MHD na aula", help="Explique como o MHD será aplicado, por exemplo: 'Ensinar os alunos a formular hipóteses e testá-las no tabuleiro'.")
    
# Etapas do Método Hipotético-Dedutivo
st.header("Etapas do Método Hipotético-Dedutivo")
observacao = st.text_area("Observação", help="O que os alunos devem observar inicialmente? Por exemplo: 'A posição atual no tabuleiro'.")
hipotese = st.text_area("Hipótese", help="Que hipóteses os alunos devem propor? Por exemplo: 'O próximo movimento ideal para vencer'.")
deducao = st.text_area("Dedução", help="Como as hipóteses serão analisadas? Por exemplo: 'Prevendo os desdobramentos das jogadas'.")
teste_experimental = st.text_area("Teste Experimental", help="Explique como os alunos testarão suas hipóteses. Exemplo: 'Executar as jogadas no aplicativo'.")
analise_consolidacao = st.text_area("Análise e Consolidação", help="Descreva como os resultados serão analisados. Exemplo: 'Comparar o resultado com a hipótese inicial'.")
    
# Registro e Reflexão
st.header("Registro e Reflexão")
registro_alunos = st.text_area("Registro dos Alunos", help="Explique como os alunos devem registrar suas hipóteses, testes e resultados.")
questionamentos = st.text_area("Questionamentos Norteadores", help="Liste perguntas para guiar os alunos, como 'O que você espera alcançar com este movimento?'.")
reflexao_final = st.text_area("Reflexão Final", help="Descreva a discussão final e os aprendizados a serem consolidados.")
    
# Botão para salvar o plano
if st.button("Gerar Plano de Aula"):
    st.success("Plano de aula gerado com sucesso!")

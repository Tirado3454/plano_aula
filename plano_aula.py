from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import base64
import streamlit as st

def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Formulário para os campos do planejamento
    with st.form("planejamento_form"):
        st.subheader("Informações Gerais")
        professor = st.text_input("Nome do Professor:", help="Digite o nome completo do professor responsável pela aula.")
        disciplina = st.text_input("Disciplina:", help="Informe a disciplina relacionada ao plano de aula.")
        duracao = st.text_input("Duração da Aula:", help="Informe o tempo total planejado para a aula.")
        numero_alunos = st.text_input("Número de Alunos:", help="Especifique o número estimado de alunos para esta aula.")
        tema = st.text_input("Tema:", help="Defina o tema principal que será abordado na aula.")

        st.subheader("Competências, Conteúdo e Recursos")
        competencia = st.text_area("Competência de Área:", help="Descreva as competências que serão trabalhadas, alinhadas à BNCC ou outro documento oficial.")
        habilidades = st.text_area("Habilidades:", help="Liste as habilidades que os alunos deverão desenvolver.")
        conteudo = st.text_area("Conteúdo:", help="Detalhe os conteúdos que serão abordados.")
        recursos = st.text_area("Recursos:", help="Especifique os materiais, ferramentas ou equipamentos necessários.")

        st.subheader("Organização dos Espaços")
        espacos = []
        for i in range(1, 4):
            st.markdown(f"**Espaço {i}**")
            atividade = st.text_area(f"Espaço {i} - Atividade:", help="Descreva a atividade realizada neste espaço.")
            duracao_espaco = st.text_input(f"Espaço {i} - Duração:", help="Informe a duração estimada para esta atividade.")
            papel_aluno = st.text_area(f"Espaço {i} - Papel do Aluno:", help="Explique o papel dos alunos nesta atividade.")
            papel_professor = st.text_area(f"Espaço {i} - Papel do Professor:", help="Explique o papel do professor nesta atividade.")
            espacos.append((atividade, duracao_espaco, papel_aluno, papel_professor))

        st.subheader("Avaliação")
        avaliacao_objetivos = st.text_area("Avaliação dos Objetivos:", help="Descreva como os objetivos da aula serão avaliados.")
        avaliacao_aula = st.text_area("Avaliação da Aula:", help="Faça uma avaliação geral da aula, destacando pontos positivos e aspectos a melhorar.")

        st.subheader("Etapas do Método Hipotético-Dedutivo")
        observacao = st.text_area("Observação:", help="Descreva as observações iniciais feitas antes de começar a aula.")
        hipotese = st.text_area("Hipótese:", help="Apresente as hipóteses levantadas a partir da observação.")
        deducao = st.text_area("Dedução:", help="Explique a dedução feita a partir das hipóteses.")
        teste = st.text_area("Teste Experimental:", help="Detalhe o teste experimental realizado para validar as hipóteses.")
        analise = st.text_area("Análise e Consolidação:", help="Apresente a análise final e os resultados consolidados.")

        st.subheader("Reflexão e Registros")
        registro = st.text_area("Registro dos Alunos:", help="Registre as reflexões ou observações feitas pelos alunos.")
        questionamentos = st.text_area("Questionamentos Norteadores:", help="Liste perguntas que guiarão a aula e a discussão.")
        reflexao = st.text_area("Reflexão Final:", help="Escreva a reflexão final sobre a aula, considerando os aprendizados e desafios.")

        submitted = st.form_submit_button("Gerar PDF")

    if submitted:
        # Geração do PDF
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        margin_x = 50
        margin_y = 70
        y = height - margin_y - 30

        def draw_wrapped_text(canvas, text, x, y, max_width, line_height):
            """Desenha texto justificado com verificação de quebra de página."""
            words = text.split()
            line = ""
            for word in words:
                test_line = " ".join([line, word]).strip()
                if canvas.stringWidth(test_line, "Helvetica", 12) < max_width:
                    line = test_line
                else:
                    canvas.drawString(x, y, line)
                    y -= line_height
                    if y < margin_y:
                        canvas.showPage()
                        y = height - margin_y - 30
                        canvas.setFont("Helvetica", 12)
                    line = word
            if line:
                canvas.drawString(x, y, line)
                y -= line_height
                if y < margin_y:
                    canvas.showPage()
                    y = height - margin_y - 30
                    canvas.setFont("Helvetica", 12)
            return y

        def add_section(canvas, title, fields, y):
            """Adiciona seções com verificação de espaço e títulos."""
            canvas.setFont("Helvetica-Bold", 14)
            canvas.drawString(margin_x, y, title)
            y -= 30
            for label, value in fields:
                canvas.setFont("Helvetica", 12)
                canvas.drawString(margin_x, y, f"{label}:")
                y -= 20
                y = draw_wrapped_text(canvas, value, margin_x + 20, y, width - 2 * margin_x, 15)
                y -= 20
                if y < margin_y:
                    canvas.showPage()
                    y = height - margin_y - 30
            return y

        # Adicionar todas as seções
        y = add_section(c, "Informações Gerais", [
            ("Nome do Professor", professor),
            ("Disciplina", disciplina),
            ("Duração da Aula", duracao),
            ("Número de Alunos", numero_alunos),
            ("Tema", tema),
        ], y)

        y = add_section(c, "Competências, Conteúdo e Recursos", [
            ("Competência de Área", competencia),
            ("Habilidades", habilidades),
            ("Conteúdo", conteudo),
            ("Recursos", recursos),
        ], y)

        y = add_section(c, "Organização dos Espaços", [
            (f"Espaço {i+1} - Atividade", esp[0]),
            (f"Espaço {i+1} - Duração", esp[1]),
            (f"Espaço {i+1} - Papel do Aluno", esp[2]),
            (f"Espaço {i+1} - Papel do Professor", esp[3])
        ] for i, esp in enumerate(espacos), y)

        y = add_section(c, "Avaliação", [
            ("Avaliação dos Objetivos", avaliacao_objetivos),
            ("Avaliação da Aula", avaliacao_aula),
        ], y)

        y = add_section(c, "Etapas do Método Hipotético-Dedutivo", [
            ("Observação", observacao),
            ("Hipótese", hipotese),
            ("Dedução", deducao),
            ("Teste Experimental", teste),
            ("Análise e Consolidação", analise),
        ], y)

        y = add_section(c, "Reflexão e Registros", [
            ("Registro dos Alunos", registro),
            ("Questionamentos Norteadores", questionamentos),
            ("Reflexão Final", reflexao),
        ], y)

        # Finalizar PDF
        c.save()
        buffer.seek(0)

        # Exibir e baixar PDF
        pdf_data = buffer.getvalue()
        st.markdown("### Visualização do PDF")
        st.markdown(
            f'<iframe src="data:application/pdf;base64,{base64.b64encode(pdf_data).decode()}" width="700" height="500"></iframe>',
            unsafe_allow_html=True,
        )
        st.download_button(
            label="Baixar PDF",
            data=pdf_data,
            file_name="planejamento_aula.pdf",
            mime="application/pdf",
        )

if __name__ == "__main__":
    planejamento_aula_function()
